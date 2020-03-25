#Modules
import os
import csv

#Set path for file
csvpath ='../Resources/budget_data.csv'

#Set Variables
months = []
total_revenue = []
greatest_increase = []
greatest_decrease = []
revenue = 0

#Read in the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csvheader}")
    # Count Total # of months and total net amount
    for row in csvreader: 
        months.append(row[0])
        total_revenue.append(int(row[1]))
#Total months = length of months
#total revenue = length of revenue
# print(len(months)) #---DO I NEED  A PRINT?
# print(len(total_revenue)) #---- DO I NEED A PRINT?

#Loop through to compare profit/losses to previous row and set revenue to 0 
# SHOULD ALL OF THIS BE UNDER FOR ROW LOOP?
total_months = len(months)
total_revenue = len(revenue) #DOES THIS MEAN TOTAL PROFITS/LOSSES OR COUNT; IT MEANS COUNT
# total_revenue = revenue + 1
average_change = (total_revenue/total_months)
revenue = 0
for x in range(len(total_revenue)): #HOW DOES IT KNOW IT'S ROW [1]?
    if revenue >= greatest_increase
        greatest_increase = revenue
        month_increase = months
    elif revenue <= greatest_decrease
        greatest_decreae = revenue
        month_decrease = months

        #Print the Following Information
Print("Financial Analysis")
Print("---------------------------")
Print(f"Total Months: + {total_months}")
Print(f"Total + {int(total_revenue)}")
Print(f"Greatest Increase in Profits: + {month_increase} + ({greatest_increase})")
Print(f"Greatest Decrease in Profits: + {month_decrease} + ({greatest_decrease})")

outpath = os.path.join("..","output", "budget_data.txt")
with open(output_path, 'w') as textfile:
    textwriter = textwriter(textfile)
