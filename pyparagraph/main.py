import os
#import re

#create numbered list of txt files to choose from at runtime
textdir = 'raw_data'
docs = os.listdir(textdir)
txtfilelist = [doc for doc in docs if doc.endswith(".txt")]
txtoptions = ""
for i in range(len(txtfilelist)):
	txtoptions += " ("+str(i)+") "+ txtfilelist[i]+" "

print("Choose a file:")
print(txtoptions)
filenum = int(input("Read file number: "))
textfile = txtfilelist[filenum]

#open text file and convert to string
textpath = os.path.join(textdir, textfile)

with open(textpath, 'r') as paragraph_txt:
	paragraph = str(paragraph_txt.read())
	
#calculate word count w.r.t. spaces
word_count = len(paragraph.split(' '))

#calculate sentence count by unifying sentence-end punctuation and splitting
#(re method just threw up errors)
paragraph_sentences = paragraph.replace("!", ".")
paragraph_sentences = paragraph_sentences.replace("?", ".")
#subtract 1 so empty space after last period isn't counted as a sentence
sentence_count = len(paragraph_sentences.split('.')) - 1

#count alphanumeric characters for letter count
letter_count = len([ch for ch in paragraph if ch.isalnum()])

#print analysis and calculate averages
print("Paragraph Analysis")
print("------------------")
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average Letter Count: " + str(letter_count/word_count))
print("Average Sentence Length: "+ str(word_count/sentence_count))