# importe required libraries
import openpyxl
import csv
import pandas as pd

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

# read the csv file and
# convert into dataframe object
df = pd.DataFrame(pd.read_csv("tt.csv"))

# show the dataframe
df

#test