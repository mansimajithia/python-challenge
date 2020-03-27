import os
import csv

#Set file for path
csvpath = './Resources/election_data.csv'

#List Variables
total_votes = 0
total_candidates = 0
candidates = []
percent_received = []
candidates_list = []
votes_received_list = []
candidate_index = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    #count votes
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidates_list:
            candidates_index = candidates_list.index(candidate)
            votes_received_list[candidates_index] += 1
        else:
            candidates_list.append(candidate)
            votes_received_list.append(1)
print(total_votes)
print(candidates_list)
print(votes_received_list)