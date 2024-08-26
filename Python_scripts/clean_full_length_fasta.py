import os
from Bio import SeqIO
import pandas as pd
import re

def fasta_to_dataframe(fasta_file):
    headers = []
    sequences = []
    lengths = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        headers.append(record.id)
        sequences.append(str(record.seq))
        lengths.append(len(record))

    df = pd.DataFrame({"Header": headers, "Sequence": sequences, "Length": lengths})
    return df

def extract_sequences_by_headers(parent_fasta, header_list, output_fasta):
    with open(parent_fasta, "r") as parent_fh, open(output_fasta, "w") as output_fh:
        for record in SeqIO.parse(parent_fh, "fasta"):
            if record.id in header_list:
                SeqIO.write(record, output_fh, "fasta")

# Directory containing the FASTA files
directory = "/Users/ranjananataraj/Downloads/full_length/"

# Directory to save the cleaned files
output_directory = "/Users/ranjananataraj/Downloads/full_length/cleaned/"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".fasta"):
        fasta_file = os.path.join(directory, filename)
        
        # Process each FASTA file
        df = fasta_to_dataframe(fasta_file)
        character = "X"
        pattern = re.compile(f".*{re.escape(character)}.*")
        strings_with_character = [string for string in df["Sequence"] if pattern.match(string)]
        clean_seq_header = df["Header"][~df["Sequence"].isin(strings_with_character)].tolist()
        output_fasta = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_cleaned.fasta")
        
        # Extract sequences and save to output file
        extract_sequences_by_headers(fasta_file, clean_seq_header, output_fasta)
