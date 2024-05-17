import os
import csv

# Initialize variables
total_votes = 0
candidate = ""
votes_for_candidate = {} # Define dictionary for candidates name
winning_votes = 0
winner = ""

# Define the relative directory path
relative_input_dir = '..\python-challenge\PyPoll\Resources'

# Join the current directory with the relative directory
election_csv = os.path.join(relative_input_dir,'election_data.csv')

# Open the CSV file in read mode
with open(election_csv, 'r') as csvfile:
    
# Create a CSV reader object
    csv_reader = csv.reader(csvfile)

# Skip the header row (if present)
    next(csv_reader)

# Process each row after skipping the header
    for row in csv_reader:
        
        # Get the candidates name
        candidate = row[2]
        
        # Calculate votes for each candidate
        if candidate in votes_for_candidate:
            votes_for_candidate[candidate] += 1
        else: 
            votes_for_candidate[candidate] = 1
        
        # Calculate total votes
        total_votes += 1
        
# Print out the results
print(f"Election Results")
print(f"-------------------------------------------")
print(f"Total Votes: {total_votes:,}")
print(f"-------------------------------------------")


for candidate, votes in votes_for_candidate.items():
    vote_percentage = round((votes / total_votes) * 100, 2)
    
    print(f'{candidate}: {vote_percentage:.2f}% ({votes:,})') 
    
print(f"-------------------------------------------")

# Find the winner of the election
for candidate, votes in votes_for_candidate.items():
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
        
print(f"Winner: {winner}")
print(f"-------------------------------------------")

# Set variables for output file
# Define the relative directory path
relative_output_dir = '..\python-challenge\PyPoll\Results'

# Join the current directory with the relative directory
results_output = os.path.join(relative_output_dir, "PyPoll Election Results")

# Write the results into the PyBank Financial Analysis.txt file
with open(results_output, "w") as output_csv_file:
    output_csv_file.write("Election Results\n")
    output_csv_file.write("--------------------------------------------\n")
    output_csv_file.write(f"Total Votes: {total_votes:,}\n")
    output_csv_file.write("--------------------------------------------\n")

    for candidate, votes in votes_for_candidate.items():
        vote_percentage = round((votes / total_votes) * 100, 2)
        output_csv_file.write(f"{candidate}: {vote_percentage:.2f}% ({votes:,})\n") 
        
    output_csv_file.write("--------------------------------------------\n") 

    output_csv_file.write(f"Winner: {winner}\n")
    
    output_csv_file.write("--------------------------------------------\n")
    