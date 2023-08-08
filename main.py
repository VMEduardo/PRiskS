import os
from calculate_risk_scores import calculate_all_scores
from filter_snps import filter_all_vcfs
from visualize import plot_individual_scores
from common import snp_weights

# Directory with the original VCF files
vcf_directory = 'data' # Update this if your VCF files are in a different directory

# Directory for the filtered VCF files
filtered_vcf_directory = 'runtime/filtered_vcfs'
os.makedirs(filtered_vcf_directory, exist_ok=True)

# Filename for the risk scores
scores_filename = 'runtime/risk_scores.csv'

# Filter the SNPs of interest from all the VCF files
filter_all_vcfs(vcf_directory, filtered_vcf_directory, snp_weights)

# Calculate the polygenic risk scores
calculate_all_scores(filtered_vcf_directory, scores_filename)

# Visualize the scores
plot_individual_scores(scores_filename)
