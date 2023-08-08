import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

mpl.rcParams['figure.max_open_warning'] = 0

def plot_individual_scores(scores_filename):
    """
    The function takes a csv and generate a graph for each individual
    """
    # Load the PRS from csv file
    scores_df = pd.read_csv(scores_filename)

    # Get a list of all individuals
    individuals = scores_df['Individual'].unique()

    # Ensure a directory exists to save the graphs
    output_directory = 'graphs'
    os.makedirs(output_directory, exist_ok=True)

    # Generate a graph for each individual
    for individual in individuals:
        individual_df = scores_df[scores_df['Individual'] == individual]
        
        # Skip individuals with zero PRS
        if individual_df['Score'].sum() == 0:
            continue
        
        plt.figure()
        plt.bar(individual_df['Disease'], individual_df['Score'])

        # Titles and tags
        plt.title('PRS for ' + individual)
        plt.xlabel('Disease')
        plt.ylabel('Risk Score')

        # rotate tags
        plt.xticks(rotation=90)

        # Save graph
        plt.savefig(os.path.join(output_directory, f"{individual}_PRS.png"))

        plt.close()


