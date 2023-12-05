#Importing modules
import os
import csv

#Accessing the budget data csv file
csvpath = os.path.join("..","Resources","budget_data.csv")

with open(csvpath) as budgetcsv:
#Getting the code to read the csv file and recognise commas
    readbudget = csv.reader(budgetcsv, delimiter=",")
    #First Row contains the column names, we don't need them
    next(readbudget)
    #We don't need the first month as part of the net calculations
    num_values = [next(readbudget)]
    #Obtaining the first value of the Profit/Loss column
    pl_num = int(num_values[0][1])
    profloss = []
    #Variable that will help to calculate Profit/Loss
    last_pl = pl_num

    for row in readbudget:
        #Getting the total number of months
        num_values.append(row)
        #Calculating total Profit/Loss
        pl_num = pl_num + int(row[1])
        #Getting the changes in Profit/Loss in the recorded period
        profloss.append(int(row[1])-last_pl)
        #Getting the average change in Profit/Loss
        last_pl = int(row[1])

#Biggest Profit gain
max_gain = profloss.index(max(profloss))
#Biggest Loss
max_loss = profloss.index(min(profloss))

#Exporting all the desired information
export = f''' Financial Analysis
___________________________________
Total Months: {len(num_values)}
Total: ${pl_num}
Average Change: ${round(sum(profloss)/(len(profloss)),2)}
Greatest Increase in Profits: {num_values[max_gain+1][0]} (${max(profloss)})
Greatest Decrease in Profits: {num_values[max_loss+1][0]} (${min(profloss)})
'''

print(export)
csvpath = os.path.join("..","Analysis","Financial_Analysis.txt")
with open(csvpath,"w") as textfile:
    textfile.write(export)
