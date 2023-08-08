import os
import pandas as pd
from common import load_snp_weights, snp_weights
from collections import defaultdict

def get_genotype_weight(snp_id, genotype, snp_weights):
    """
    This function takes a SNP ID, a genotype, and a DataFrame of SNP weights,
    and returns the correct weight
    """
    # Handle unexpected genotypes
    if genotype == '1|0':
        genotype = '0|1'
    
    # Find the SNP in the DataFrame
    snp_info = snp_weights.loc[snp_weights['SNP'] == snp_id]

    if snp_info.empty:
        print(f"Warning: SNP ID {snp_id} not found in snp_weights DataFrame. Skipping this SNP.")
        return None
        
    # Find the weight associated with the genotype
    try:
        weight = snp_info[genotype].values[0]
    except KeyError:
        print(f"Warning: Genotype {genotype} not found for SNP ID {snp_id} in snp_weights DataFrame.")
        return None

    return weight


def calculate_score(vcf_filename, snp_weights):
    """
    This function calculates the genetic risk score for an individual VCF file.
    """
    scores = {}
    for disease in snp_weights.keys():
        total_scores = defaultdict(float)
        with open(vcf_filename, 'r') as vcf_file:
            for line in vcf_file:
                # Ignore metadata lines in VCF file
                if line.startswith('#'):
                    continue

                # Separate the fields from the line
                fields = line.strip().split()

                # Check the fields and print out the problematic line
                if len(fields) < 10:  # Need at least CHROM to FORMAT fields
                    print("Unexpected line format: ", line)
                    continue

                # Gets the SNP ID and genotypes (field #2 and all after #9 in the VCF file)
                snp_id = fields[2]
                genotypes = fields[9:]  # All fields after FORMAT are genotypes

                for i, genotype in enumerate(genotypes):
                    # Assume the genotype is the first field in the format information
                    genotype = genotype.split(':')[0]

                    # Calculate genotype weight
                    genotype_weight = get_genotype_weight(snp_id, genotype, snp_weights[disease])

                    # Add to total score only if genotype_weight is not None
                    if genotype_weight is not None:
                        total_scores[i] += genotype_weight

        for i, score in total_scores.items():
            scores[(disease, i)] = score
    return scores




def calculate_all_scores(filtered_vcf_directory, output_filename):
    """
    This function calculates the total genetic risk scores for all filtered VCF files in a directory and writes the results to a CSV output file.
    """
    scores = []

    for filename in os.listdir(filtered_vcf_directory):
        if filename.endswith('_filtered.vcf'):
            vcf_filename = os.path.join(filtered_vcf_directory, filename)
            individual_scores = calculate_score(vcf_filename, snp_weights)
            # Since the filename contains the individual name
            individual_name = filename.replace('_filtered.vcf', '')
            for (disease, index), score in individual_scores.items():
                scores.append({'Individual': f"{individual_name}_{index}", 'Disease': disease, 'Score': score})

    scores_df = pd.DataFrame(scores)
    scores_df.to_csv(output_filename, index=False)

