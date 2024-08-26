import pandas as pd

df = pd.read_csv("/Users/ranjananataraj/Documents/iiSc/4b_all_protein_analysis/other mammals/skunk/skunk_annot.csv")

ls = ["Adaptation" if 
      (df["skunk"][i] == df["Hu_H1N1"][i]) or (df["skunk"][i] == df["Hu_H3N2"][i])
      else "Barrier" if ((df["Avian"][i] == df["Hu_H1N1"][i]) or (df["Avian"][i] == df["Hu_H3N2"][i])) and 
      ((df["skunk"][i] != df["Hu_H1N1"][i]) and (df["skunk"][i] != df["Hu_H3N2"][i])) 
      else None 
      for i in range(len(df["Position"]))]


df["feature"] = ls

barrier_score = [-0.02 if df["feature"][i] == "Barrier" else 0 for i in range(0,len(df["Position"]))]


df["score"] = barrier_score

df.to_csv("/Users/ranjananataraj/Desktop/skunk_4b_Hu_data_wb.csv")

