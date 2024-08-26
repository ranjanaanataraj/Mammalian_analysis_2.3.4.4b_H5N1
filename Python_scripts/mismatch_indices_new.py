from Bio import SeqIO
import seaborn as sns
import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

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

fasta_file = "/media/aka/OS/Users/alekh/Desktop/Ranjana/Hu_AV_SL_C_msa.fasta"
df_HA = fasta_to_dataframe(fasta_file)

seq = df_HA["Sequence"].to_list()

hu_HA =seq[0]
avian_HA = seq[1]
cattle_HA = seq[2]
sea_lion_HA = seq[3]

j = set(find_mismatch_indices(avian_HA, cattle_HA, 
sea_lion_HA))

k = set(find_mismatch_indices(hu_HA,avian_HA, cattle_HA, 
sea_lion_HA))

l = set(find_mismatch_indices(hu_HA, cattle_HA, 
sea_lion_HA))

j_diff_k = j - l
k_diff_j = l - j
intersection_sup = j&l
intersection = []
diff_res = []
for i in intersection_sup:
	if (hu_HA[i] == sea_lion_HA[i]) & (hu_HA[i] != avian_HA[i]):
		intersection.append(i)
	elif hu_HA[i] != sea_lion_HA[i]  :
		diff_res.append(i)
		


		
k_diff_j_sorted = list(k_diff_j)
k_diff_j_sorted.sort()
j_diff_k_sorted = list(j_diff_k)
j_diff_k_updated = j_diff_k_sorted + diff_res

j_diff_k_updated_set = set(j_diff_k_updated)
j_diff_k_updated.sort()
intersection.sort()
print(j_diff_k_updated)
#print("Classical that have been  acquired by 4b:", intersection)

for i in j_diff_k_updated:
  #print("Avian :" +  avian_HA[i] + str(i))
  print("sea_lion :" + sea_lion_HA[i] + str(i))
  #print("cattle :" + cattle_HA[i] + str(i))
  print("human :" + hu_HA[i] + str(i))


j_diff_k_text_cattle = ["A58T", "I109V", "I139V", "R340K", "G362E", "N441D", "V478I", "I495V", "Q591R", "L631M", "I648V","A675T"]



j_diff_k_text_sl = ["V463I", "M464L", "I478V", "K591R", "V616I", "D701N"]

k_diff_j_text = ["K54R", "E65D", "I147T", "T184A", "S225G", "T271A", "I292V", "M315I", "P453S", "T559I", "A588T", "G590S", "M645L", "A684S"]

intersection_text_sl = ["340K"]


fig,ax = plt.subplots(figsize = (8,6))
venn_diagram = venn2(subsets=(len(j_diff_k_updated_set),len(k_diff_j),len(intersection)),set_labels = ('',''),
set_colors = ('magenta', 'pink'), alpha = 0.8)

venn_diagram.get_patch_by_id('10').set_edgecolor('grey')
venn_diagram.get_patch_by_id('10').set_linewidth(1.45)
venn_diagram.get_patch_by_id('01').set_edgecolor('grey')
venn_diagram.get_patch_by_id('01').set_linewidth(1.45)
venn_diagram.get_patch_by_id('11').set_edgecolor('grey')
venn_diagram.get_patch_by_id('11').set_linewidth(1.45)

for text in venn_diagram.set_labels:
	text.set_fontsize(12)
	text.set_fontweight("bold")
	
venn_diagram.get_label_by_id('10').set_text('\n'.join(map(str,j_diff_k_text_sl)))
venn_diagram.get_label_by_id('10').set_fontweight("bold")
venn_diagram.get_label_by_id('10').set_fontsize(10)

venn_diagram.get_label_by_id('01').set_text('\n'.join(map(str,k_diff_j_text)))
venn_diagram.get_label_by_id('01').set_fontweight("bold")
venn_diagram.get_label_by_id('01').set_fontsize(10)

venn_diagram.get_label_by_id('11').set_text('\n'.join(map(str,intersection_text_sl)))
venn_diagram.get_label_by_id('11').set_fontweight("bold")
venn_diagram.get_label_by_id('11').set_fontsize(11)


plt.savefig("/media/aka/OS/Users/alekh/Desktop/Ranjana/venn_sl.pdf")
