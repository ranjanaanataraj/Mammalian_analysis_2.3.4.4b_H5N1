import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_radar_chart(csv_file, output_image):
    """Generates a radar plot of missing mutations for IAV adaptation."""
    df = pd.read_csv(csv_file)
    
    unique_proteins = df["Protein"].unique()
    num_proteins = len(unique_proteins)
    angles = np.linspace(0, 2 * np.pi, num_proteins, endpoint=False)
    
    protein_to_angle = {protein: angle for protein, angle in zip(unique_proteins, angles)}
    theta = df["Protein"].map(protein_to_angle)
    r = df["Remaining"]
    
    plt.figure(figsize=(10, 8))
    ax = plt.subplot(111, projection='polar')
    ax.scatter(theta, r, c="red", alpha=0.75)
    ax.set_xticks(angles)
    ax.set_xticklabels(unique_proteins, fontsize=12)
    
    plt.title("Missing Human-Adaptable Mutations in IAV Proteins", fontsize=14)
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a radar plot of missing IAV mutations.")
    parser.add_argument("csv_file", type=str, help="Path to processed mutation data CSV.")
    parser.add_argument("output_image", type=str, help="Path to save radar plot image.")
    args = parser.parse_args()
    
    plot_radar_chart(args.csv_file, args.output_image)
