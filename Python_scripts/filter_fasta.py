from Bio import SeqIO

# Input and output file paths
input_fasta_file = "/Users/ranjananataraj/Downloads/ALL_protein/PB/PB2_cattle_raw.fasta"
output_fasta_file = "/Users/ranjananataraj/Desktop/PA_1_cattle_raw.fasta"

# Function to filter records based on header description
def filter_records(records):
    filtered_records = []
    for record in records:
        if "Polymerase acidic protein" in record.description:
            filtered_records.append(record)
    return filtered_records

# Read the input FASTA file
records = list(SeqIO.parse(input_fasta_file, "fasta"))

# Filter records based on header description
filtered_records = filter_records(records)

# Write filtered records to the output FASTA file
with open(output_fasta_file, "w") as output_handle:
    SeqIO.write(filtered_records, output_handle, "fasta")
