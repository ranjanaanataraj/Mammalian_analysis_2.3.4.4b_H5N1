from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa

def calculate_residue_distance(pdb_file, chain_id, residue1_id, residue2_id):
    """
    Calculate the Euclidean distance between two residues in a PDB file.

    Parameters:
    pdb_file (str): Path to the PDB file.
    chain_id (str): The chain identifier.
    residue1_id (int): The residue number of the first residue.
    residue2_id (int): The residue number of the second residue.

    Returns:
    float: The distance between the two residues in angstroms, or None if the residues are not standard amino acids.
    """
    # Load and parse the PDB file
    pdb_parser = PDBParser()
    structure = pdb_parser.get_structure("protein", pdb_file)

    # Extract the residues using the correct format for residue keys
    chain = structure[0][chain_id]  # Model 0 (first model), specified chain
    try:
        residue1 = chain[(' ', residue1_id, ' ')]
        residue2 = chain[(' ', residue2_id, ' ')]
    except KeyError:
        print(f"Residue {residue1_id} or {residue2_id} not found in chain {chain_id}.")
        return None

    # Check if residues are amino acids and extract the alpha carbon (Cα) atoms
    if is_aa(residue1) and is_aa(residue2):
        ca1 = residue1['CA']  # Alpha carbon of residue 1
        ca2 = residue2['CA']  # Alpha carbon of residue 2

        # Compute the Euclidean distance using the `-` operator between atoms
        distance = ca1 - ca2
        return distance
    else:
        print(f"Residue {residue1_id} or {residue2_id} is not a standard amino acid.")
        return None

# Example usage
pdb_file = "/Users/ranjananataraj/Documents/IISc/4b_all_protein_analysis/structures/3ube.pdb"
chain_id = 'A'
residue1_id = [122,199,214] #mutations
residue2_id = [226,228] #classical_signatures 
output_res = []
output_score = []

for i in residue1_id:
    # Filter out None values in radii list
    radii = [distance for j in residue2_id if (distance := calculate_residue_distance(pdb_file, chain_id, i-1, j)) is not None]
    
    if radii and min(radii) <= 5:  # Ensure radii is not empty and check distance
        output_res.append(i)
        output_score.append(0.03)
    else:
        output_res.append(i)
        output_score.append(0.02)

print(output_res)
print(output_score)
