import random
import sys

# creating the playing deck of cards
class shoe:
    def __init__(self, num_of_decks):
        self.num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.one_deck = self.num * 4
        self.shoe = self.one_deck * num_of_decks
    
    def choose(self):
        return self.shoe.pop() #pop() modifies the original list
    
    def shuffle(self):
        random.shuffle(self.shoe)
        
class dealer:
    def __init__(self,shoe):
        self.current_cards = []
        self.shoe = shoe

    def draw_card(self):
        card_chosen = self.shoe.choose()
        self.current_cards.append(card_chosen)

class player:
    def __init__(self, shoe):
        self.current_cards = []
        self.shoe = shoe
    
    def draw_card(self):
        card_chosen = self.shoe.choose()
        self.current_cards.append(card_chosen)


card_value = {1:'Ace', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'Jack', 12:'Queen', 13:'King'}
pictures = ['Jack', 'Queen', 'King']
bet_amt = 0

def main():
    welcome = input('Welcome to the table. Fortune favors the bold-will you take your seat? \nY. Yes \nN. No \n').upper().strip()
    if welcome == 'Y':
        game_begin()
    
    else:
        sys.exit()

def game_begin():

    playing_cards = shoe(3)
    playing_cards.shuffle()
    P1 = player(playing_cards)
    Dealer = dealer(playing_cards)

    P1.draw_card()
    show_p(P1)
    Dealer.draw_card()
    show_d(Dealer)
    P1.draw_card()
    show_p(P1)
    calculate_p(P1)
    ask(P1)
    Dealer.draw_card()
    show_d(Dealer)
    calculate_d(Dealer)

def show_p(p):
    last_card = p.current_cards[-1]
    print(f"Dealer deals you {card_value[last_card]} ")

def show_d(d):
    last_card = d.current_cards[-1]
    print(f"Dealer got {card_value[last_card]} ")

# Needed guidance to solve all possible cases for Ace
def calculate(s):
    totals = [0]  # start with one possible total

    for card in s.current_cards:
        new_totals = []

        for total in totals:
            if card_value[card] in pictures:
                new_totals.append(total + 10)
            elif card == 1:  # Ace
                new_totals.append(total + 1)
                new_totals.append(total + 11)
            else:
                new_totals.append(total + card_value[card])

        totals = new_totals

    # remove duplicates
    totals = list(set(totals))
    return totals

def calculate_p(p):

    valid_totals = calculate(p)
    valid_totals = [t for t in valid_totals if t <= 21]
    if valid_totals == []:
        sys.exit("Player Busted")
    else:
        result = "/".join(map(str,valid_totals))
        print(f"You got {result}")

def calculate_d(x):
    while True:
        total = calculate(x)
        total = [t for t in total if t <= 21]

        if total:
            if max(total) < 17:
                x.draw_card()
                show_d(x)
                total = calculate(x)
                
            else:
                break
        else:
            sys.exit("Dealer Busted")

    print(f"Dealer got {max(total)}")

def ask(u):
    print("--------------------------")
    while input("1. Hit \n2. Stand\n").strip() != "2":
        print("--------------------------")
        u.draw_card()
        calculate_p(u)

main()
