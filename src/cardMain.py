__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'

import random
from src.Card import Card
from src.PLayer import Player
import time

copie = []
player1 = Player("Alexandre")
player1.load_card_set("decks/deck1.txt")

word = "kaka|lol"
word = word.split("|")[0]
print(word)

while len(player1.deck) > 0:
    del player1.deck[0]

for element in player1.deck:
    element.print_card()

print(player1.deck[1].name)
print(player1.deck[1].attack)
print(player1.deck[1].health)
print(player1.deck[1].cost)
print(player1.deck[1].shield)
print(player1.deck[1].hidden)
print(player1.deck[1].taunt)
print(player1.deck[1].use)
