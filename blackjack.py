import random
import time

# ASCII art for cards
suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [(rank, suit) for rank in ranks for suit in suits]

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card, _ in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11
        else:
            value += int(card)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_hand(hand, title):
    hand_str = ', '.join(f"{rank}{suit}" for rank, suit in hand)
    print(f"{title}: {hand_str} (Value: {calculate_hand_value(hand)})")

def main():
    print("Welcome to Blackjack!")
    
    # Initialize deck and hands
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    while True:
        print_hand(player_hand, "Your Hand")
        print(f"Dealer's Hand: {dealer_hand[0][0]}{dealer_hand[0][1]}, ?")
        
        player_value = calculate_hand_value(player_hand)
        
        if player_value == 21:
            print("🎉 BlackJack! You win! 🎉")
            return
        elif player_value > 21:
            print("💔 You bust! Dealer wins.")
            return
        
        action = input("Do you want to Hit or Stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    # Dealer's turn
    print_hand(dealer_hand, "Dealer's Hand")
    dealer_value = calculate_hand_value(dealer_hand)
    
    while dealer_value < 17:
        dealer_hand.append(deal_card(deck))
        print_hand(dealer_hand, "Dealer's Hand")
        dealer_value = calculate_hand_value(dealer_hand)

    # Determine the winner
    print(f"\nFinal Results:\nYour Value: {player_value}\nDealer's Value: {dealer_value}")
    if dealer_value > 21 or player_value > dealer_value:
        print("🎉 You win! 🎉")
    elif player_value < dealer_value:
        print("💔 Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
