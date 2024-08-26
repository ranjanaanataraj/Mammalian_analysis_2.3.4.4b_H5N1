from Bio import SeqIO
import seaborn as sns
import pandas as pd
import re
import matplotlib.pyplot as plt

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
    # Open the parent FASTA file and the output file for writing
    with open(parent_fasta, "r") as parent_fh, open(output_fasta, "w") as output_fh:
        # Iterate over sequences in the parent FASTA file
        for record in SeqIO.parse(parent_fh, "fasta"):
            # Check if the header is in the header list
            if record.id in header_list:
                # Write the sequence to the output file
                SeqIO.write(record, output_fh, "fasta")


fasta_file = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/Hu_C_SL/fasta/msa/Hu_Ca_Sl_NS1_cs_msa.fasta"
df = fasta_to_dataframe(fasta_file)
print(df["Sequence"][0][75])

