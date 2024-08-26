import matplotlib.pyplot as put
import seaborn as sns
import pandas as pd
from Bio import SeqIO
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



fasta_file = "/Volumes/Recovery/IISc/4b_all_protein_analysis/Cattle/fasta/cleaned/PB2_cattle_raw_full_length_cleaned_pm_aligned.fasta"

df = fasta_to_dataframe(fasta_file)

mut = [57, 138, 361, 440, 477, 630, 675]
res = ["A","I","G","N","I","L","A"]

ls_57  = []
ls_138 = []
ls_361 = []
ls_440 = []
ls_447 = []
ls_630 = []
ls_675 = []

for i,j in zip(df["Header"], df["Sequence"]):
	if j[57] == "A":
		ls_57.append(i)
	if j[138] == "I":
		ls_138.append(i)
	if j[361] == "G":
		ls_361.append(i)
	if j[440] == "N":
		ls_440.append(i)
	if j[447] == "I":
		ls_447.append(i)
	if j[630] == "L":
		ls_630.append(i)
	if j[675] == "A":
		ls_675.append(i)


ls = [ls_57,ls_138,ls_361,ls_440,ls_447,ls_630,ls_675]
for i in ls:
	print(Counter(i))
		
	