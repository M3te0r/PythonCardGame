__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'

import random


class Player:

    #variables
    health = 30
    mana = 1
    hand = []
    field = []

    def __init__(self, deck):
        self.health = 30
        self.attack = 1
        for i in range(4):
            self.hand.append( deck[random.randint( 0, len(deck) )] )

    #G#
    def pickUp(self, deck):
        self.hand.append(deck[random.randint(0, len(deck))])

    #H#
    def deploy(self):
        print("Choisissez une carte a deployer")
        for i in self.hand:
            print(self.hand[i].name, " ", i)
            reponse = input("entrez le numero de la carte:")
            if reponse.isnumeric():
                self.field.append(self.hand[reponse])
                self.hand.remove(reponse)

    #I#
    def clean(self):
        for i in self.field:
            self.field.remove(i)

    #j#
    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True

    #K#
    def setMana(self, value):
        self.mana = value
