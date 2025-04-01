# IAV Human Adaptation Analysis

This repository contains scripts to analyze mutations in influenza A virus (IAV) proteins to assess how many mutations are required for human adaptation. The workflow involves:

1. **Extracting full-length sequences** from a given FASTA file.
2. **Identifying mutations** that differentiate avian and mammalian consensus sequences.
3. **Counting mutation frequencies** at key positions.
4. **Visualizing results** using heatmaps and radar plots.

## Repository Structure
```
📂 IAV_Human_Adaptation_Analysis
│── 📂 data/              # Example input files (FASTA, CSV)
│── 📂 scripts/           # Processing and visualization scripts
│── 📂 results/           # Generated plots and processed data
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

## Output
- `mutation_data.csv`: Processed mutation counts per protein.
- `radar_plot.png`: Radar chart showing missing mutations.
- `heatmap.png`: Heatmap of mutation frequencies.

## License
MIT License

## Contributors
- Ranjana Natara (@ranjanaanataraj)

