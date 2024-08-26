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


df_hu_sign = pd.read_csv("/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/cs_heatmap/classical_signatures_with_ref.csv")

df_hu_sign.set_index("Gene",inplace = True)

HA_list = df_hu_sign.loc["PB2"]["Position"].to_list()
HA_res = df_hu_sign.loc["PB2"]["Human"].to_list()
Av_res = df_hu_sign.loc["PB2"]["Avian"].to_list()

df_protein = fasta_to_dataframe("/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/cs_heatmap/fasta/fox_PB2_msa.fasta")

count = []
hits = []
mutations_acquired = []

for i,j,m in zip(HA_list, HA_res, Av_res):
	for k,l in zip(df_protein["Sequence"].to_list(), df_protein["Header"].to_list()):
		if k[i-1] == j:
			count.append(l)
			hits.append(i)
			mutations_acquired.append(str(m) + str(i)+ str(j))

print("Count: " + str(len(list(set(count)))))

print("No:of human mutations acquired: " + str(len(list(set(hits)))))
for i in list(set(mutations_acquired)):
	print("Human mutations acquired: " + i)
print("No:of human mutations yet to acquire: " + str(len(HA_list) - len(list(set(hits)))))