from Bio import SeqIO
import seaborn as sns
import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

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


fasta_file = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/cs_heatmap/fasta/cattle_PA_msa.fasta"

n = 614
res = "K"
df = fasta_to_dataframe(fasta_file)

score = [1 if i[n] == res else 0 for i in df["Sequence"]]

residue = [i[n] for i in df["Sequence"]]
print(Counter(residue))
print(Counter(score))