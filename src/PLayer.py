__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'

import random
from src.Card import Card

class Player:

    def __init__(self, name):
        self.name = name
        self.health = 30
        self.mana = 0
        self.turn_mana = 0
        self.max_mana = 10
        self.hand = []
        self.field = []
        self.deck = []
        self.cemetery = []

    #Fonction de pioche#
    def pickUp(self):
        self.hand.append(self.deck[0])
        del self.deck[0]

    #Fonction de message de début de tour#
    def turn_message(self):
        print("C'est à votre tour, ", self.name, " !")

    #Affichage du field#
    def print_field(self):
        for card in self.field:
            card.print_card(False)

    def deploy(self):
        print("Choisissez une carte a deployer")
        for i in self.hand:
            print(self.hand[i].name, " ", i)
            reponse = input("entrez le numero de la carte:")
            if reponse.isnumeric():
                self.field.append(self.hand[reponse])
                self.hand.remove(reponse)

    def load_card_set(self, filename):
        """
        :param filename: nom du fichier
        :type filename: str
        """
        #name attack health mana
        myfic = open(filename, "r", 1)
        tmp = {}
        for line in myfic:
            i = 0
            while i < 7:
                word = line.partition("|")
                tmp[i] = word[0]
                i += 1
            tmp[7] = word[0].split('\n')[0]
            self.deck.append(Card(tmp[0], tmp[2], tmp[1], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7]))
        myfic.close()
