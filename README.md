# Performance of Epidemiological Surveillance: The Symptom-to-Death Interval in Fatal Dengue Cases, Cabo Frio (2015–2024)


## Abstract
> This repository documents and executes the Extract, Transform, Load (ETL) pipeline designed to generate a temporally coherent and clean dataset of Notifiable Dengue cases for the municipality of Cabo Frio, Rio de Janeiro (IBGE Code: 330070). The raw data is sourced from the official Brazilian Notifiable Diseases Information System (SINAN) via the openDataSUS platform. The objective of this pipeline is to transition raw, large-scale, annual national files into a single, standardized, analysis-ready CSV file spanning ten years (2015 to 2024) suitable for subsequent spatio-temporal modeling and epidemiological analysis.


## 1. Research Context
Dengue fever remains one of the major vector-borne diseases in Brazil, with recurrent seasonal outbreaks. Cabo Frio, a coastal municipality in the state of Rio de Janeiro, presents climatic and demographic conditions that make it particularly relevant for local epidemiological analysis.

This project aims to:
- Consolidate dengue records across ten consecutive years (2015–2024) for the municipality of Cabo Frio.
- Establish a clean, structured dataset derived from **SINAN (Sistema de Informação de Agravos de Notificação)** records.
- Enable reproducible descriptive analysis and temporal interpretation.


## 1. Data Source and Scope

### 1.1 Source System

The data is collected from the Sistema de Informação de Agravos de Notificação (SINAN), the official repository for mandatory notification diseases in Brazil, maintained by the Ministry of Health. Data files are accessed as publicly available annual archives.

### 1.2 Geographic and Temporal Scope

Target Geography: Municipality of Cabo Frio, Rio de Janeiro (ID_MN_RESI = '330070').
Time Series: 10 fiscal years (2015 to 2024).

### 1.3 Selected Features

To optimize the dataset for focal analysis, the ETL pipeline reduces the feature space to the following critical epidemiological variables:

| Column Name | Description | Data Type after Cleaning |
|--------------|-------------|---------------------------|
| **ID_MN_RESI** | Municipality of Residence (IBGE 6-digit code) | String |
| **DT_SIN_PRI** | Date of First Symptoms | Date/Time |
| **NU_IDADE_N** | Age (Normalized) | Numeric (Integer) |
| **CS_SEXO** | Sex | String |
| **CS_RACA** | Race/Color | String |
| **CLASSI_FIN** | Final Case Classification (e.g., Dengue, Zika, Chikungunya) | String |
| **EVOLUCAO** | Case Outcome (Cure, Death, etc.) | String |
| **DT_OBITO** | Date of Death | Date/Time |


## 2. ETL Pipeline Methodology

The data transformation process is structured into sequential Jupyter Notebooks, ensuring modularity, data provenance, and reproducibility.

### Stage 1: Data Acquisition (01-Getting Data About Dengue Across Brazil.ipynb)

This notebook is responsible for the automated ingestion of raw data.

Process: Downloads annual .zip archives of national dengue case data from the openDataSUS S3 bucket.

Output: Creates the data/raw/dengue/ directory and deposits all original, annual national CSV files (e.g., DENGBR15.csv through DENGBR24.csv).

---

### Stage 2: Geographic Filtering and Reduction (02-Selecting Only CABO FRIO Data.ipynb)

This notebook performs the first major transformation, filtering the national records down to the target municipality.

Process: Iterates through all files in data/raw/dengue/, selects only the required columns, and applies a rigid filter (ID_MN_RESI == '330070').

Output: Saves annual, reduced CSV files (e.g., DENGBR15_processed.csv) into the data/processed/dengue/ directory.

---

### Stage 3: Harmonization and Consolidation (03-Merging All the Files into a Essential DF (CABO FRIO 2015-2024).ipynb)

This notebook merges the intermediate annual files into a final master dataset and ensures temporal coherence.

Process: Reads all *_processed.csv files, concatenates them into a single pandas DataFrame, and performs critical type conversion (string dates in DDMMYYYY format are converted to datetime objects).

Output: Generates the final, analysis-ready file: data/processed/dengue/DENGCF10y.csv.

---

### Stage 4: (04-(...).ipynb)
...

## 3. Repository Structure

```
DengueAnalysis/
├── data/
│   ├── raw/                  
│   │   └── dengue/
│   │       ├── DENGBR15.csv
│   │       └── ...
│   └── processed/            
│       └── dengue/
│           ├── DENGBR15_processed.csv
│           └── DENGCF10y.csv
├── notebooks/            
│   ├── 01-Getting Data About Dengue Across Brazil.ipynb
│   ├── 02-Selecting Only CABO FRIO Data.ipynb
│   └── 03-Merging All the Files into a Essential DF (CABO FRIO 2015-2024).ipynb
├── README.md              
└── requirements.txt     
```
---

## 4. Reproducibility and Dependencies

### 4.1 Required Libraries

This project relies on standard scientific Python libraries. Installation via pip is recommended.

```
pip install pandas requests
```


### 4.2 Execution Order

To reproduce the final dataset, the notebooks must be executed sequentially:

* 01-Getting Data About Dengue Across Brazil.ipynb
* 02-Selecting Only CABO FRIO Data.ipynb
* 03-Merging All the Files into a Essential DF (CABO FRIO 2015-2024).ipynb
* 04-(...).ipynb