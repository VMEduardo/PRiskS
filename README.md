PRiskS: Polygenic Risk Score (PRS) calculator

Description
PRiskS (Polygenic Risk Score System) is a program that calculates and visualizes Polygenic Risk Scores (PRS) from an individual's genetic data. The program uses VCF (Variant Call Format) files and SNP weights to calculate the PRS for various diseases. These scores are then visualized in bar charts, one for each individual.

Project Structure

PRiskS
PRiskS
│
├── .gitignore
│
├── data
│   ├── individual1.vcf
│   ├── individual2.vcf
│   ├── ... (otros archivos .vcf según sea necesario)
│   └── snp_weights
│       └── diseases.csv
│
├── runtime
│   └── risk_scores.csv (este archivo se genera durante la ejecución)
│
├── common.py
├── filter_snps.py
├── calculate_risk_scores.py
├── visualize.py
└── main.py

File Details:
common.py: Defines common functions used throughout the project, in particular, the function to load SNP weights from CSV files in a directory.

filter_snps.py: Contains functions to filter SNPs of interest from VCF files and write the results to new filtered VCF files.

calculate_risk_scores.py: Defines functions to calculate the genetic risk scores based on the filtered VCF files and the SNP weights associated with diseases.

visualize.py: Provides a function to visualize and save graphs of genetic risk scores for each individual.

main.py: Is the main script that orchestrates the entire process, from filtering SNPs, calculating PRS, to visualizing the results.

How to Use:
Place your VCF files in the data folder.

Ensure you have the correct CSV files with SNP weights for diseases in the data/snp_weights folder.

Run main.py.

Once executed, the program will filter SNPs of interest, calculate PRS, and generate PRS graphs for each individual. These graphs will be saved in a folder called graphs.

The calculated genetic risk scores for each individual and disease will be saved in runtime/risk_scores.csv

Notes:
Ensure that the CSV files in the snp_weights folder are structured correctly, with an 'SNP' column and other columns for the genotypes and their corresponding weights.
VCF files can be either uncompressed (.vcf) or compressed (.vcf.gz).
Graphs will be generated only for individuals with a non-zero PRS.