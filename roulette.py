import random
import time

# defined roulette wheel with red and black
roulette_wheel = {
    0: "green",
    1: "red", 2: "black", 3: "red", 4: "black", 5: "red", 6: "black", 7: "red", 8: "black", 9: "red", 
    10: "black", 11: "black", 12: "red", 13: "black", 14: "red", 15: "black", 16: "red", 17: "black", 
    18: "red", 19: "black", 20: "red", 21: "black", 22: "red", 23: "black", 24: "red", 25: "black", 
    26: "red", 27: "black", 28: "red", 29: "black", 30: "red", 31: "black", 32: "red", 33: "black", 
    34: "red", 35: "black", 36: "red"
}

# Define bet types
bet_types = ['number', 'color', 'even', 'odd', 'low', 'high']

# fn to display the roulette wheel in ascii
def print_roulette_wheel():
    wheel = """
    +---------------------------------------------------+
    |  0  |  32  |  15  |  19  |  4   |  21  |  2   | 
    |  25  |  17  |  34  |  6   |  27  |  13  |  36  | 
    |  11  |  30  |  8   |  23  |  10  |  5   |  24  | 
    |  16  |  33  |  1   |  20  |  14  |  31  |  9   | 
    |  22  |  18  |  29  |  7   |  28  |  12  |  35  | 
    |  3   |  26  |  0   |
    +---------------------------------------------------+
    """
    print(wheel)
# more like a roulette rectangle lmao
# Function to get player's bet
def get_player_bet():
    print("Welcome to Roulette! You can bet on the following options:")
    print("1. A specific number (0-36)")
    print("2. A color (red or black)")
    print("3. Odd or Even")
    print("4. Low (1-18) or High (19-36)")

    bet_type = input("What would you like to bet on? (number/color/odd/even/low/high): ").lower()
    while bet_type not in bet_types:
        print("Invalid bet type. Please choose a valid option.")
        bet_type = input("What would you like to bet on? (number/color/odd/even/low/high): ").lower()

    if bet_type == 'number':
        bet_value = int(input("Enter a number to bet on (0-36): "))
        while bet_value < 0 or bet_value > 36:
            bet_value = int(input("Please enter a valid number (0-36): "))
    elif bet_type == 'color':
        bet_value = input("Enter a color to bet on (red/black): ").lower()
        while bet_value not in ['red', 'black']:
            bet_value = input("Please enter a valid color (red/black): ").lower()
    elif bet_type in ['odd', 'even']:
        bet_value = bet_type
    elif bet_type in ['low', 'high']:
        bet_value = bet_type

    return bet_type, bet_value

# Function to spin the wheel and return the result
def spin_wheel():
    time.sleep(2)  # Simulate the wheel spinning
    print("Spinning the wheel...")
    result_number = random.randint(0, 36)
    result_color = roulette_wheel[result_number]
    print(f"The ball landed on {result_number} ({result_color})!")
    return result_number, result_color

# Function to calculate the result
def check_bet(bet_type, bet_value, result_number, result_color):
    if bet_type == 'number' and bet_value == result_number:
        return True, 35  # Winning on number pays 35 to 1
    elif bet_type == 'color' and bet_value == result_color:
        return True, 1  # Winning on color pays 1 to 1
    elif bet_type == 'odd' and result_number % 2 == 1:
        return True, 1  # Winning on odd pays 1 to 1
    elif bet_type == 'even' and result_number % 2 == 0 and result_number != 0:
        return True, 1  # Winning on even pays 1 to 1
    elif bet_type == 'low' and 1 <= result_number <= 18:
        return True, 1  # Winning on low pays 1 to 1
    elif bet_type == 'high' and 19 <= result_number <= 36:
        return True, 1  # Winning on high pays 1 to 1
    else:
        return False, 0

# Main game loop
def main():
    balance = 1000  # Starting balance
    print("Welcome to ASCII Roulette!\n")

    while balance > 0:
        print(f"Your current balance is ${balance}")
        print_roulette_wheel()

        # Get player's bet
        bet_type, bet_value = get_player_bet()

        # Get bet amount
        bet_amount = int(input("Enter the amount to bet: $"))
        while bet_amount <= 0 or bet_amount > balance:
            bet_amount = int(input(f"Please enter a valid bet amount (you have ${balance}): $"))

        # Spin the wheel and check the outcome
        result_number, result_color = spin_wheel()
        win, payout = check_bet(bet_type, bet_value, result_number, result_color)

        if win:
            print(f"Congratulations! You won ${bet_amount * payout}!")
            balance += bet_amount * payout
        else:
            print(f"Sorry, you lost ${bet_amount}. Better luck next time!")
            balance -= bet_amount

        # Ask player if they want to play again
        if balance > 0:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break
        else:
            print("You ran out of money! Game over!")
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
