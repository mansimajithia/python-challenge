import os
import csv

#Set file for path
csvpath = '../Resources/election_data.csv'

#Variables to store data
#Total votes = total votes + 1 (=+ 1)
#unique candidates
#The total number of votes each candidate won
#The winner of the election based on popular votes
    #if a>b and c
total_votes= row[0]
county = row[1]
candidate =row[2]
total_votes = 0
canditates = 
candidate 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csvheader}")
    #count votes
    for row in csvreader:
        total_votes += 1