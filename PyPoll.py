import os
import csv

# Path to collect data from the Resources folder
electionCsvPath = os.path.join('..', 'Python', 'election_data.csv')
totalVotes = 0
ElectionResults = {}

with open(electionCsvPath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

      candidate = row[2]

      if candidate in ElectionResults:
        ElectionResults[candidate] = ElectionResults[candidate] + 1
      else:
        ElectionResults[candidate] = 1 

      totalVotes += 1

outputPath = os.path.join('..', 'Python', 'election_data.txt')
file = open(outputPath, 'w')

print("Election Results:")
file.write("Election Results:" + "\n")

print("----------------------------------")
file.write("----------------------------------" + "\n")

print(f"Total Votes: {totalVotes}")
file.write(f"Total Votes: {totalVotes}" + "\n")

print("----------------------------------")
file.write("----------------------------------" + "\n")

for candidate, votes in ElectionResults.items():
    print(candidate + ":   " + str(round((votes/totalVotes) *100,2)) + "%   " + str(votes))
    file.write(candidate + ":   " + str(round((votes/totalVotes) *100,2)) + "%   " + str(votes) + "\n")

print("----------------------------------")
file.write("----------------------------------" + "\n")

print("winner:" + max(ElectionResults, key=ElectionResults.get))
file.write("winner:" + max(ElectionResults, key=ElectionResults.get))
file.close()

