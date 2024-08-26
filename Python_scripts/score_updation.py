import pandas as pd

df = pd.read_csv("/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/score_plot/cattle_4b_Hu_data_wb.csv")

score_new = [
    0.04 if i == 1 else 
    0.03 if i == 0.5 else 
    0.02 if i == 0.25 else 
    -0.02 if i == -0.25 
    else None  # or some other default value
    for i in df["score"]
]

df["score_new"] = score_new

#df.to_csv("/Users/ranjananataraj/Desktop/cattle_4b_Hu_data_wb_updated.csv")
print(df)

df.set_index("Protein",inplace = True)

for i in ["NP","NS1","PA","PB1","PB2"]:
	print(i +" "+ str(sum(df["score_new"].loc[i])))