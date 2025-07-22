import random

# 1. Ask user their name
name = input("Welcome agent, what is your name?\n")

# 2. Lists of adjectives and animals (6 items each)
adjectives = ["Sneaky", "Brave", "Fuzzy", "Silent", "Swift", "Clever"]
animals = ["Otter", "Panther", "Fox", "Owl", "Tiger", "Lynx"]

# 3. Randomly choose one adjective and one animal
random_adjective = random.choice(adjectives)
random_animal = random.choice(animals)

# 4. Randomly choose a lucky number from 1 to 99
lucky_number = random.randint(1, 99)

# 5. Combine them into a codename
codename = random_adjective + " " + random_animal

# 6. Print the final message
print("\n🔍 Agent " + name + ", your codename is: " + codename)
print("🍀 Your lucky number is: " + str(lucky_number))