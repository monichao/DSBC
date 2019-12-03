#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv
csvpath = os.path.join('..', 'homework', 'election_data.csv')

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    candidates = []
    
    for row in csvreader:
        Name = row[2]
        candidates.append(Name)


total = len(candidates)

# Creating a dictionary  
count = {} 
for name in candidates: 
    if (name in count): 
        count[name] += 1
    else: 
        count[name] = 1


Winner = max(count.keys(), key =(lambda k: count[k]))
        

print ('Election Results \n-------------------------')

file = open('pypoll.txt','a')
file.write('Election Results \n')
file.write('----------------------------------\n')

for name in count:
    percent_votes = count[name]/total
    percent_votes_format = "{:.3%}".format(percent_votes)
    print(f'{name}: {percent_votes_format} ({count[name]})')
    file.write(f'{name}: {percent_votes_format} ({count[name]})\n')
    
print ('------------------------- ')
print(f'Winner :{Winner}')
print ('------------------------- ')
file.write('----------------------------------\n')
file.write(f'Winner: {Winner}')
file.close()

    