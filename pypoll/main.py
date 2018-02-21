import os
import csv

#create numbered list of csv files to choose from at runtime
csvfolder = 'raw_data'
docs = os.listdir(csvfolder)
csvfilelist = [doc for doc in docs if doc.endswith(".csv")]
csvoptions = ""
for i in range(len(csvfilelist)):
	csvoptions += f" ({i}) {csvfilelist[i]}"

print("Choose a file:")
print(csvoptions)
filenum = int(input("Read file number: "))
filename = csvfilelist[filenum]

#open selected csv file
csvpath = os.path.join(csvfolder, filename)

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	#initialize variables
	votes = 0
	candidates = {}
	
	for row in csvreader:
		if row[0] == "Voter ID":
			continue
		votes += 1
		
		#if a candidate has not been listed, add them to the dictionary
		#otherwise, increment their vote count
		if not row[2] in candidates:
			candidates[row[2]] = 1
		else:
			candidates[row[2]] += 1

#convert dictionary to list
canList = candidates.items()

#initialize variables to calculate winner
winner = ""
maxvotes = 0

#function for formatting percents
def perc(n):
	return str(round(n*100,1))+"%"

hline = "-------------------"
analysis = ["\nElection results", hline,
			f"Total Votes: {votes}", hline]

#add candidates to analysis, calculate winner
for row in canList:
	analysis.append(f"{row[0]}: {perc(row[1]/votes)} ({row[1]})")
	if row[1] > maxvotes:
		maxvotes = row[1]
		winner = row[0]

#add winner to analysis
analysis.extend([hline, "Winner: "+winner, hline])

with open("analysis.txt","w") as output:
	for line in analysis:
		output.write(line+"\n")
		print(line)