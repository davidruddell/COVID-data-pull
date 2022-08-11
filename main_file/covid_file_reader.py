# Author: Quanwei Lei
# Purpose: read in csv files and then filter out failed excel files and non UA-99 and non UA-89 barcodes
import csv
import glob
import pandas as pd
import os
path = input("Enter Path:")
all_files = glob.glob(os.path.join(path, "*.xlsx"))
for f in all_files:
    if f.__contains__("FAIL") == False:
        print(f)
        sheets = pd.read_excel(f, sheet_name = None)
        print(sheets.keys())