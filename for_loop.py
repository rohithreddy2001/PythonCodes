expenses = [1500, 3000, 2500, 4000, 3500, 2800]
total = 0
for expense in range(0,len(expenses)):
    print("Month:", expense+1, "Expenses:",expenses[expense])
    total += expenses[expense]
    # print("Total Expenses: ", total)
print("Total Expenses: ", total)