import pandas as pd
import os
import gzip
import shutil
from common import load_snp_weights

def filter_snps(vcf_filename, output_filename, snp_weights):
    """
    Takes the VCF file, filter SNPs of interest and write the result on a new file
    """
    # Extract all SNPs of interest from the snp_weights
    snps_of_interest = set()
    for disease in snp_weights:
        snps_of_interest.update(snp_weights[disease]['SNP'].values)

    # Choose the correct method to open the file based on its extension
    if vcf_filename.endswith('.vcf.gz'):
        file_opener = gzip.open
    elif vcf_filename.endswith('.vcf'):
        file_opener = open
    else:
        print(f"Unsupported file extension for {vcf_filename}")
        return

    with file_opener(vcf_filename, 'rt') as vcf_file, open(output_filename, 'w') as output_file:
        for line in vcf_file:
            # ignore metadata rows on VCF file
            if line.startswith('#'):
                continue

            # Separate the fields from the line
            fields = line.strip().split()

            # Check if the line has the correct number of fields
            if len(fields) < 3:
                continue

            # Gets the SNP ID (field #2 in the VCF file)
            snp_id = fields[2]

            # If the SNP is in our list of SNPs of interest, write it to the output file
            if snp_id in snps_of_interest:
                output_file.write(line)


def filter_all_vcfs(vcf_directory, output_directory, snp_weights):
    """
    This function filters the SNPs of interest from all VCF files in a directory
    and writes the results to corresponding output files in another directory
    """
    for filename in os.listdir(vcf_directory):
        if filename.endswith('.vcf.gz'):
            vcf_filename = os.path.join(vcf_directory, filename)
            output_filename = os.path.join(output_directory, filename.replace('.vcf.gz', '_filtered.vcf'))
            filter_snps(vcf_filename, output_filename, snp_weights)
        elif filename.endswith('.vcf'):
            vcf_filename = os.path.join(vcf_directory, filename)
            output_filename = os.path.join(output_directory, filename.replace('.vcf', '_filtered.vcf'))
            filter_snps(vcf_filename, output_filename, snp_weights)


