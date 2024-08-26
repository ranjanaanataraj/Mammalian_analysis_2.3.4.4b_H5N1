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


fasta_file = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/Humans/H1N1/N1/Hu_H1N1_N1_cs.fasta"
df = fasta_to_dataframe(fasta_file)

res = 404
res_list = []
for i in df["Sequence"]:
	res_list.append(i[res])
	
print(res_list)

