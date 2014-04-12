__author__ = 'Julien'


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