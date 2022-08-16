# Author: Quanwei Lei
# Purpose: read in csv files and then filter out failed excel files and sheets that are not useful
# towards the dataset

import csv
import glob
import pandas as pd
import os

def main():
    # asks user for path with all of excel files available,
    # currently using: /home/quan/Desktop/excel
    path = input("Enter Path:")
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    df = pd.DataFrame(columns= ['iLab Submission #', 'Position', 'SampleName', 'N1', 'RP', 'Interpretation'])


    # opens every file name found in folder given
    for f in all_files:
        # if FAIL is found in file name, it will not be scanned
        if f.__contains__("FAIL") == False:
            sheets = pd.read_excel(f, sheet_name = None)
            # filter out STARS
            keys = removal(sheets)
            # for every valid sheet found in the excel sheet, will add the data to the main pandas dataframe
            for key in keys:
                temp = pd.read_excel(f,key)
                df = pd.concat([df, temp], ignore_index=True)

    return df


# removes all sheets with the name STARS, also allows for easy access to filtering of sheets
def removal(keys):
    newkeys = []
    for i in keys:
        # filters out any sheet containing the keyword STARS
        if i.__contains__("STARS") == False:
            newkeys.append(i)
    return newkeys


if __name__== "__main__" :
    main()