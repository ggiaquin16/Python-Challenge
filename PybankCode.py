import os
import csv

budgetCsvPath = os.path.join('..','Python','budget_data.csv')
rowCount = 0
netTotal = 0
change = 0
previous = 0
averageChange = 0
greatestIncrease = 0
increaseMonth = ""
greatestDecrease = 999999999
decreaseMonth = ""

with open(budgetCsvPath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        netTotal += int(row[1])
        rowCount += 1
        if rowCount > 1:
            change = int(row[1]) - previous
        previous = int(row[1])
        averageChange += change

        if (change > greatestIncrease):
            greatestIncrease = change
            increaseMonth = row[0]
        elif (change < greatestDecrease):
            greatestDecrease = change
            decreaseMonth = row[0]

    averageChange = round(averageChange  / (rowCount - 1),2)

outputPath = os.path.join("..", "Python", "bank_data.txt")
file = open(outputPath, "w")

file.write("Financial Analysis" + "\n")
print("Financial Analysis")

file.write("----------------------------------" + "\n")
print("----------------------------------")

file.write(f"Total Months: {rowCount}" + "\n")
print(f"Total Months: {rowCount}")

file.write(f"Total: ${netTotal}" + "\n")
print(f"Total: ${netTotal}")

file.write(f"Average Change: ${averageChange}" + "\n")
print(f"Average Change: ${averageChange}")

file.write(f"Greatest Increase in Profits: {increaseMonth} (${greatestIncrease})" + "\n")
print(f"Greatest Increase in Profits: {increaseMonth} (${greatestIncrease})")

file.write(f"Greatest Decreaes in Profits: {decreaseMonth} (${greatestDecrease})")
print(f"Greatest Decreaes in Profits: {decreaseMonth} (${greatestDecrease})")

file.close()



