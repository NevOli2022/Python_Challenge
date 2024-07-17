import os
import csv

print("Election Results")
print("----------------------------------------")

Ballot_id=[]
Candidate= []

with open('Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        Candidate.append(row[2])
        Ballot_id.append(row[0])

    Vote_Total = len(Ballot_id)

    List_of_Candidates = list(set(Candidate))
    List_of_Candidates.sort()
    
    Popular = [Candidate.count(x) for x in List_of_Candidates]

    Percentage = [round((Popular[i] / Vote_Total) * 100, 3) for i in range(len(Popular))]

    for w in Popular:
        Votes = max(Popular)
        Votes_master = Popular.index(Votes)
        Winner = List_of_Candidates[Votes_master]

print("Total Votes: " + str(Vote_Total))
print("-----------------------------------------")
for i in range(len(List_of_Candidates)):
        print(f"{List_of_Candidates[i]}: {Percentage[i]:.3f}% ({Popular[i]})")
print("-----------------------------------------")
print("Winner: " + str(Winner))
print("-----------------------------------------")


#Export
output = open("Analysis/Election Analysis", "w")
with open("Analysis/Election_Analsys",'w') as file:
    file.write("Election Results\n")
    file.write("---------------------------------------------------------------------\n")
    file.write(f"Total Votes: {Vote_Total}\n")
    file.write("---------------------------------------------------------------------\n")
    file.write(f"{List_of_Candidates[1]}: {Percentage[0]}% ({Popular[0]})\n")
    file.write(f"{List_of_Candidates[0]}: {Percentage[1]}% ({Popular[1]})\n")
    file.write(f"{List_of_Candidates[2]}: {Percentage[2]}% ({Popular[2]})\n")
    file.write("-----------------------------------------\n")
    file.write(f"Winner: {Winner}\n")
    file.write("-----------------------------------------\n")

