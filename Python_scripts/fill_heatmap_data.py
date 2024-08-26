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



fasta_file_NS1 = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/other mammals/fasta/other_mammals_NS1.fasta"
df_om_NS1 = fasta_to_dataframe(fasta_file_NS1)

fasta_file_NP = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/other mammals/fasta/other_mammals_NP.fasta"
df_om_NP = fasta_to_dataframe(fasta_file_NP)

fasta_file_PA = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/other mammals/fasta/other_mammals_PA.fasta"
df_om_PA = fasta_to_dataframe(fasta_file_PA)

fasta_file_PB1 = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/other mammals/fasta/other_mammals_PB1.fasta"
df_om_PB1 = fasta_to_dataframe(fasta_file_PB1)

fasta_file_PB2 = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/other mammals/fasta/other_mammals_PB2.fasta"
df_om_PB2 = fasta_to_dataframe(fasta_file_PB2)




df = pd.read_csv("/Users/ranjananataraj/Desktop/mutation_data_other_mammals.csv")
df.set_index("Protein",inplace = True)

NS1_ls = (df["Position"].loc["NS1"]).to_list()
NS1_res = []
for i in df_om_NS1["Sequence"]:
	for j in NS1_ls:
		NS1_res.append(i[j-1])


NP_ls = (df["Position"].loc["NP"]).to_list()
NP_res = []
for i in df_om_NP["Sequence"]:
	for j in NP_ls:
		NP_res.append(i[j-1])

PA_ls = (df["Position"].loc["PA"]).to_list()
PA_res = []
for i in df_om_PA["Sequence"]:
	for j in PA_ls:
		PA_res.append(i[j-1])

PB1_ls = (df["Position"].loc["PB1"]).to_list()
PB1_res = []
for i in df_om_PB1["Sequence"]:
	for j in PB1_ls:
		PB1_res.append(i[j-1])

PB2_ls = (df["Position"].loc["PB2"]).to_list()
PB2_res = []
for i in df_om_PB2["Sequence"]:
	for j in PB2_ls:
		PB2_res.append(i[j-1])

print(len(NS1_ls))
print(len(NP_ls))
print(len(PA_ls))
print(len(PB1_ls))
print(len(PB2_ls))


df["bear"].loc["NS1"] = NS1_res[0:11]
df["dolphin"].loc["NS1"] = NS1_res[11:22]
df["feline"].loc["NS1"] = NS1_res[22:33]
df["goat"].loc["NS1"] = NS1_res[33:44]
df["raccoon"].loc["NS1"] = NS1_res[44:55]
df["skunk"].loc["NS1"] = NS1_res[55:66]

df["bear"].loc["NP"] = NP_res[0:6]
df["dolphin"].loc["NP"] = NP_res[6:12]
df["feline"].loc["NP"] = NP_res[12:18]
df["goat"].loc["NP"] = NP_res[18:24]
df["raccoon"].loc["NP"] = NP_res[24:30]
df["skunk"].loc["NP"] = NP_res[30:36]


df["bear"].loc["PA"] = PA_res[0:10]
df["dolphin"].loc["PA"] = PA_res[10:20]
df["feline"].loc["PA"] = PA_res[20:30]
df["goat"].loc["PA"] = PA_res[30:40]
df["raccoon"].loc["PA"] = PA_res[40:50]
df["skunk"].loc["PA"] = PA_res[50:60]

df["bear"].loc["PB1"] = PB1_res[0:16]
df["dolphin"].loc["PB1"] = PB1_res[16:32]
df["feline"].loc["PB1"] = PB1_res[32:48]
df["goat"].loc["PB1"] = PB1_res[48:64]
df["raccoon"].loc["PB1"] = PB1_res[64:80]
df["skunk"].loc["PB1"] = PB1_res[80:96]

df["bear"].loc["PB2"] = PB2_res[0:16]
df["dolphin"].loc["PB2"] = PB2_res[16:32]
df["feline"].loc["PB2"] = PB2_res[32:48]
df["goat"].loc["PB2"] = PB2_res[48:64]
df["raccoon"].loc["PB2"] = PB2_res[64:80]
df["skunk"].loc["PB2"] = PB2_res[80:96]


#print(len(HA_res))
print(df)
df.to_csv("/Users/ranjananataraj/Desktop/other_mammals.csv")
