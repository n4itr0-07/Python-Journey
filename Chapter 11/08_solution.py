
#TODO: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is a number that cannot be formed by multiplying two smaller natural numbers. 

#FIXME: For example:
# - 2 is a prime number because the only divisors are 1 and 2.
# - 3 is a prime number because the only divisors are 1 and 3.
# - 4 is not a prime number because it can be divided by 1, 2, and 4 (4 = 2 × 2).

#TODO: Prime numbers are the building blocks of the natural numbers because every natural number greater than 1 can be factored into prime numbers, which is called its prime factorization.

# prime_number = int(input("Enter Your Number : "))

# is_prime = True

# if prime_number > 1:
#     for i in range(2, prime_number):
#         if (prime_number % i) == 0:
#             is_prime = False
#             break

# print(prime_number, "Is Prime Number !")


prime_number = int(input("Enter Your Number : "))

is_prime = True

if prime_number > 1:
    for i in range(2, prime_number):
        if (prime_number % i) == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(prime_number, "is a prime number!")
else:
    print(prime_number, "is not a prime number.")
