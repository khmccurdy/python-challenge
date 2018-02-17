import os
import csv

csvfolder = 'raw_data'
docs = os.listdir(csvfolder)
csvfilelist = [doc for doc in docs if doc.endswith(".csv")]
#csvoptions = ["("+str(i)+") "+csvfilelist[i] for i in range(len(csvfilelist))]
csvoptions = ""
for i in range(len(csvfilelist)):
	csvoptions += " ("+str(i)+") "+ csvfilelist[i]+" "

print("Choose a file:")
print(csvoptions)
filenum = int(input("Read file number: "))
filename = csvfilelist[filenum]

csvpath = os.path.join(csvfolder, filename)

with open(csvpath, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	months=0
	totalRev = 0
	firstRev = 0
	lastRev = 0
	maxrow = ["No Increase", 0]
	minrow = ["No Decrease", 0]
	
	for row in csvreader:
		if row[0] == "Date":
			continue
		months += 1
		
		rev = int(row[1])
		totalRev += rev
		
		if rev > maxrow[1]:
			maxrow = [row[0], rev]
		elif rev < minrow[1]:
			minrow = [row[0], rev]
		
		if months==1:
			firstRev = rev
		lastRev = rev

avgChange = (lastRev-firstRev)/(months-1)
avgChange = round(avgChange)

analysis = ["\nFinancial Analysis \n-------------------",
			"Total Months: "+ str(months),
			"Total Revenue: $" + str(totalRev),
			"Average Revenue Change: $" + str(avgChange),
			"Greatest Increase in Revenue: " + maxrow[0] + " ($"+str(maxrow[1])+")",
			"Greatest Decrease in Revenue: " + minrow[0] + " ($"+str(minrow[1])+")"]

with open("analysis.txt","w") as output:
	for line in analysis:
		output.write(line+"\n")
		print(line)