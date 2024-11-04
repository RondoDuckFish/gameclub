import random
import time

# ASCII art for slot symbols
symbols = {
    '🍒': """
      🍒
     🍒🍒🍒
    """,
    '🍋': """
      🍋
     🍋🍋🍋
    """,
    '🍊': """
      🍊
     🍊🍊🍊
    """,
    '🔔': """
      🔔
     🔔🔔🔔
    """,
    '⭐': """
      ⭐
     ⭐⭐⭐
    """
}

def spin_slots():
    return random.choices(list(symbols.keys()), k=3)

def print_slots(slots):
    print(" | ".join(slots))

def main():
    money = 100  # Starting money
    print("Welcome to the Slot Machine!")
    print(f"You have ${money}.")
    
    while money > 0:
        bet = int(input(f"How much do you want to bet? (You have ${money}): "))
        if bet <= 0 or bet > money:
            print("Invalid bet amount. Try again.")
            continue
        
        print("Spinning...")
        time.sleep(1)  # Pause for effect

        slots = spin_slots()
        print_slots(slots)
        
        if slots[0] == slots[1] == slots[2]:  # All symbols match
            winnings = bet * 10  # Winning payout
            money += winnings
            print(f"🎉 You Win! You earned ${winnings}! Your total money is now ${money}. 🎉")
        else:
            money -= bet  # Losing the bet amount
            print(f"😢 You Lose! Your total money is now ${money}.")
        
        if money == 0:
            print("You're out of money! Game over.")
            break
        
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
