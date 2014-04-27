__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'

import random
from src.Card import Card
from src.PLayer import Player
import time

copie = []
player1 = Player("Alexandre")
player1.load_card_set("decks/deck1.txt")
del player1.deck[0]
for element in player1.deck:
    print(element.name)
print(player1.deck[0].name)
print(player1.deck[4])
