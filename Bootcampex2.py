#058
import random

score = 0

for i in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct!")
        score += 1
    else:
        print("Wrong. The correct answer was", num1 + num2)

print(f"You got {score} out of 5.")

sports = ["Soccer", "Basketball"]
fav_sport = input("Enter your favorite sport: ")
sports.append(fav_sport)
sports.sort()
print("Sorted list of sports:", sports)

#071
sports = ["Soccer", "Basketball"]
fav_sport = input("Enter your favorite sport: ")
sports.append(fav_sport)
sports.sort()
print("Sorted list of sports:", sports)

#072
subjects = ["Math", "English", "Science", "History", "Geography", "Art"]
dislike = input("Which subject do you dislike? ")
if dislike in subjects:
    subjects.remove(dislike)
print("Updated list of subjects:", subjects)

#073
foods = {}
for i in range(1, 5):
    food = input(f"Enter favorite food {i}: ")
    foods[i] = food

print("Your favorite foods:", foods)

remove = int(input("Enter the index of the food to remove: "))
if remove in foods:
    del foods[remove]

sorted_foods = dict(sorted(foods.items()))
print("Updated list:", sorted_foods)

#074
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White"]
start = int(input("Enter a starting number (0-4): "))
end = int(input("Enter an end number (5-9): "))

print("Selected colors:", colors[start:end+1])

#075
numbers = [123, 456, 789, 321]
for num in numbers:
    print(num)

guess = int(input("Enter a three-digit number: "))

if guess in numbers:
    print("Number found at position:", numbers.index(guess) + 1)
else:
    print("That is not in the list.")

#080
first_name = input("Enter your first name: ")
print("Length of first name:", len(first_name))

surname = input("Enter your surname: ")
print("Length of surname:", len(surname))

full_name = first_name + " " + surname
print("Full name:", full_name)
print("Length of full name (including space):", len(full_name))

#085
name = input("Enter your name: ")  
vowels = "aeiouAEIOU"  
count = sum(1 for letter in name if letter in vowels)  

print("Your name has", count, "vowel(s).")  

# 096
matrix = [
    [0, 2, 5, 8],
    [3, 7, 4],
    [1, 6, 9],
    [4, 2, 0]
]

print("2D list created!")

# 097
row = int(input("Enter row number: "))
col = int(input("Enter column number: "))

if row < len(matrix) and col < len(matrix[row]):
    print("Value:", matrix[row][col])
else:
    print("Invalid index.")

# 098
row = int(input("Enter row number to display: "))

if row < len(matrix):
    print("Row:", matrix[row])
    new_value = int(input("Enter a new value to add: "))
    matrix[row].append(new_value)
    print("Updated row:", matrix[row])
else:
    print("Invalid row number.")

# 099
row = int(input("Enter row number: "))
col = int(input("Enter column number: "))

if row < len(matrix) and col < len(matrix[row]):
    print("Current value:", matrix[row][col])
    new_value = int(input("Enter new value: "))
    matrix[row][col] = new_value
    print("Updated row:", matrix[row])
else:
    print("Invalid index.")

# 100
sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}

print("Sales data dictionary created!")

# 101
name = input("Enter name: ")
region = input("Enter region (N/S/E/W): ").upper()

if name in sales and region in sales[name]:
    print("Current sales:", sales[name][region])
    new_sales = int(input("Enter new sales value: "))
    sales[name][region] = new_sales
    print("Updated sales for", name, ":", sales[name])
else:
    print("Invalid name or region.")


# 102
people = {}

for i in range(4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    shoe_size = int(input("Enter shoe size: "))
    people[name] = {"Age": age, "Shoe Size": shoe_size}

search_name = input("Enter a name to look up: ")
if search_name in people:
    print("Age:", people[search_name]["Age"])
    print("Shoe size:", people[search_name]["Shoe Size"])
else:
    print("Name not found.")

# 103
for name, info in people.items():
    print(name, "-", "Age:", info["Age"])







