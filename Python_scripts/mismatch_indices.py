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

def find_mismatch_indices(*sequences):
    lengths = [len(seq) for seq in sequences]
    if len(set(lengths)) != 1:
        raise ValueError("All sequences must be of equal length")

    mismatch_indices = []
    for i in range(lengths[0]):
        if len(set(seq[i] for seq in sequences)) != 1:
            mismatch_indices.append(i)

    return mismatch_indices

fasta_file = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/A_C_SL_M/fasta/A_C_SL_M_PB2_cs_msa.fasta"
df_HA = fasta_to_dataframe(fasta_file)

seq = df_HA["Sequence"].to_list()
avian_HA =seq[0]
cattle_HA = seq[1]
sea_lion_HA = seq[2]
fox_HA = seq[3]

mismatch_indices = find_mismatch_indices(avian_HA, cattle_HA,sea_lion_HA,fox_HA)

print("Indices of mismatched characters:", mismatch_indices)

for i in mismatch_indices:
  print("Avian :" +  avian_HA[i] + str(i))
  print("sea_lion :" + sea_lion_HA[i] + str(i))
  print("cattle :" + cattle_HA[i] + str(i))
  print("fox :" + fox_HA[i] + str(i))