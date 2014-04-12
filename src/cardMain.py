__author__ = 'Julien Leseine'

import random

#-------------------------------------------------------------------------#

class Card:

    #variables
    name = 0
    health = 0
    attack = 0
    cost = 0

    #A#
    def __init__(self, _name, _health, _attack, _cost):
        self.name = _name
        self.health = _health
        self.attack = _attack
        self.cos = _cost

    #B#
    def print(self, DiplayMana=True):
        if DiplayMana == True:
            print(self.name, " ( ", self.atack, "/", self.health, ") : ", self.mana)

        else:
            print(self.name, " ( ", self.atack, "/", self.health, ")")

    #C#
    def fight(self, Card):
        self.health -= Card.attack

    #D#
    def isAlive(self):
        if self.health <= 0:
            return True

        else:
            return False

    #E#
    def loadCardSet(name):
        #name attack health mana
        myfic = open(name, "r", 1)
        deck = []
        tmp = {}
        i = 0
        for line in myfic:
            word = line.partition(" ")
            tmp[0] = word[0]
            word = word[2].partition(" ")
            tmp[1] = word[0]
            word = word[2].partition(" ")
            tmp[2] = word[0]
            word = word[2].partition(" ")
            tmp[3] = word[0].split('\n')[0]
            deck.append(Card(tmp[0], tmp[2], tmp[1], tmp[3]))
            i = i + 1
        myfic.close()
        return deck



#-------------------------------------------------------------------------#
#F#
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
            print(self.hand[i].name , " ", i)
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
        self.mana = va#

    #L#
    def playTurn(self, player1, player2):
