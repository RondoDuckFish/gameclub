import random
import time

# Define the key variables and the range for the year
yearlow = 1638  # Year the first casino opened (Il Ridotto)
yearhigh = 2024  # This year

# Introduction and name input
print("Hello and welcome to the world of life!")
name = input("What is your desired name? ")
print(f"Hello, {name}!!! Welcome to life!")

# Loading game with random delay
print("Game is loading...")
time.sleep(random.randint(3, 10))
print("Game loaded!")

# Arriving into the world
cities = [
    "New York", "Tokyo", "Paris", "London", "Berlin", "Sydney",
    "Rio de Janeiro", "Cape Town", "Moscow", "Beijing", "Toronto",
    "Mexico City", "Mumbai", "Singapore", "Istanbul"
]
random_city = random.choice(cities)
current_year = random.randint(yearlow, yearhigh)
print(f"The year is {current_year}.")
print(f"You, {name}, have been born in the city of: {random_city}.")

# Defining variables for physical and mental health
ParentWealth = random.randint(30000, 150000)  # Random wealth for parents
variables = {
    "Physical Health": 100,
    "Sanity": 100,
    "Happiness": 100,
    "Energy": 100,
    "Smartness": 30,
    "Social Life": 100,
    "Wealth": ParentWealth
}

# Random event picker to simulate life events
def random_event():
    events = [
        "Parents died in a car crash.",
        "You were kidnapped at a young age.",
        "You became a prodigy in mathematics.",
        "You met a famous celebrity!",
        "You lost a loved one to an illness.",
        "You inherited a large sum of money!",
        "You decided to pursue a career in art.",
        "You got a scholarship to a prestigious school.",
        "You won the lottery!"
    ]
    return random.choice(events)

# Game loop with random events and changes
def life_simulation():
    age = 0  # Start at age 0
    while age < 100:  # Life continues until age 100
        age += 1
        print(f"\nAge: {age}")
        
        # Simulate random event
        event = random_event()
        print(f"Event: {event}")
        
        # Randomly affect variables based on the event
        if "Parents died" in event:
            variables["Wealth"] -= 10000  # Lose wealth after parents' death
            variables["Sanity"] -= 15  # Sanity might decrease after losing parents
        elif "kidnapped" in event:
            variables["Happiness"] -= 20  # Kidnapping decreases happiness
            variables["Sanity"] -= 30  # Sanity decreases significantly
        elif "mathematics" in event:
            variables["Smartness"] += 10  # Increase smartness
            variables["Happiness"] += 10  # Happiness increases when excelling
        elif "celebrity" in event:
            variables["Social Life"] += 15  # Meeting a celebrity increases social life
            variables["Happiness"] += 10  # Happiness increases
        elif "inheritance" in event:
            variables["Wealth"] += 50000  # Inherit a sum of money
            variables["Happiness"] += 20  # Wealth boosts happiness

        # Display current stats
        print(f"Physical Health: {variables['Physical Health']}")
        print(f"Sanity: {variables['Sanity']}")
        print(f"Happiness: {variables['Happiness']}")
        print(f"Energy: {variables['Energy']}")
        print(f"Smartness: {variables['Smartness']}")
        print(f"Social Life: {variables['Social Life']}")
        print(f"Wealth: ${variables['Wealth']}")
        
        # Adjusting variables to simulate aging
        if variables["Sanity"] <= 0:
            print("You have lost all sanity and can no longer function.")
            break
        
        if variables["Happiness"] <= 0:
            print("You have become too unhappy to continue the game.")
            break
        
        # Simulate a decision to maintain variables (like exercising, socializing, etc.)
        decision = input("Make a decision (1-Exercise, 2-Socialize, 3-Work, 4-Read, 5-Quit): ")
        
        if decision == "1":
            variables["Physical Health"] += 5
            variables["Energy"] -= 10
            variables["Happiness"] += 5
            print("You exercised to improve your physical health.")
        elif decision == "2":
            variables["Social Life"] += 10
            variables["Happiness"] += 5
            variables["Sanity"] += 5
            print("You socialized with friends.")
        elif decision == "3":
            variables["Wealth"] += 5000
            variables["Energy"] -= 15
            variables["Happiness"] -= 5
            print("You worked hard and earned some money.")
        elif decision == "4":
            variables["Smartness"] += 5
            variables["Happiness"] += 10
            print("You read a book to increase your knowledge.")
        elif decision == "5":
            print(f"Thanks for playing, {name}!")
            break
        else:
            print("Invalid decision. Please choose a valid option.")
        
        # Check if the player has run out of vital stats
        if variables["Physical Health"] <= 0 or variables["Energy"] <= 0:
            print("You are too weak to continue. Game Over!")
            break
        
        time.sleep(1)  # Simulate time passing
    
    print("Game Over!")

# Start the life simulation game
life_simulation()
