# **IAV Human Adaptation Analysis**

This repository contains the computational pipeline used to replicate key analyses and visualizations from our study,  
**"Decoding Non-Human Mammalian Adaptive Signatures of 2.3.4.4b H5N1 to Assess Its Human Adaptive Potential"**, available on bioRxiv [**here**](https://www.biorxiv.org/content/10.1101/2024.08.26.609722v1).  

The study investigates the molecular evolution and mammalian adaptation potential of the **2.3.4.4b H5N1 influenza A virus (IAV)** by integrating:
- **Comparative sequence analysis**  
- **Evolutionary selection pressure modeling**  
- **Structural and functional insights**  

Our systematic approach aims to characterize host-specific mutations and assess their role in mammalian adaptation, providing a **quantitative framework** for evaluating the pandemic potential of avian influenza strains.

---

## **Methodology Overview**
1. **Curating full-length viral protein sequences** and removing incomplete or ambiguous entries.  
2. **Computing host-specific consensus sequences** to identify residues that diverge between avian and mammalian isolates.  
3. **Quantifying selective pressures** (dN/dS) at these sites using **codeml** branch-site models, inferring evolutionary constraints.  
4. **Characterizing residue-specific frequency distributions** to assess fixation trends in avian vs. mammalian hosts.  
5. **Visualizing adaptation bottlenecks** using heatmaps and radar plots to highlight key viral proteins (HA, NA, PB2, PB1, PA, NS1) and residues yet to be acquired for human adaptation.  

This repository provides **fully reproducible scripts** for sequence processing, mismatch residue identification, evolutionary analysis, and figure generation.

---

## **Repository Structure**
```
📂 IAV_Human_Adaptation_Analysis
│── 📂 data/              # Example input files (FASTA, CSV, codeml config/output)
│── 📂 scripts/           # Processing and visualization scripts
│── 📂 results/           # Generated plots and processed data
│── 📂 codeml/            # PAML codeml configuration and results
│── 📜 README.md          # Project overview and usage instructions
│── 📜 requirements.txt   # Dependencies for easy setup
```

---

## **Installation**
To set up the repository and install dependencies:
```bash
git clone https://github.com/yourusername/IAV_Human_Adaptation_Analysis.git
cd IAV_Human_Adaptation_Analysis
pip install -r requirements.txt
```

---

## **Key Scripts & Their Functions**
### `scripts/radar_data_mammal.py`
Processes **FASTA sequences** and a **mutation signature CSV file** to:  
1. Extract IAV protein sequences
2.  Identify host-specific mutation sites
3.  Count acquired vs. missing mutations
4.  Save output as `mutation_data.csv`  

**Run it with:**
```bash
python scripts/radar_data_mammal.py data/protein_sequences.fasta data/mutation_signatures.csv results/mutation_data.csv
```

### `scripts/radar_mammal.py`
Reads `mutation_data.csv` and generates a **radar plot** highlighting unacquired mutations across viral proteins.  
1. Assigns unique angles per protein  
2. Plots mutation bottlenecks in a **polar coordinate system**  
3. Saves as `radar_plot.png`  

**Run it with:**
```bash
python scripts/radar_mammal.py results/mutation_data.csv results/radar_plot.png
```

### `scripts/plot_heatmap.py`
Creates a **heatmap** of mutation frequencies, highlighting **highly mutable residues** across viral proteins.  
1. Organizes mutations into a **matrix**
2. Uses Seaborn for visualization  
3. Saves the heatmap as `heatmap.png`  

**Run it with:**
```bash
python scripts/plot_heatmap.py results/mutation_data.csv results/heatmap.png
```

---

## **Codeml Selection Analysis (`codeml/`)**
This directory contains **PAML codeml configuration files** for selection pressure analysis.  

### **Codeml Models & Rationale**
| **Model**                 | **Objective** |
|---------------------------|--------------|
| `codeml_model0.ctl`       | **Baseline dN/dS ratio** assuming a single selection pressure across all sites. |
| `codeml_branch_site.ctl`  | **Branch-site model** to detect **positive selection** in host-specific lineages. |
| `codeml_ancestor.ctl`     | **Ancestral reconstruction** of mutations to infer evolutionary trajectories. |

These analyses allow us to **test whether residues under selection correspond to those required for mammalian adaptation**—providing **functional evidence** for their role in host switching and virulence.

### **Running Codeml**
To execute each model:
```bash
codeml codeml/codeml_model0.ctl
codeml codeml/codeml_branch_site.ctl
codeml codeml_ancestor.ctl
```
Outputs will be stored as:
```
📜 results_model0.txt       # Baseline dN/dS results
📜 results_branch_site.txt  # Positively selected sites
📜 results_ancestor.txt     # Reconstructed ancestral sequences
```

---

## **Outputs**
| **File**                    | **Description** |
|-----------------------------|----------------|
| `mutation_data.csv`         | Mutation counts per protein |
| `radar_plot.png`            | Radar chart of missing mutations |
| `heatmap.png`               | Heatmap of mutation frequencies |
| `results_model0.txt`        | Global dN/dS selection pressure |
| `results_branch_site.txt`   | Host-specific positively selected sites |
| `results_ancestor.txt`      | Evolutionary history of key residues |

---

## **Why This Matters**
- **Mismatch residues** identified in `mismatch_indices.py` are tested for **selection pressure** to confirm functional importance.  
- **Branch-site models** detect **host-specific adaptation**, informing whether certain residues **facilitate mammalian tropism**.  
- **Ancestral reconstruction** clarifies evolutionary trajectories, distinguishing **adaptive vs. neutral mutations**.  
- **Visualizations (heatmaps & radar plots)** quantify adaptation bottlenecks, providing **a clear framework** for assessing the pandemic potential of 2.3.4.4b H5N1.

---

## **License**
MIT License

## **Contributors**
👩‍🔬 **Ranjana Nataraj** (@ranjanaanataraj)
