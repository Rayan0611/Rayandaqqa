import time

# 1) Employee class
class Employee:
    def __init__(self, name, age, id, hours_worked):
        self.name = name
        self.age = age
        self.id = id
        self.hours_worked = hours_worked
        self.rate = 15

    def clock_in(self):
        print(f"{self.name} clocked in at {time.strftime('%H:%M:%S')}")

    def clock_out(self):
        print(f"{self.name} clocked out at {time.strftime('%H:%M:%S')}")

    def calculate_wage(self):
        wage = self.hours_worked * self.rate
        return wage

    def who_am_i(self):
        print("I am an Employee.")

# 2) waitress class inherits Employee
class Waitress(Employee):
    def __init__(self, name, age, id, hours_worked, customers_served):
        super().__init__(name, age, id, hours_worked)
        self.customers_served = customers_served
        self.base_rate = 9

    def calculate_wage(self):
        # Base rate + 5 dollars per customer served
        wage = (self.hours_worked * self.base_rate) + (5 * self.customers_served)
        return wage

    def who_am_i(self):
        print("I am a Waitress.")

# 3) Cashier class inherits Employee
class Cashier(Employee):
    def __init__(self, name, age, id, hours_worked):
        super().__init__(name, age, id, hours_worked)
        self.customers_served_count = 0

    def customers_served(self, count):
        self.customers_served_count = count
        print(f"{self.name} the cashier served {self.customers_served_count} customers.")

    def who_am_i(self):
        print("I am a Cashier.")

    #  Method for custom print output
    def __str__(self):
        return f"CASHIER ({self.name}, {self.id})"

# 4) Customer class
class Customer:
    customers_dict = {}  # class variable dictionary

    def __init__(self, name, order, price):
        self.name = name
        self.order = order
        self.price = price
        # Add to class dictionary
        Customer.customers_dict[self.name] = (self.order, self.price)

    def who_am_i(self):
        print("I am a Customer.")

# A test for the implementation 

# Make an object for a waitress
emp1 = Employee("John", 28, "E001", 40)
emp2 = Employee("Lisa", 32, "E002", 35)

print(f"{emp1.name} earned ${emp1.calculate_wage()} after working {emp1.hours_worked} hours.")
print(f"{emp2.name} earned ${emp2.calculate_wage()} after working {emp2.hours_worked} hours.")

print()

# Make three customers and add their info to the customer dictionary
cust1 = Customer("Alice", "Burger", 12.50)
cust2 = Customer("Bob", "Pizza", 15.00)
cust3 = Customer("Charlie", "Salad", 10.00)

print("Customer dictionary:")
print(Customer.customers_dict)
cust1.who_am_i()
print()

# Create one waitress and show her work info
waitress = Waitress("Megan", 25, "W001", 30, customers_served=20)
waitress.clock_in()
print(f"{waitress.name} earned ${waitress.calculate_wage()} as a waitress.")
waitress.clock_out()
waitress.who_am_i()
print()

# Create one cashier to show how many customers she helped and print her name and ID nicely
cashier = Cashier("Suzy", 27, "C001", 38)
cashier.customers_served(50)
print(cashier)
cashier.who_am_i()
