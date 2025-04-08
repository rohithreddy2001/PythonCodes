indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

Dish = input("Enter a dish name: ")

if Dish in indian:
    print(Dish,"is available in Indian")
elif Dish in chinese:
    print(Dish,"is available in Chinese")
elif Dish in italian:
    print(Dish,"is avialable in Italian")
else:
    print("Sorry! We don't have",Dish)