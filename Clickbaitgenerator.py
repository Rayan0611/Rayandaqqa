import random

# Word lists
nouns = ['Athlete', 'Clown', 'Shovel', 'Robot']
places = ['house', 'attic', 'school', 'basement']
provinces = ['Ontario', 'BC', 'Alberta', 'Nova Scotia']
when = ['later this year', 'soon', 'later today', 'right now']
object_pronouns = ['her', 'him', 'them']
possessive_pronouns = ['hers', 'his', 'theirs']
personal_pronouns = ['She', 'he', 'they']

def preset1():
    return f"You won't believe what this {random.choice(nouns)} did in a {random.choice(places)}!"

def preset2():
    return f"{random.choice(personal_pronouns)} moved to {random.choice(provinces)} and changed {random.choice(possessive_pronouns)} life {random.choice(when)}!"

def preset3():
    return f"Why this {random.choice(nouns)} is trending {random.choice(when)} will shock {random.choice(object_pronouns)}."

def preset4():
    return f"The hidden secret about {random.choice(places)} in {random.choice(provinces)}!"

def preset5():
    return f"{random.choice(personal_pronouns)} discovered a {random.choice(nouns)} {random.choice(when)} — and you need to see it!"

# To generate Randoms headlines 
def generate_headline():
    presets = [preset1, preset2, preset3, preset4, preset5]
    return random.choice(presets)()

# To generate multiple of them
def generate_multiple_headlines(num):
    if num > 0:
        return [generate_headline() for _ in range(num)]
    else:
        raise ValueError("Number of headlines must be positive.")

try:
    num_headlines = int(input("Enter the number of headlines to generate: "))
    headlines = generate_multiple_headlines(num_headlines)
    for headline in headlines:
        print(headline)
except ValueError:
    print("Invalid input. Please enter a positive integer.")
