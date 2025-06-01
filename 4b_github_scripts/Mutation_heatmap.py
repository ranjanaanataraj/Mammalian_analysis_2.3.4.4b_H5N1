import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(csv_file, output_png):
    """Generates a heatmap from a mutation frequency CSV file."""
    df = pd.read_csv(csv_file, index_col=0)
    plt.figure(figsize=(12, 6))
    sns.heatmap(df, annot=True, cmap="coolwarm", fmt=".0f", linewidths=0.5)
    plt.xlabel("Amino Acids")
    plt.ylabel("Mismatch Positions")
    plt.title("Mutation Frequency Heatmap")
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a heatmap from mutation frequency data.")
    parser.add_argument("csv_file", type=str, help="Path to mutation frequency CSV file.")
    parser.add_argument("output_png", type=str, help="Path to save heatmap image.")
    args = parser.parse_args()
    
    plot_heatmap(args.csv_file, args.output_png)
