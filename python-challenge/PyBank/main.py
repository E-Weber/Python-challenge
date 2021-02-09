import csv
TotalMonths = 0
TotalProfitLoss = 0
AverageProfitLoss = 0.00
GreatestIncrease = {"date": "", "amount": 0}
GreatestDecrease = {"date": "", "amount": 0}
LastChange = 0
RevenueList = []
Revenueavg = 0
month = []

file_path = "./Resources/budget_data.csv"
out_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    Date = csv_header.index('Date')
    ProfitLoss = csv_header.index('Profit/Losses')
    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the data set
        TotalMonths = TotalMonths + 1
        date = row[0]
        profit = float(row[1])

    # Net total Amount of profit/loss over entire period
        TotalProfitLoss = TotalProfitLoss + int(row[ProfitLoss])

    # Calculate changes in profit/loss over entire period, then find average
        AverageProfitLoss = float(row[1]) - LastChange
        LastChange = float(row[1])
        RevenueList = RevenueList + [LastChange]
        month = [month] + (row["date"])

    # The greatest increase in losses (date and amount) over the entire period
        if (profit > GreatestIncrease["amount"]):
            GreatestIncrease["date"] = date
            GreatestIncrease["amount"] = profit
    # The greatest decrease in losses(date and amount) over the entire period
        if (profit < GreatestDecrease["amount"]):
            GreatestDecrease["date"] = date
            GreatestDecrease["amount"] = profit
    Revenueavg = sum(RevenueList) / len(RevenueList)


# print results
print("Finacial Analysis")
print("-------------")
print(f"Total Months: {TotalMonths}")
print(
    f"Greatest Increase In Profits: {GreatestIncrease['date']} (${GreatestIncrease['amount']}")
print(
    f"Greatest Decrease In Profits: {GreatestDecrease['date']} (${GreatestDecrease['amount']}")
print(
    f"Total: {TotalProfitLoss}")

# write to a file
with open(out_file, 'w') as outputFile:
    outputFile.write("Financial Analysis")
    outputFile.write("-------------")
    outputFile.write(f"Total Months: {TotalMonths}")
    outputFile.write("Total:{TotalProfitLoss}")
#  Results Below
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
