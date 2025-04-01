# IAV Human Adaptation Analysis

This repository contains the computational pipeline used to replicate key analyses and visualizations from our study, **"Decoding non-human mammalian adaptive signatures of 2.3.4.4b H5N1 to assess its human adaptive potential"**, available on bioRxiv (https://www.biorxiv.org/content/10.1101/2024.08.26.609722v1). The study investigates the molecular evolution and mammalian adaptation potential of the 2.3.4.4b H5N1 influenza A virus (IAV) by integrating comparative sequence analysis, evolutionary selection pressure modeling, and structural insights.
Our approach systematically:

Curates full-length viral protein sequences to exclude incomplete or ambiguous entries.

Computes consensus sequences for avian and mammalian isolates and identifies amino acid residues exhibiting host-specific divergence.

Quantifies the selective pressures acting on these residues using codeml (dN/dS) models, including branch-site and ancestral reconstruction frameworks, to infer potential functional significance.

Characterizes residue-specific frequency distributions across avian and mammalian isolates to assess fixation trends.

Generates heatmaps and radar plots to visualize host adaptation bottlenecks across key viral proteins (HA, NA, PB2, PB1, PA, NS1), identifying residues yet to be acquired for optimal mammalian adaptation.

This repository provides fully reproducible scripts for sequence processing, mismatch residue identification, evolutionary analysis, and figure generation, enabling robust exploration of 2.3.4.4b H5N1 adaptation dynamics.



1. **Extracting full-length sequences** from a given FASTA file.
2. **Identifying mutations** that differentiate avian and mammalian consensus sequences.
3. **Counting mutation frequencies** at key positions.
4. **Calculating dN/dS ratios** using `codeml` to infer selection pressure.
5. **Visualizing results** using heatmaps and radar plots.

## Repository Structure
```
📂 IAV_Human_Adaptation_Analysis
│── 📂 data/              # Example input files (FASTA, CSV, codeml config/output)
│── 📂 scripts/           # Processing and visualization scripts
│── 📂 results/           # Generated plots and processed data
│── 📂 codeml/            # Example PAML codeml input/output files
│── 📜 README.md          # Project overview and usage instructions
│── 📜 requirements.txt   # Dependencies for easy setup
```

## Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/IAV_Human_Adaptation_Analysis.git
cd IAV_Human_Adaptation_Analysis
pip install -r requirements.txt
```

## Script Descriptions

### `scripts/radar_data_mammal.py`
This script processes an input **FASTA file** of IAV protein sequences and a **CSV file** containing known human-adaptable mutation sites. It:
1. Extracts sequence data from the FASTA file.
2. Reads the CSV file containing human-adaptable mutations.
3. Identifies positions where avian and human residues differ.
4. Counts how many mutations have been acquired vs. still missing.
5. Saves the mutation count as `mutation_data.csv`.

**Run the script:**
```bash
python scripts/radar_data_mammal.py data/protein_sequences.fasta data/mutation_signatures.csv results/mutation_data.csv
```

### `scripts/radar_mammal.py`
This script reads `mutation_data.csv` and generates a **radar plot** to visualize the number of mutations still required for human adaptation across different IAV proteins. It:
1. Reads the mutation count data.
2. Assigns unique angles to each protein for the radar chart.
3. Plots the **remaining mutations** on a polar coordinate system.
4. Saves the figure as `radar_plot.png`.

**Run the script:**
```bash
python scripts/radar_mammal.py results/mutation_data.csv results/radar_plot.png
```

### `scripts/plot_heatmap.py`
This script generates a **heatmap** of mutation frequencies at key positions, allowing visualization of the most frequently mutated residues across proteins. It:
1. Reads `mutation_data.csv`.
2. Organizes mutations into a **matrix format**.
3. Plots a heatmap using Seaborn.
4. Saves the heatmap as `heatmap.png`.

**Run the script:**
```bash
python scripts/plot_heatmap.py results/mutation_data.csv results/heatmap.png
```

### `codeml/`
This folder contains **PAML codeml configuration files** used to calculate dN/dS ratios and infer selection pressure on IAV proteins. The logic is as follows:

1. **`codeml_model0.ctl`** – Runs a **basic dN/dS (ω) calculation** assuming a **single ω ratio across all sites**, giving an overall measure of selection.
2. **`codeml_branch_site.ctl`** – Uses a **branch-site model** to detect **positively selected residues** specific to mammalian or avian hosts.
3. **`codeml_ancestor.ctl`** – Reconstructs **ancestral sequences**, allowing comparison of evolutionary changes and identifying sites under selection pressure.

### **Why We Did This?**

- The mismatch residues identified in `mismatch_indices.py` are tested for **positive selection** to confirm if they are functionally important.
- The **branch-site model** helps determine if any **host-specific selection** is occurring, which could indicate adaptation to mammalian hosts.
- Ancestral reconstruction allows us to **trace the evolutionary history** of these sites and understand whether mutations were driven by natural selection.
- If residues under selection pressure correspond to those required for mammalian adaptation, this provides evidence that they play a role in **host switching and virulence**.

### **How to Run `codeml`?**
To run the selection analysis:
```bash
codeml codeml/codeml_model0.ctl
codeml codeml/codeml_branch_site.ctl
codeml codeml/codeml_ancestor.ctl
```
Each will generate an output file (e.g., `results_model0.txt`, `results_branch_site.txt`, `results_ancestor.txt`).

## Output
- `mutation_data.csv`: Processed mutation counts per protein.
- `radar_plot.png`: Radar chart showing missing mutations.
- `heatmap.png`: Heatmap of mutation frequencies.
- `codeml/results_model0.txt`: dN/dS values for overall selection pressure.
- `codeml/results_branch_site.txt`: Positively selected sites specific to avian or mammalian hosts.
- `codeml/results_ancestor.txt`: Ancestral state reconstruction of key residues.

## License
MIT License

## Contributors
- Ranjana Nataraj (@ranjanaanataraj)

