import os, csv
poll_data = os.path.join("Resources", "election_data.csv")

with open(poll_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
Political_Candidate_Dict = {}
names_list = []
Names_Set = set()
Total_Votes = 0

with open(poll_data, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for row in csvreader:
        
        if len(row) > 2:
            
            Total_Votes += 1
            Ballot_ID = row[0]
            County = row[1]
            Candidate = row[2]
            
            if Candidate not in names_list:
                names_list.append(Candidate)
                Political_Candidate_Dict[Candidate] = 1
            
            else:Political_Candidate_Dict[Candidate] += 1

# Calculate and display the percentage of votes for each candidate

for candidate, votes in Political_Candidate_Dict.items():
    percentage = (votes / Total_Votes) * 100
    Political_Candidate_Dict[candidate] = {
        'votes': votes,
        'percentage': percentage
    }

# Find the winner

winner = max(Political_Candidate_Dict, key=lambda x: Political_Candidate_Dict[x]['votes'])

# Prepare the full text with line breaks

val = "\n\n".join([f"{candidate}: {Political_Candidate_Dict[candidate]['percentage']:.3f}% ({Political_Candidate_Dict[candidate]['votes']})" for candidate in names_list])
export = f'''
Election Results
----------------------------
Total Votes: {Total_Votes}
----------------------------
{val}
----------------------------
Winner: {winner}
----------------------------
'''

# Print the full text

print(export)
export_file = "./Analysis/Result.txt"
with open(export_file, 'w') as f:
    f.write(export)