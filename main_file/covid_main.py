# importe required libraries
import openpyxl
import csv
import pandas as pd
import glob
import os
import covid_file_reader

#path = r'/home/davidruddell/Documents/Data7Projects/harris-data-pull/' # use your path


def main():
	df = covid_file_reader.main()

	#empty dataframe for duplicate data
	df_duplicates = pd.DataFrame()

	#empty list for duplicate data positions
	duplicate_pos = []

	print(df) #testing print in terminal

	#integer values for index positions
	i_pos = 0
	j_pos = i_pos+1 #integer values for index positions

	# add duplicate data to new csv file
	for i in df.iloc[:, 2]: #2 in reference to third column 'SampleName'
		for j in df.iloc[(i_pos+1):, 2]:
			if (i == j):
				if (i_pos not in duplicate_pos):
					df_duplicates_new_row = pd.DataFrame({
						'iLab Submission #' : [df.iloc[i_pos]['iLab Submission #']],
						'Position' : [df.iloc[i_pos]['Position']],
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
						'Position' : [df.iloc[j_pos]['Position']],
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

	#delete duplicate data from main dataframe
	duplicate_pos.sort(reverse=True)
	print(duplicate_pos)

	df = df.drop(index=duplicate_pos)

	df = df.reset_index(drop=True)

	print(df) #print dataframe

if __name__== "__main__" :
    main()