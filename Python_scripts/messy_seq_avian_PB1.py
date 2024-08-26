from Bio import SeqIO
import pandas as pd
import re

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


def extract_sequences_by_headers(parent_fasta, header_list, output_fasta):
    # Open the parent FASTA file and the output file for writing
    with open(parent_fasta, "r") as parent_fh, open(output_fasta, "w") as output_fh:
        # Iterate over sequences in the parent FASTA file
        for record in SeqIO.parse(parent_fh, "fasta"):
            # Check if the header is in the header list
            if record.id in header_list:
                # Write the sequence to the output file
                SeqIO.write(record, output_fh, "fasta")




def find_strings_without_regex(strings, regex_pattern):
    # Compile the regex pattern
    regex = re.compile(regex_pattern)
    
    # List to store strings that don't match the regex pattern
    strings_without_regex = []
    
    # Iterate over each string in the input list
    for string in strings:
        # If the regex pattern doesn't match the string, add it to the list
        if not regex.search(string):
            strings_without_regex.append(string)
    
    return strings_without_regex


regex_pattern = r"H.{5}R"  # Specific regex pattern: H followed by 5 characters and then R



fasta_file = "/Users/ranjananataraj/Desktop/Avian_PB1_full_length.fasta"

df = fasta_to_dataframe(fasta_file)
strings = df["Sequence"].to_list()

strings_without_regex = find_strings_without_regex(strings, regex_pattern)


for i in strings_without_regex:
	print(df["Header"] [df["Sequence"]== i])














