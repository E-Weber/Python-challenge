import os
import csv

csvpath = "./Resources/election_data.csv"

TotalVotes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(f"CSV Header{csv_header}")

    voterID = csv_header.index('Voter ID')
    candidate = csv_header.index('Candidate')
    county = csv_header.index('County')
    candidateList = []
# Read Each row
    for row in csvreader:
        # The total number of votes cast
        TotalVotes = TotalVotes + 1

# A complete list of candidates who received votes
        candidateList.append(str(row[candidate]))
        unique_candidateList = list(set(candidateList))
# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# RESULTS
print(f"Total Votes: {TotalVotes}")
print(f"Candidates: {candidateList}")

# -------------------------
# Total Votes: 3521001
# -------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
#Winner: Khan
# -------------------------
