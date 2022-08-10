# importe required libraries
import openpyxl
import csv
import pandas as pd
import glob
import os


#FIXME right now we concat only the first sheet of each excel file, need to combine the multiple sheets
#FIXME when combining sheets, after 'Invalid' column there is a NaN row that does not show on excel (8 rows instead of expected 7)


path = r'/home/davidruddell/Documents/Data7Projects/harris-data-pull/' # use your path

#combine all files into one dataframe
all_files = glob.glob(os.path.join(path, "*.xlsx"))
df_allfiles = pd.concat((pd.read_excel(f) for f in all_files), ignore_index=True)

#main combined dataframe
df = pd.DataFrame(columns= ['iLab Submission #', 'Position', 'SampleName', 'N1', 'RP', 'Interpretation', 'OKCheck'])
df = pd.concat([df, df_allfiles], ignore_index=True)

#empty dataframe for duplicate data
df_duplicates = pd.DataFrame()

#empty list for duplicate data positions
duplicate_pos = []

print(df) #testing print in terminal

#integer values for index positions
i_pos = 0
j_pos = 0 #integer values for index positions
# add duplicate data to new csv file
for i in df.iloc[:, 3]: #3 in reference to third column 'SampleName'
	for j in df.iloc[i_pos:, 3]:
		if (i == j):
			df_duplicates = df_duplicates.append({
				'iLab Submission #' : df.iloc[j_pos]['iLab Submission #'],
				'Position' : df.iloc[j_pos]['Position'],
				'SampleName' : df.iloc[j_pos]['SampleName'],
				'N1' : df.iloc[j_pos]['N1'],
				'RP' : df.iloc[j_pos]['RP'],
				'Interpretation' : df.iloc[j_pos]['Interpretation'],
				'OKCheck' : df.iloc[j_pos]['OKCheck']
				}, ignore_index=True)
			
			duplicate_pos = duplicate_pos.append(j_pos)
		
		j_pos +=1
	i_pos += 1

#delete duplicate data from main dataframe
for i in duplicate_pos:
	df.drop([i])

df #print dataframe












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