#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#the greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv
csvpath = os.path.join('..', 'homework', 'budget_data.csv')

with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvfile)

#making lists for profit and months
    profit = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change = []

    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the results
    print("Financial Analysis")
    print("---------------------")
    print("total months: " + str(total_months))
    print("Total: " + "$" + str(sum(profit)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


#making and printing an ouput file
    file = open("output.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("...................................................................................." + "\n")
    file.write("total months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(profit)) + "\n")
    file.write("Average change: " + "$" + str(revenue_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    file.close()
