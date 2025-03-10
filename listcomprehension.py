fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1
uppercased_fruits = [fruit.upper() for fruit in fruits]
print("Uppercased fruits:", uppercased_fruits)

# Exercise 2
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:", capitalized_fruits)

# Exercise 3
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit if letter in "aeiouAEIOU") > 2]
print("Fruits with more than two vowels:", fruits_with_more_than_two_vowels)

# Exercise 4
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit if letter in "aeiouAEIOU") == 2]
print("Fruits with only two vowels:", fruits_with_only_two_vowels)

# Exercise 5
fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print("Fruits with more than 5 characters:", fruits_with_more_than_five_characters)

# Exercise 6
fruits_with_exactly_five_characters = [fruit for fruit in fruits if len(fruit) == 5]
print("Fruits with exactly 5 characters:", fruits_with_exactly_five_characters)

# Exercise 7
fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]
print("Fruits with less than 5 characters:", fruits_with_less_than_five_characters)

# Exercise 8
fruit_name_lengths = [len(fruit) for fruit in fruits]
print("Fruit name lengths:", fruit_name_lengths)

# Exercise 9
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit.lower()]
print("Fruits with Letter 'a':", fruits_with_letter_a)

# Exercise 10
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# Exercise 11
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)

# Exercise 12
positive_numbers = [num for num in numbers if num > 0]
print("Positive numbers:", positive_numbers)

# Exercise 13
negative_numbers = [num for num in numbers if num < 0]
print("Negative numbers:", negative_numbers)

# Exercise 14
numbers_with_two_or_more_digits = [num for num in numbers if abs(num) >= 10]
print("Numbers with two or more digits:", numbers_with_two_or_more_digits)

# Exercise 15
numbers_squared = [num ** 2 for num in numbers]
print("numbers squared:", numbers_squared)

# Exercise 16
odd_negative_numbers = [num for num in numbers if num < 0 and num % 2 != 0]
print("Odd negative numbers:", odd_negative_numbers)

# Exercise 17
numbers_plus_5 = [num + 5 for num in numbers]
print("Numbers plus 5:", numbers_plus_5)

# Bonus
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in numbers if is_prime(num)]
print("prime numbers:", primes)
