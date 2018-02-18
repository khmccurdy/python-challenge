import os
import csv

#create numbered list of csv files to choose from at runtime
csvfolder = 'raw_data'
docs = os.listdir(csvfolder)
csvfilelist = [doc for doc in docs if doc.endswith(".csv")]
csvoptions = ""
for i in range(len(csvfilelist)):
	csvoptions += " ("+str(i)+") "+ csvfilelist[i]+" "

print("Choose a file:")
print(csvoptions)
filenum = int(input("Read file number: "))
filename = csvfilelist[filenum]

#open selected csv file
csvpath = os.path.join(csvfolder, filename)

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	#initialize variables
	months=0
	totalRev = 0
	firstRev = 0
	lastRev = 0
	maxrow = ["No Increase", 0]
	minrow = ["No Decrease", 0]
	
	for row in csvreader:
		#don't count the label row
		
		if row[0] == "Date":
			continue
		months += 1
		
		#convert revenue column to an integer, sum values
		rev = int(row[1])
		totalRev += rev
		
		#calculate running max increase and decrease
		if rev > maxrow[1]:
			maxrow = [row[0], rev]
		elif rev < minrow[1]:
			minrow = [row[0], rev]
		
		#store first and final revenues for use in average change
		if months==1:
			firstRev = rev
		lastRev = rev

#calculate average change
avgChange = (lastRev-firstRev)/(months-1)
avgChange = round(avgChange)

#save output lines to a list
analysis = ["\nFinancial Analysis \n-------------------",
			"Total Months: "+ str(months),
			"Total Revenue: $" + str(totalRev),
			"Average Revenue Change: $" + str(avgChange),
			"Greatest Increase in Revenue: " + maxrow[0] + " ($"+str(maxrow[1])+")",
			"Greatest Decrease in Revenue: " + minrow[0] + " ($"+str(minrow[1])+")"]

#write output to file and print to terminal
with open("analysis.txt","w") as output:
	for line in analysis:
		output.write(line+"\n")
		print(line)