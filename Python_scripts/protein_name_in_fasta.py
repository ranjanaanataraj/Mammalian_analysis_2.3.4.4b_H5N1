from Bio import SeqIO
import pandas as pd
import re
from collections import Counter

def fasta_header(fasta_file):
    headers = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        headers.append(record.description)

    return headers

def extract_protein_name(header):
    match = re.match(r'^.*_(.+)', header)
    if match:
        print("Match found:", match.group(0))  # Print the entire match
        print("Captured group:", match.group(1)[6:])  # Print the captured group
        return match.group(1)[6:]
    else:
        print("No match found for header:", header)
        return None

fasta_file = "/Users/ranjananataraj/Downloads/ALL_protein/PB/PB2_cattle_raw.fasta"
fasta_headers = fasta_header(fasta_file)
# Extract protein names
protein_names = [extract_protein_name(header) for header in fasta_headers]

print(Counter(protein_names))
