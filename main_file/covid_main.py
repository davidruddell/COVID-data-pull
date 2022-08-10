# importe required libraries
from multiprocessing.reduction import duplicate
import openpyxl
import csv
import pandas as pd
import glob
import os

path = r'/home/davidruddell/Documents/Data7Projects/harris-data-pull/' # use your path

#combine all files into one dataframe
all_files = glob.glob(os.path.join(path, "*.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

#empty dataframe for duplicate data
df_duplicates = pd.DataFrame()

#empty list for duplicate data positions
duplicate_pos = []

# add duplicate data to new csv file
for i in df.iloc[:, 'SampleName']:
	for j in df.iloc[i:, 'SampleName']:
		if (i == j):
			df_duplicates = df_duplicates.append({
				'iLab Submission #' : df['iLab Submission #'][j],
				'Position' : df['Position'][j],
				'SampleName' : df['SampleName'][j],
				'N1' : df['N1'][j],
				'RP' : df['RP'][j],
				'Interpretation' : df['Interpretation'][j]
				}, ignore_index=True)
			
			duplicate_pos = duplicate_pos.append(j)

#delete duplicate data from main dataframe
for i in len(duplicate_pos):
	df.drop([i])















''' old code
# open given workbook
# and store in excel object
excel = openpyxl.load_workbook("2021Sep22_ClarityResultsReview-P1-CH.xlsx")

# select the active sheet
sheet = excel.active

# writer object is created
col = csv.writer(open("tt.csv",
					'w',
					newline=""))

# writing the data in csv file
for r in sheet.rows:
	# row by row write
	# operation is perform
	col.writerow([cell.value for cell in r])

# read the csv file ande most basic of these is the humble CSV file. When you open a CSV file you get something that looks like this:
# convert into dataframe object
df = pd.DataFrame(pd.read_csv("tt.csv"))

df_duplicate = pd.DataFrame()

# show the dataframe
df
'''