#Modules
import os
import csv

#Set path for file
csvpath ='./Resources/budget_data.csv'

#Set Variables
total_months = 0
total_revenue = 0
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
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader: 
        # Total Months
        total_months += 1

        # Total Revenue
        total_revenue = total_revenue + (int(row[1]))
        # Revenue FChange
        monthly_revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change.append(monthly_revenue_change)

        average_revenue_change = round(sum(revenue_change)/(total_months),2)

        if (monthly_revenue_change > greatest_increase):
            greatest_increase_month = row [0]
            greatest_increase = monthly_revenue_change
        elif (monthly_revenue_change < greatest_decrease):
             greatest_decrease_month = row [0]
             greatest_decrease = monthly_revenue_change

#Print Financial Analysis
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_revenue_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease})")