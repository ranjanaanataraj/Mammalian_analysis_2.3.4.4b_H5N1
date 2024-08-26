import os
from Bio import SeqIO
import pandas as pd

def fasta_to_dataframe(fasta_file):
    headers = []
    sequences = []
    lengths = []

    try:
        for record in SeqIO.parse(fasta_file, "fasta"):
            headers.append(record.id)
            sequences.append(str(record.seq))
            lengths.append(len(record))
    except Exception as e:
        print(f"Error reading {fasta_file}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if there's an error

    df = pd.DataFrame({"Header": headers, "Sequence": sequences, "Length": lengths})
    return df

def extract_sequences_by_headers(parent_fasta, header_list, output_fasta):
    with open(parent_fasta, "r") as parent_fh, open(output_fasta, "w") as output_fh:
        for record in SeqIO.parse(parent_fh, "fasta"):
            if record.id in header_list:
                SeqIO.write(record, output_fh, "fasta")

# Directory containing the FASTA files
directory = "/Users/ranjananataraj/Downloads"
# Directory to save the output files
output_directory = "/Users/ranjananataraj/Downloads/full_length"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".fasta"):
        fasta_file = os.path.join(directory, filename)
        
        # Process each FASTA file
        df = fasta_to_dataframe(fasta_file)
        
        if df.empty:
            print(f"Skipping {filename} due to empty or invalid FASTA file.")
            continue
        
        try:
            value_counts = df["Length"].value_counts()
            print(value_counts)
            index_of_max_value = value_counts.idxmax()
            full_length_seq_header = df["Header"][df["Length"] == int(index_of_max_value)].tolist()
            output_fasta = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_full_length.fasta")
            
            # Extract sequences and save to output file
            extract_sequences_by_headers(fasta_file, full_length_seq_header, output_fasta)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
