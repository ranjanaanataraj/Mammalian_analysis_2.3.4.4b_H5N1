import os
import argparse
import logging
from Bio import SeqIO
import pandas as pd

def filter_full_length_sequences(fasta_file, min_length):
    """
    Filters sequences to retain only those that meet a minimum length requirement.
    Args:
        fasta_file (str): Path to the input FASTA file.
        min_length (int): Minimum length threshold.
    Returns:
        list: List of SeqRecord objects meeting the length requirement.
    """
    return [record for record in SeqIO.parse(fasta_file, "fasta") if len(record) >= min_length]

def remove_x_containing_sequences(sequences):
    """
    Removes sequences containing 'X' from a list of SeqRecord objects.
    Args:
        sequences (list): List of SeqRecord objects.
    Returns:
        list: Filtered list of SeqRecord objects.
    """
    return [record for record in sequences if "X" not in str(record.seq)]

def process_fasta(input_fasta, output_fasta, min_length):
    """
    Filters a FASTA file to remove short sequences and those containing 'X'.
    Args:
        input_fasta (str): Path to input FASTA file.
        output_fasta (str): Path to output cleaned FASTA file.
        min_length (int): Minimum length threshold.
    """
    sequences = filter_full_length_sequences(input_fasta, min_length)
    cleaned_sequences = remove_x_containing_sequences(sequences)
    
    SeqIO.write(cleaned_sequences, output_fasta, "fasta")
    logging.info(f"Saved cleaned FASTA to {output_fasta} with {len(cleaned_sequences)} sequences.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter and clean FASTA sequences.")
    parser.add_argument("input_fasta", type=str, help="Path to input FASTA file.")
    parser.add_argument("output_fasta", type=str, help="Path to output FASTA file.")
    parser.add_argument("--min_length", type=int, default=500, help="Minimum sequence length (default: 500).")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    process_fasta(args.input_fasta, args.output_fasta, args.min_length)
