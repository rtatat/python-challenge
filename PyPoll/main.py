#Importing modules
import os
import csv

#Accessing the election data csv file
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, encoding="UTF-8") as votes:
    #Getting the code to read the csv file and recognise commas
    readvotes = csv.reader(votes, delimiter= ",")
    #We don't need the first row as it contains column names
    next(readvotes)
    #Establishing stores to contain total and candidate votes
    total_votes = []
    candidate_votes = ()
    #Getting the total number of votes
    for vote in readvotes:
        total_votes.append(vote[2])
vote_num = len(total_votes)

#Beginning to establish candidate code
candidates = list(set(total_votes))
total_candid_votes = []
percent = []
#Getting the votes per candidate and list of candidates
for candidate in candidates:
    total_candid_votes.append(total_votes.count(candidate))

#Getting the percentage that each candidate got
all_candidates = []
for i in range (len(candidates)):
    percent = total_candid_votes[i]/vote_num*100
    all_candidates.append(f'{candidates[i]}: {round(percent,3)}% ({total_candid_votes[i]})')
    

#Getting the winner of the election
winner_winner = total_candid_votes.index(max(total_candid_votes))

#Exporting all of the desired information
export = f'''Election Results
__________________________________________

Total Votes: {vote_num}
__________________________________________

{all_candidates}
__________________________________________

Winner: {candidates[winner_winner]}
__________________________________________
'''
print(export)
csvpath = os.path.join("Analysis","Polling_Analysis.txt")
with open(csvpath, "w") as textfile:
    textfile.write(export)
