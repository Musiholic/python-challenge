import os, csv
budget_csv = os.path.join("Resources","budget_data.csv")

#read csv file

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    next(csv_reader)

#variables 

    Months = 0
    Total = 0
    Prev_Revenue = 0
    Rev_Change_List = []
    Month_List = []
    Month_Total = 0

#calculate revenue, months, and total

    for row in csv_reader:
        Months = Months + 1
        Current_Revenue = int(row[1])
        Total = Total + Current_Revenue

        if Prev_Revenue != 0 :
            Rev_Change = Current_Revenue - Prev_Revenue
            Rev_Change_List.append(Rev_Change)
            Month_List.append(row[0])
            Month_Total = Month_Total + Rev_Change

        Prev_Revenue = Current_Revenue

    Ave_Change = Month_Total / (Months - 1)

#print revenue, months, and total

    print(f'Total number of months: {Months}')
    print(f'Total profit/loss: ${Total}')
    print(f'Total change: {Month_Total}')
    print(f'Average change: ${Ave_Change:.2f}')

#Calculate Max Increase and Decrease

    Max_Increase = max(Rev_Change_List)
    Max_Increase_Month = Month_List[Rev_Change_List.index(Max_Increase)]

    print(f"Greatest Increase in Profits: {Max_Increase_Month} (${Max_Increase})")

    Max_Decrease = min(Rev_Change_List)
    Max_Decrease_Month = Month_List[Rev_Change_List.index(Max_Decrease)]

    print(f"Greatest Decrease in Profits: {Max_Decrease_Month} (${Max_Decrease})")

#export to txt file

export = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {Months}\n"
    f"Total: ${Total}\n"
    f"Average Change: ${Ave_Change:.2f}\n"
    f"Greatest Increase in Profits: {Max_Increase_Month} (${Max_Increase})\n"
    f"Greatest Decrease in Profits: {Max_Decrease_Month} (${Max_Decrease})\n")

print(export)
export_file = "./Analysis/Result.txt"
with open(export_file, 'w') as f:
    f.write(export)