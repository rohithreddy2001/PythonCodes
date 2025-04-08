def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(2))
# print(is_prime(11))  # True
# print(is_prime(15))  # False
# def find_primes(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes
#
# start_range = 0
# end_range = 10
# prime_numbers = find_primes(start_range, end_range)
# print(prime_numbers)
# count = 0
# for i in prime_numbers:
#     count += 1
# print(count, f"prime numbers between {start_range} and {end_range}")

