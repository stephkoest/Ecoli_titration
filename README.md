# DnaA Motif Detection and Motif Shuffling

![License](https://img.shields.io/github/license/stephkoest/Ecoli_titration)
![Version](https://img.shields.io/badge/version-1.0-blue)

## Overview

This repository contains Python scripts developed as part of our study on **DnaA titration and its regulatory role in *Escherichia coli* replication initiation**. The scripts allow for:
1. **Detection of DnaA box motifs** on circular bacterial genomes.
2. **Shuffling of DnaA box motifs** to generate control datasets for statistical analysis.

### Preprint

For a detailed description of the project and its biological significance, please refer to our preprint:
> [**Regulatory role of chromosomal DnaA titration in bacterial DNA replication**](https://www.biorxiv.org/content/10.1101/2024.10.07.617004v1)  
> _by Olivi et al._

### Key Findings
- **DnaA motif detection**: We identified conserved DnaA box motifs across *E. coli* and *Salmonella enterica* genomes. Our analysis showed that DnaA boxes cluster around the replication origin (oriC), supporting the titration model for DnaA regulation.
- **Motif shuffling**: Using shuffled motifs, we compared the distribution of real motifs against randomized controls to statistically validate motif overrepresentation near oriC.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
   - [DnaA Motif Detection](#dnaA-motif-detection)
   - [Motif Shuffling](#motif-shuffling)
4. [Contributing](#contributing)
5. [License](#license)
6. [Citation](#citation)

## Features

- **Motif detection**: Detect DnaA box motifs in circular genomes, allowing for both forward and reverse complement matching.
- **Motif shuffling**: Generate shuffled versions of detected motifs for control datasets.
- **Performance**: Optimized for large bacterial genomes with circular chromosome support.
- **Statistical validation**: Enable comparison of real motif distributions against shuffled controls.

## Installation

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/stephkoest/Ecoli_titration.git
cd Ecoli_titration
```

# DnaA Motif Detection and Motif Shuffling

![License](https://img.shields.io/github/license/stephkoest/Ecoli_titration)
![Version](https://img.shields.io/badge/version-1.0-blue)

## Overview

This repository contains Python scripts developed as part of our study on **DnaA titration and its regulatory role in *Escherichia coli* replication initiation**. The scripts allow for:
1. **Detection of DnaA box motifs** on circular bacterial genomes.
2. **Shuffling of DnaA box motifs** to generate control datasets for statistical analysis.

### Preprint

For a detailed description of the project and its biological significance, please refer to our preprint:
> [**The Escherichia coli replication initiator DnaA is titrated on the chromosome**](https://www.biorxiv.org/content/10.1101/2024.10.07.617004v1)  
> _by [Lorenzo Olivi] et al._

### Key Findings
- **DnaA motif detection**: We identified conserved DnaA box motifs across *E. coli* and *Salmonella enterica* genomes. Our analysis showed that DnaA boxes cluster around the replication origin (oriC), supporting the titration model for DnaA regulation.
- **Motif shuffling**: Using shuffled motifs, we compared the distribution of real motifs against randomized controls to statistically validate motif overrepresentation near oriC.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
   - [DnaA Motif Detection](#dnaA-motif-detection)
   - [Motif Shuffling](#motif-shuffling)
4. [Contributing](#contributing)
5. [License](#license)
6. [Citation](#citation)

## Features

- **Motif detection**: Detect DnaA box motifs in circular genomes, allowing for both forward and reverse complement matching.
- **Motif shuffling**: Generate shuffled versions of detected motifs for control datasets.
- **Performance**: Optimized for large bacterial genomes with circular chromosome support.
- **Statistical validation**: Enable comparison of real motif distributions against shuffled controls.

## Installation

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/stephkoest/Ecoli_titration.git
cd Ecoli_titration
#Ensure you have Python 3 installed. it should need no further packages, as it runs with basic python.
```

## Usage

### DnaA Motif Detection

Detect DnaA box motifs on a genome provided in FASTA format.

```bash
python matchBox.py <DnaA_box_fasta> <genome_fasta>
```

**Arguments**:
- `<DnaA_box_fasta>`: A FASTA file containing DnaA box motifs.
- `<genome_fasta>`: A FASTA file of the target genome (circular genome support included).

The output will list all detected DnaA motifs in the genome, with their coordinates, sequences, and strand orientation.

### Motif Shuffling

Generate shuffled versions of the DnaA box motifs for statistical comparison.

```bash
python shuffleBoxes.py <DnaA_box_fasta> <output_fasta> <N>
```

**Arguments**:
- `<DnaA_box_fasta>`: The original DnaA box motif FASTA file.
- `<output_fasta>`: Output FASTA file for the shuffled motifs.
- `<N>`: Number of shuffled sets to generate.

This script will output `N` sets of shuffled motifs, which can then be used for downstream statistical analysis and comparison with real motif distributions.

## License

This project is licensed under the MIT License. 

## Citation

If you use this code in your research, please cite our preprint:

> [**The Escherichia coli replication initiator DnaA is titrated on the chromosome**](https://www.biorxiv.org/content/10.1101/2024.10.07.617004v1)  
> _by Olivi et al._



