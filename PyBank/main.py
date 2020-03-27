#Modules
import os
import csv

#Set path for file
csvpath ='./Resources/budget_data.csv'

#Set Variables
months = []
total_revenue = []
greatest_increase = 0
greatest_decrease = 0
revenue = 0
previous_revenue = 0
revenue_change = []
row = []

#Read in the csv file -- 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader: 
        months.append(row[0])
        total_revenue.append(row[1])
        monthly_rev_change = int(row[1])- previous_revenue
        revenue_change.append(monthly_rev_change)
        if (monthly_rev_change > greatest_increase):
            greatest_increase_month = row [0]
            greatest_increase = monthly_rev_change
        elif (monthly_rev_change < greatest_decrease):
            greatest_decrease_month = row [0]
            greatest_decrease = monthly_rev_change
        previous_revenue = int(row[1])
print(greatest_increase_month)
print(sum(total_revenue))
total_months = len(months)
print(total_months)
print(greatest_increase)
print(greatest_decrease)
print(greatest_decrease_month)

#Print Financial Analysis
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${final_total_revenue}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease})")

#Export to text file
outpath = os.path.join("..","output", "budget_data.txt")
with open(outputpath, 'w') as outputfile:
    textwriter = textwriter(textfile)

    outputfile.write("Financial Analysis\n")
    outputfile.write("---------------------------\n")
    outputfile.write(f"Total Months: + {total_months}\n")
    outputfile.write(f"Total + {int(total_revenue)}\n")
    outputfile.write(f"Greatest Increase in Profits: + {month_increase} + ({greatest_increase})\n")
    outputfile.write(f"Greatest Decrease in Profits: + {month_decrease} + ({greatest_decrease})")

for lines in line:
    print(line)