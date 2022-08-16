# import required libraries
import openpyxl
import csv
import pandas as pd
import glob
import os
import covid_file_reader

#path = /home/username/COVIDdatafolder


def main():
	df = covid_file_reader.main()

	#empty dataframe for duplicate data
	df_duplicates = pd.DataFrame()

	#empty list for duplicate data positions
	duplicate_pos = []

	#empty list for unnecesasry data rows
	extradata_pos = []

	print(df) #testing print in terminal

	#integer values for index positions
	i_pos = 0
	j_pos = i_pos+1 #integer values for index positions

	# add duplicate data to new csv file
	for i in df.iloc[:, 2]: #2 in reference to third column 'SampleName'
		for j in df.iloc[(i_pos+1):, 2]:
			if (i.__contains__("UA89-") == False) and (i.__contains__("UA99-") == False):
				extradata_pos.append(i_pos)

			else:

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
	remove_pos = duplicate_pos + extradata_pos
	remove_pos_set = [*set(remove_pos)]

	remove_pos_set.sort(reverse=True)

	df = df.drop(index=remove_pos_set)

	df = df.reset_index(drop=True)

	df.to_csv('COVID_Data_Combined.csv', index=False)
	df_duplicates.to_csv('COVID_Data_Duplicates.csv', index=False)

if __name__== "__main__" :
    main()