import os
import pandas as pd

def load_snp_weights(directory):
    """
    This function loads the SNP weights from all CSV files in a directory into a dictionary of pandas DataFrames.
    """
    snp_weights = {}
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            disease = filename[:-4]
            snp_weights[disease] = pd.read_csv(os.path.join(directory, filename))
    return snp_weights

# Load SNP weights from csv files in snp_weights directory
snp_weights = load_snp_weights("data/snp_weights")

