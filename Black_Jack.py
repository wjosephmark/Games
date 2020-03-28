import random

dealer_cards = []
player_cards = []

player_total = sum(player_cards)
dealer_total = sum(dealer_cards)

player_move_array = ['placeholder']

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print(" ")
        print("The visible dealer card is:", dealer_cards[0])

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))

if len(dealer_cards) == 2:
    print("Your hand is:", player_cards)
    print(" ")

def hit_or_stay():
    global player_move_array

    def player_move_func():
        player_move_array.pop()
        player_move = input("Would you like to hit or stay? -> ")
        player_move_array.append(player_move)

    def who_won():
        if sum(dealer_cards) > sum(player_cards):
            print(" ")
            print("Dealer total was:", sum(dealer_cards))
            print("Dealer won!  Better luck next time!")
            exit()

        if sum(dealer_cards) < sum(player_cards):
            print(" ")
            print("Dealer total was:", sum(dealer_cards))
            print("You won!  Great job!")
            exit()
    
    player_move_func()
    
    if "hit" in player_move_array:
        player_cards.append(random.randint(1, 11))
        if sum(player_cards) > 21:
            print("You busted, Dealer wins!")
            exit()
        print("Your hand is now:", player_cards)
    elif "stay" in player_move_array:
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.randint(1, 11))

        if sum(dealer_cards) > 21:
             print("The Dealer busted!  You win!")
             exit()
        
        who_won()

    else:
        print("That is not an option.")
        hit_or_stay()

while sum(player_cards) < 22:
    hit_or_stay()