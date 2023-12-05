# Module 3 Challenge - Python
# Two Challnges were completed
Firstly, the following was done:
* Create a new repository for this project called python-challenge
* Repository was cloned to my computer

2 folders were created, PyBank and PyPoll corresponding to each challenge.
Each folder includes:
* main.py, containing the main script
* Resources folder containing the required CSV files used
*Analysis folder containing a text file output

Changes were pushed to GitHub

# PyBank Challenge:
A csv file called budget_data.csv was provided to me, containing the columns "Date" and "Profit/Loss".

Columns were filled with an extended data set

I needed to create a code that calculated:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire perios

The final results should look like:
```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```
The script prints to the terminal and into a text file

#PyPoll Challenge:
I was provided with a set of poll data called election_data.csv. 
The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
I needed to create a Python script that analyzes the votes and calculates each of the following values:

* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote

My analysis should look like:
```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```
The script prints to the terminal and into a text file
