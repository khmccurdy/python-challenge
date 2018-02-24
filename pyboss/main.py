import os
import csv
#import state abbreviation dictionary
from us_state_abbrev import us_state_abbrev as stateref

#list of csv files
csvfolder = 'raw_data'
docs = os.listdir(csvfolder)
csvfiles = [doc for doc in docs if doc.endswith(".csv")]

def format(csvpath):
	with open(csvpath, newline = '') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		
		#initialize column lists with labels
		emp_id = ["Emp ID"]
		first_name = ["First Name"]
		last_name = ["Last Name"]
		dob = ["DOB"]
		ssn = ["SSN"]
		state = ["State"]
		
		for row in csvreader:
			#skip label row
			if row[0] == "Emp ID":
				continue
			
			emp_id.append(row[0])
			
			#split name into first and last
			name = row[1].split(" ")
			first_name.append(name[0])
			last_name.append(name[1])
			
			#rearrange date of birth
			old_dob = row[2].split("-")
			new_dob = old_dob[1]+"/"+old_dob[2]+"/"+old_dob[0]
			dob.append(new_dob)
			
			#replace first 5 ssn digits with *'s
			ssn.append("***-**-"+row[3][-4:])
			
			#replace state with abbreviation using the dictionary
			state.append(stateref[row[4]])
		
		#zip the column lists
		newlist = zip(emp_id,first_name,last_name,dob,ssn,state)
		
		#make sure output directory exists
		outdir = 'output'
		if not os.path.exists(outdir):
			os.makedirs(outdir)
		
		#set output path to output\<source_name>_formatted.csv
		output_name = os.path.split(csvpath)[1][:-4] + "_formatted.csv"
		output_path = os.path.join(outdir, output_name)
		print(output_path)
		
		#write newlist into a file
		with open(output_path, 'w', newline = '') as output_file:
			csvwriter = csv.writer(output_file, delimiter=',')
			for row in newlist:
				csvwriter.writerow(row)
		
#run format on all files in list
for file in csvfiles:
	format(os.path.join(csvfolder,file))