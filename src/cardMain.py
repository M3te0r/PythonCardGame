__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'

import random
from src.Card import Card
from src.PLayer import Player
import time

print("Bienvenue ! Entrez vos noms !")
name1 = input("Joueur 1 ?")
name2 = input("Joueur 2 ?")

player1 = Player(name1)
player2 = Player(name2)
player1.load_card_set("decks/deck1.txt")
player2.load_card_set("decks/deck1.txt")

for element in player1.deck:
    element.print_card()

while player1.health > 0 and player2.health > 0:
    player1.player_turn(player2)
    if player2.health > 0 :
        player2.player_turn(player1)
if player1.health <= 0:
    print(player2.name," gagne !")
else:
    print(player1.name," gagne !")

