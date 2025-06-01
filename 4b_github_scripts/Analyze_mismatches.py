import argparse
from Bio import SeqIO
import pandas as pd
from collections import Counter
import logging

def fasta_to_dataframe(fasta_file):
    """Loads a FASTA file into a DataFrame."""
    headers, sequences = [], []
    for record in SeqIO.parse(fasta_file, "fasta"):
        headers.append(record.id)
        sequences.append(str(record.seq))
    return pd.DataFrame({"Header": headers, "Sequence": sequences})

def find_mismatch_indices(seq1, seq2):
    """Finds mismatch positions between two aligned sequences."""
    return [i for i in range(len(seq1)) if seq1[i] != seq2[i]]

def count_mutations(df, positions):
    """Counts the frequency of residues at mismatch positions."""
    counts = {pos: Counter(df["Sequence"].str[pos]) for pos in positions}
    return pd.DataFrame.from_dict(counts, orient="index").fillna(0)

def main(avian_fasta, mammalian_fasta, output_csv):
    """Main function to analyze mismatches and save mutation counts."""
    avian_df = fasta_to_dataframe(avian_fasta)
    mammalian_df = fasta_to_dataframe(mammalian_fasta)
    
    avian_consensus = avian_df["Sequence"].mode()[0]
    mammalian_consensus = mammalian_df["Sequence"].mode()[0]
    
    mismatch_positions = find_mismatch_indices(avian_consensus, mammalian_consensus)
    mutation_counts = count_mutations(avian_df, mismatch_positions)
    
    mutation_counts.to_csv(output_csv)
    logging.info(f"Saved mutation frequency data to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze sequence mismatches and mutation frequencies.")
    parser.add_argument("avian_fasta", type=str, help="Path to avian consensus FASTA.")
    parser.add_argument("mammalian_fasta", type=str, help="Path to mammalian consensus FASTA.")
    parser.add_argument("output_csv", type=str, help="Path to save mutation frequency CSV.")
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main(args.avian_fasta, args.mammalian_fasta, args.output_csv)
