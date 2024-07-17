import os

import csv

print("Financial Analysis")
print("---------------------------------------------")


with open('Resources/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    Total_Months = 0
    Total_Sum = 0
    Profit_Changes = []
    Dates = []
    change = 0
    current_value = 0
    Previous_value = 0

    for row in csvreader:
        Total_Months += 1
        Total_Sum += int(row[1])

        current_value = int(row[1])
        if Total_Months > 1:  # Exclude the first change value
            change = current_value - Previous_value
            Profit_Changes.append(change)

        Dates.append(row[0])

        Previous_value = current_value

    Average_Change = sum(Profit_Changes) / len(Profit_Changes)
    Greatest_Inc = max(Profit_Changes)
    Greatest_Dec = min(Profit_Changes)
    Inc_Date = Dates[Profit_Changes.index(Greatest_Inc)+1]
    Dec_Date = Dates[Profit_Changes.index(Greatest_Dec)+1]

print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Sum}")
print(f"Average Change: ${Average_Change:.2f}")
print(f"Greatest Increase in Profits: {Inc_Date} $({Greatest_Inc})")
print(f"Greatest Decrease in Profits: {Dec_Date} $({Greatest_Dec})")


#Exporting to Text file
output = open("Analysis/Bank_Analysis", "w")
with open("Analysis/Bank_Analysis",'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"---------------------------------------------------------------------\n")
    file.write(f"Total Months: {Total_Months}\n")
    file.write(f"Total: ${Total_Sum}\n")
    file.write(f"Average Change: ${Average_Change:2f}\n")
    file.write(f"Greatest Increase in Profits: {Inc_Date} $({Greatest_Inc})\n")
    file.write(f"Greatest Decrease in Profits: {Dec_Date} $({Greatest_Dec})\n")