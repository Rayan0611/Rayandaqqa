# 005
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
result = (num1 + num2) * num3

print("The answer is", result)

# 006
start_slices = int(input("How many pizza slices did you start with? "))
eaten_slices = int(input("How many slices have you eaten? "))
left_slices = start_slices - eaten_slices

print("You have", left_slices, "slices left.")

# 007
name = input("Enter your name: ")
age = int(input("Enter your age: "))
new_age = age + 1

print(name, "next birthday you will be", new_age)

# 008
total_bill = float(input("Enter the total bill amount: "))
diners = int(input("Enter the number of diners: "))
amount_per_person = total_bill / diners

print("Each person must pay", amount_per_person)


# 017
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")

# 018
number = int(input("Enter a number: "))
if number < 10:
    print("Too low")
elif 10 <= number <= 20:
    print("Correct")
else:
    print("Too high")

# 019
choice = int(input("Enter 1, 2, or 3: "))
if choice == 1:
    print("Thank you")
elif choice == 2:
    print("Well done")
elif choice == 3:
    print("Correct")
else:
    print("Error message")

# 024
word = input("Enter any word: ")
print(word.upper())

# 025
first_name = input("Enter your first name: ")
if len(first_name) < 5:
    surname = input("Enter your surname: ")
    print((first_name + surname).upper())
else:
    print(first_name.lower())

# 026
word = input("Enter a word: ").lower()
vowels = "aeiou"
if word[0] in vowels:
    pig_latin = word + "way"
else:
    pig_latin = word[1:] + word[0] + "ay"
print(pig_latin)

# 034
print("1) Square\n2) Triangle")
choice = int(input("Enter a number: "))

if choice == 1:
    side = float(input("Enter the length of one side: "))
    print("Area:", side * side)
elif choice == 2:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print("Area:", 0.5 * base * height)
else:
    print("Invalid choice!")

# 035
name = input("Enter your name: ")
print(name * 3)

# 036
name = input("Enter your name: ")
num = int(input("Enter a number: "))
print(name * num)

# 037
name = input("Enter your name: ")
for letter in name:
    print(letter)

# 038
name = input("Enter your name: ")
num = int(input("Enter a number: "))
for _ in range(num):
    for letter in name:
        print(letter)

# 039
num = int(input("Enter a number (1-12): "))
for i in range(1, 13):
    print(num, "x", i, "=", num * i)

# 040
num = int(input("Enter a number below 50: "))
for i in range(50, num - 1, -1):
    print(i)

# 041
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    print(name * num)
else:
    print("Too high" * 3)

# 042
total = 0
for _ in range(5):
    num = int(input("Enter a number: "))
    include = input("Include this number? (yes/no): ")
    if include.lower() == "yes":
        total += num
print("Total:", total)

# 043
direction = input("Count up or down? ").lower()

if direction == "up":
    top = int(input("Enter the top number: "))
    for i in range(1, top + 1):
        print(i)
elif direction == "down":
    bottom = int(input("Enter a number below 20: "))
    for i in range(20, bottom - 1, -1):
        print(i)
else:
    print("I don't understand.")

# 048: 
count = 0

while True:
    name = input("Enter the name of someone to invite: ")
    print(name, "has now been invited.")
    count += 1
    again = input("Do you want to invite someone else? (yes/no): ").lower()
    if again != "yes":
        break

print("Total people coming to the party:", count)

# 049
compnum = 50
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < compnum:
        print("Too low, try again.")
    elif guess > compnum:
        print("Too high, try again.")
    else:
        print(f"Well done, you took {attempts} attempts.")
        break

# 050
while True:
    num = int(input("Enter a number between 10 and 20: "))
    if num < 10:
        print("Too low, try again.")
    elif num > 20:
        print("Too high, try again.")
    else:
        print("Thank you.")
        break
