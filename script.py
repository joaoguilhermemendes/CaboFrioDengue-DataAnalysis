import pandas as pd
import os
from typing import List

# Define directories (consistent with Notebook 2)
PROCESSED_DIR: str = 'data/processed/dengue'
FINAL_FILE: str = 'cabo_frio_dengue_consolidated_cleaned.csv'
final_filepath = os.path.join(PROCESSED_DIR, FINAL_FILE)

# List of processed files that will be concatenated
PROCESSED_FILES: List[str] = [
    'DENGBR24_processed.csv', 
    'DENGBR23_processed.csv', 
    'DENGBR22_processed.csv', 
    'DENGBR21_processed.csv', 
    'DENGBR20_processed.csv', 
    'DENGBR19_processed.csv', 
    'DENGBR18_processed.csv', 
    'DENGBR17_processed.csv', 
    'DENGBR16_processed.csv', 
    'DENGBR15_processed.csv'
]

all_cabo_frio_dfs: List[pd.DataFrame] = []

# Loop to load and append each annual DataFrame to the list
for file in PROCESSED_FILES:
    filepath = os.path.join(PROCESSED_DIR, file)
    
    df_temp = pd.read_csv(filepath, sep=';', encoding='utf-8')
    all_cabo_frio_dfs.append(df_temp)

# Concatenate all DataFrames into a single master DF
df_cabo_frio = pd.concat(all_cabo_frio_dfs, ignore_index=True)

# --- Essential Cleaning (Date Conversion) ---    
# SINAN dates are often in DDMMAAAA format (DayMonthYear).
# Date columns: 'DT_SIN_PRI' (Date of First Symptoms) and 'DT_OBITO' (Date of Death)
date_cols: List[str] = ['DT_SIN_PRI', 'DT_OBITO']

for col in date_cols:
    # Convert string to datetime, avoinding errors to NaT (Not a Time)
    df_cabo_frio[col] = pd.to_datetime(
        df_cabo_frio[col], 
        format='%d%m%Y', 
        errors='coerce'
    )

# --- Save the final clean and consolidated file ---
df_cabo_frio.to_csv(final_filepath, sep=';', index=False, encoding='utf-8')