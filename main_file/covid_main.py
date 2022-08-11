# importe required libraries
import openpyxl
import csv
import pandas as pd
import glob
import os


#TODO right now we concat only the first sheet of each excel file, need to combine the multiple sheets
#FIXME when combining sheets, after 'Invalid' column there is a NaN row that does not show on excel (8 rows instead of expected 7)
#TODO add in filter to df to remove submissions without 'STARS-' name
#TODO the duplicate_pos list duplicates multiple instances


path = r'/home/davidruddell/Documents/Data7Projects/harris-data-pull/' # use your path

#combine all files into one dataframe
all_files = glob.glob(os.path.join(path, "*.xlsx"))
df_allfiles = pd.concat((pd.read_excel(f) for f in all_files), ignore_index=True)

#main combined dataframe
df = pd.DataFrame(columns= ['iLab Submission #', 'Position', 'SampleName', 'N1', 'RP', 'Interpretation'])
df = pd.concat([df, df_allfiles], ignore_index=True)

#empty dataframe for duplicate data
df_duplicates = pd.DataFrame()

#empty list for duplicate data positions
duplicate_pos = []

print(df) #testing print in terminal

#integer values for index positions
i_pos = 0
j_pos = i_pos+1 #integer values for index positions

#FIXME currently when making df duplicates, using j_pos returns an index that is out of bounds. loops may be incorrect
# add duplicate data to new csv file
for i in df.iloc[:, 2]: #2 in reference to third column 'SampleName'
	for j in df.iloc[(i_pos+1):, 2]:
		if (i == j):
			if (i_pos not in duplicate_pos):
				df_duplicates_new_row = pd.DataFrame({
					'iLab Submission #' : [df.iloc[i_pos]['iLab Submission #']],
					'Position' : [df.iloc[i_pos]['Position']], #FIXME j_pos causing indexer out of bounds
					'SampleName' : [df.iloc[i_pos]['SampleName']],
					'N1' : [df.iloc[i_pos]['N1']],
					'RP' : [df.iloc[i_pos]['RP']],
					'Interpretation' : [df.iloc[i_pos]['Interpretation']]
					})
				
				df_duplicates = pd.concat([df_duplicates, df_duplicates_new_row], ignore_index=True) #add new row to duplicates (append method removed in future pandas version)

				#add the column numbers (i_pos) to list of duplicates
				duplicate_pos.append(i_pos)
			
			if (j_pos not in duplicate_pos):
				df_duplicates_new_row = pd.DataFrame({
					'iLab Submission #' : [df.iloc[j_pos]['iLab Submission #']],
					'Position' : [df.iloc[j_pos]['Position']], #FIXME j_pos causing indexer out of bounds
					'SampleName' : [df.iloc[j_pos]['SampleName']],
					'N1' : [df.iloc[j_pos]['N1']],
					'RP' : [df.iloc[j_pos]['RP']],
					'Interpretation' : [df.iloc[j_pos]['Interpretation']]
					})
				
				df_duplicates = pd.concat([df_duplicates, df_duplicates_new_row], ignore_index=True) #add new row to duplicates (append method removed in future pandas version)

				#add the column number (j_pos) to list of duplicates
				duplicate_pos.append(j_pos)
		
		j_pos += 1

	i_pos += 1
	j_pos = i_pos+1

#FIXME i did this loop wrong im fairly sure (review sometime)
#delete duplicate data from main dataframe
for i in duplicate_pos:
	df.drop([i])

df #print dataframe