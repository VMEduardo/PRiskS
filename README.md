PRiskS: Polygenic Risk Score (PRS) calculator

Description
PRiskS (Polygenic Risk Score System) is a program that calculates and visualizes Polygenic Risk Scores (PRS) from an individual's genetic data. The program uses VCF (Variant Call Format) files and SNP weights to calculate the PRS for various diseases. These scores are then visualized in bar charts, one for each individual.

Project Structure

PRiskS
├── .gitignore
├── data
│   ├── individual1.vcf
│   ├── individual2.vcf
│   ├── ... (more .vcf files as needed)
│   └── snp_weights.csv
├── runtime
│   └── risk_scores.csv (this file is generated during execution)
├── common.py
├── filter_snps.py
├── calculate_risk_scores.py
├── visualize.py
└── main.py

Usage
Make sure you have your VCF files and SNP weights CSV files in the data directory. If your VCF files are not in this directory, make sure to update the vcf_directory variable in main.py to reflect the correct location of your VCF files.

To run the program, use the command: python main.py

The polygenic risk scores will be calculated and saved in runtime/risk_scores.csv. In addition, bar charts will be generated for each individual showing their PRS for various diseases.

Script Descriptions
common.py: Loads the SNP weights from the CSV files in the data directory.
filter_snps.py: Filters the SNPs of interest from all the VCF files in a directory and writes the results to corresponding output files.
calculate_risk_scores.py: Calculates the total genetic risk scores for all filtered VCF files in a directory and writes the results to a CSV output file.
visualize.py: Takes a CSV file and generates a graph for each individual.
main.py: Main script that coordinates the execution of the other scripts.

Dependencies
Python 3.6 or later
pandas
matplotlib
