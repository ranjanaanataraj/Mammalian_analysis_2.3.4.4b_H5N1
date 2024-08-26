import re
def filter_headers_with_host(fasta_file,host_regex):
    mallard_sequences = {}
    with open(fasta_file, 'r') as file:
        header = ''
        for line in file:
            if line.startswith('>'):
                header = line.strip()
                if re.search(host_regex, header, flags=re.IGNORECASE):
                    mallard_sequences[header] = ''
            else:
                if header in mallard_sequences:
                    mallard_sequences[header] += line.strip()
    return mallard_sequences

# Example usage:
fasta_file = '/Users/ranjananataraj/Downloads/all_mammals_4b_all_proteins.fasta'
host_regex = r'goat'
host_sequences = filter_headers_with_host(fasta_file, host_regex)

# Print the number of sequences found
print("Number of sequences found:", len(host_sequences))

# Writing the filtered sequences to a new fasta file
output_file = '/Users/ranjananataraj/Downloads/goat_all_proteins.fasta'
with open(output_file, 'w') as output:
    for header, sequence in host_sequences.items():
        output.write(header + '\n')
        output.write(sequence + '\n')