# months = ['January', 'February', 'March', 'April', 'May']
# monthly_expenses = [2200, 2350, 2600, 2130, 2190]
#
# # 1. In Feb, how many dollars you spent extra compare to January?
# print(f"Extra amount spent for feb month compare to jan: {monthly_expenses[1] - monthly_expenses[0]}")
#
# # 2. Find out your total expense in first quarter (first three months) of the year.
# total_expenses = 0
# for i in range(3):
#      total_expenses += monthly_expenses[i]
# print(f"First quarter expenses: {total_expenses}")
#
# # 3. Find out if you spent exactly 2000 dollars in any month
# def is_spent(months, expenses):
#     for month, expense in zip(months, expenses):
#         if expense == 2000:
#             return f"{month}: {expense}"
#     return False
#
# print(is_spent(months, monthly_expenses))
#
# # June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#
# months.insert(5, 'June')
# monthly_expenses.insert(5, 1980)
#
# print(f"{months[5]}: {monthly_expenses[5]}")
#
#  # You returned an item that you bought in a month of April and
#  # got a refund of 200$. Make a correction to your monthly expense list
#  # based on this
#
# monthly_expenses[3] = monthly_expenses[3] - 200
#
# print(monthly_expenses[3])
#
# print("Updated monthly expenses list")
# for month, expense in zip(months, monthly_expenses):
#     print(f"{month}: {expense}")

# # Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
#
# max_number = int(input("Enter max odd limit: "))
# odd_list = []
# for i in range(1, max_number):
#     if i % 2 != 0:
#         odd_list.append(i)
# print(odd_list)

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list

print(f"Length of the list: {len(heros)}")

# 2. Add 'black panther' at the end of this list

heros.append('black panther')
print('black panther' in heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros.remove('black panther')
heros.insert(3, 'black panther')

for hero in heros:
    print(hero)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros[1:3] = ['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print("\nHeros list sorted\n")
heros_sorted = sorted(heros)
for hero in heros_sorted:
    print(hero)











