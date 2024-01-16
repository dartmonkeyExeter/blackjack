# blackjack

import tkinter as tk
import random

master = tk.Tk()
master.title("Blackjack")
master.geometry("800x600")
master.resizable(False, False)

sprites_dir = "C:/Users/aaron/Desktop/blackjack-main/cards"
card_back_sprite = tk.PhotoImage(file=f"{sprites_dir}/BACK.png")

suites = ["hearts", "diamonds", "spades", "clubs"]
values = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.sprite = tk.PhotoImage(file=f"{sprites_dir}/{suit[0]}{value}.png")
        self.name = str(value) + " of " + suit

    def __str__(self):
        return self.name

deck = []
player_hand = []
cards_drawn = 0
dealer_hand = []
dealer_cards_drawn = 0

for suit in suites:
    for value in values:
        deck.append(Card(value, suit))

def shuffle_and_draw():
    global deck, player_hand, dealer_hand, cards_drawn

    random.shuffle(deck)

    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    if "A" in [i.value for i in player_hand] and ["J","Q","K"] in [i.value for i in player_hand]:
        print("Blackjack!")

def draw_sprites():
    global cards_drawn, dealer_cards_drawn

    for idx, i in enumerate(player_hand):
        tk.Label(master, image=i.sprite).place(x=275 + (idx * 100) - (cards_drawn * 50), y=400)
    
    for jdx, j in enumerate(dealer_hand):
        if jdx == 0:
            tk.Label(master, image=j.sprite).place(x=275 + (jdx * 100) - (dealer_cards_drawn * 50), y=20)
        else:
            tk.Label(master, image=card_back_sprite).place(x=275 + (jdx * 100) - (dealer_cards_drawn * 50), y=20)

def show_dealer_hand():
    for jdx, j in enumerate(dealer_hand):
        tk.Label(master, image=j.sprite).place(x=275 + (jdx * 100) - (dealer_cards_drawn * 50), y=20)

def draw_card():
    global deck, player_hand, cards_drawn

    player_hand.append(deck.pop())
    cards_drawn += 1
    draw_sprites()

def calculate_hand():
    global player_hand

    for i in player_hand:
        if i.value == "A":
            i.value = 11
        elif i.value in ["J", "Q", "K"]:
            i.value = 10
    
    cur_sum = sum([i.value for i in player_hand])

    if cur_sum > 21:
        for j in player_hand:
            if j.value == 11:
                j.value = 1
                cur_sum -= 10
                if cur_sum <= 21:
                    break
    
    return cur_sum


def stick_cards():
    global deck, dealer_hand, cards_drawn, dealer_cards_drawn, player_hand, draw, stick

    draw.config(state="disabled")
    
    for i in dealer_hand:
        if i.value == "A":
            i.value = 11
        elif i.value in ["J", "Q", "K"]:
            i.value = 10

    while sum([i.value for i in dealer_hand]) < 17:
        dealer_hand.append(deck.pop())
        dealer_cards_drawn += 1
    
    show_dealer_hand()
    
    if sum([i.value for i in dealer_hand]) > 21:
        print("Dealer bust!")
    elif sum([i.value for i in dealer_hand]) > sum([i.value for i in player_hand]):
        print("Dealer wins!")
    elif sum([i.value for i in dealer_hand]) < sum([i.value for i in player_hand]):
        print("Player wins!")
    else:
        print("Draw!")
    
    
    

shuffle_and_draw()
draw_sprites()

draw = tk.Button(master, text="Draw", command=draw_card)
draw.place(x=20, y=500)
stick = tk.Button(master, text="Stick", command=stick_cards)
stick.place(x=740, y=500)

tk.mainloop()
