def filter_fasta_by_protein_type(input_file, output_file, protein_type):
    # Open input file for reading
    with open(input_file, 'r') as f_in:
        # Open output file for writing
        with open(output_file, 'w') as f_out:
            header = ''
            sequence = ''
            # Iterate through each line in the input file
            for line in f_in:
                if line.startswith('>'):
                    # If a header line is encountered
                    # Write the previous sequence if it matches the protein type
                    if sequence and protein_type in header:
                        f_out.write(header + '\n')
                        f_out.write(sequence + '\n')
                    # Update header for the new sequence
                    header = line.strip()
                    sequence = ''
                else:
                    # Append sequence lines
                    sequence += line.strip()
            # Write the last sequence if it matches the protein type
            if sequence and protein_type in header:
                f_out.write(header + '\n')
                f_out.write(sequence + '\n')

# Example usage:
input_file = "/Users/ranjananataraj/Downloads/goat_all_proteins.fasta"

output_file = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/other mammals/goat/goat_NS1_proteins.fasta"
protein_type = '|NS1|'
filter_fasta_by_protein_type(input_file, output_file, protein_type)
