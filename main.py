# def sum(input):
#     total = 0
#     for val in input:
#         total += val
#     return total
#
# a = [100,200,300]
# print(sum(a))

# def iseven(input):
#     if input == 0:
#         return f"{input} is Undefined"
#     elif input % 2 == 0:
#         return f"{input} is Even"
#     else: return f"{input} is Not Even"
#
# a = 10
# print(iseven(a))

# input_string = "Hello, World!"
# print(input_string[::-1])

# def rev_string(s):
#     result = ""
#     for i in s:
#         result = i + result
#     return result

# input_string = "Hello, World!"
# print(rev_string(input_string))


# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     s = s.replace(",","")
#     print(s)
#     return s == s[::-1]

# input_string = "A man, a plan, a canal, Panama"
# if is_palindrome(input_string):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# def is_vowels(s):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     for i in s:
#         if i in vowels:
#             vowel_count += 1
#     return vowel_count


# input_string = "Hello, World!"
# print(is_vowels(input_string))


# n = 10
# print(n,"Table")
# for i in range(1,11):
#     print(n,'X',i,"=",i*n)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# fact_number = 5
# print(factorial(fact_number))


# number = 5
# factorial = 1
# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# elif number == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1, number + 1):
#         factorial *= i
# print("Factorial of", number, "is", factorial)


# def ispalindrome(input):
#     result = input.replace(" ","").lower()
#     return result == result[::-1]
#
# input_string = '"abcba"'
#
# if ispalindrome(input_string):
#     print(input_string, "is palindrome")
# else:
#     print(input_string, "is not palindrome")

# def fibonacci_seq(n):
#     fib_seq = [0, 1]
#     for i in range(2, n):
#         fib_seq.append(fib_seq[-1] + fib_seq[-2])
#     return fib_seq
#
#
# n = 10
# print("fibonacci sequence: ",fibonacci_seq(n))

# def merged_list(l1,l2):
#     mergedList = []
#     i = j = 0
#     while i<len(l1) and j<len(l2):
#         if l1[i] < l2[j]:
#             mergedList.append(l1[i])
#             i += 1
#         else:
#             mergedList.append(l2[j])
#             j += 1

#     while i<len(l1):
#         mergedList.append(l1[i])
#         i += 1

#     while j<len(l2):
#         mergedList.append(l2[j])
#         j += 1

#     return mergedList

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 6, 8, 10]
# print(merged_list(list1, list2))


# input_string = "Hello World"
# unique_char = set()
# res = ""
# for char in input_string:
#     if char not in unique_char:
#         res = res + char
#         unique_char.add(char)
# print(res)


# def is_perfect_number(number):
#     # if number <= 0:
#     #     return False
#     # divisor_sum = 0
#     # for i in range(1, number):
#     #     if number % i == 0:
#     #         divisor_sum += i
#     #         print(i)
#     # print(divisor_sum)
#     # return divisor_sum == number

#     if number < 2:
#         return False
#     divisors = [i for i in range(1,number) if number % i == 0]
#     return sum(divisors) == number


# input_number = 28
# if is_perfect_number(input_number):
#     print(input_number, "is a perfect number.")
# else:
#     print(input_number, "is not a perfect number.")


# def max_difference(arr):
#     if len(arr) < 2:
#         return
#
#     min_element = arr[0]
#     max_diff = arr[1] - arr[0]
#
#     for i in range(1, len(arr)):
#         max_diff = max(max_diff, arr[i] - min_element)
#         min_element = min(min_element, arr[i])
#
#     return max_diff
#
#
# arr = [2, 7, 9, 5, 1, 3, 5]
# print("Maximum Difference:", max_difference(arr))


# import random
# def guess_game():
#     secret_number = random.randint(1, 100)
#     guesses = []
#     attempts = 0
#
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#
#     while True:
#         try:
#             guess = input("Enter your guess: ")
#             guess = int(guess)
#             if guess < 1 or guess > 100:
#                 print("Please guess a number between 1 and 100.")
#                 continue
#             guesses.append(guess)
#             attempts += 1
#
#             if guess < secret_number:
#                 print("Too low! Try again.")
#             elif guess > secret_number:
#                 print("Too high! Try again.")
#             else:
#                 print(f"Congrats! You got it in {attempts} attempts!")
#                 print(f"Your guesses were: {guesses}")
#                 break
#         except ValueError:
#             print("Please enter a valid number!")
#
# guess_game()

scorecard = ["India|300|8", "Australia|240|9", "South Africa|245|7", "Newzealand|267|9", "England|285|6"]
scorecard.append("Srilanka|257|9")
# Create a dictionary from the scorecard
score_dict = {entry.split('|')[0]: (entry.split('|')[1] + '/' + (entry.split('|'))[2]) for entry in scorecard}
print(score_dict)
for team, score in score_dict.items():
    print(f"{team} : {score}")







