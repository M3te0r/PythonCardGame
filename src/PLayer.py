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

    #Fonction de pioche avec remplissage du deck à partir du cimetière si vide#
    def pickUp(self):
        if len(self.deck) == 0:
            while len(self.cemetery) > 0:
                self.deck.append(self.cemetery[0])
                del self.cemetery[0]
        print("Vous avez pioché : ", self.deck[0].print_card())
        self.hand.append(self.deck[0])
        del self.deck[0]

    #Fonction de message de début de tour#
    def turn_message(self):
        print("C'est à votre tour, ", self.name, " !")

    #Retirer le repos d'invocation pour tous les monstres présents (à faire avant les invocations)#
    def wake_cards(self):
        for element in self.field:
            element.use = 1

    #Fonction de restauration et augmentation du mana#
    def initiate_mana(self):
        if self.turn_mana  < self.max_mana:
            self.turn_mana += 1
        self.mana = self.turn_mana

    #Invocation des serviteurs#
    def invoke_cards(self):
        saisie = ""
        while saisie != "end":
            print("Voici les serviteurs présents dans votre main. Montant de mana : ", self.mana)
            i = 1
            for element in self.hand:
                print("-(",i,")", end=' ')
                element.print_card()
                i += 1
            saisie = input("Saisissez le numero du serviteur que vous desirez invoquer, ou \"end\" pour passer")
            while self.check_input() == False:
                saisie = input("Mauvaise saisie, veuillez recommencer")
            if saisie.isnumeric():
                saisie = int(saisie)
                if self.mana >= self.hand[saisie-1]:
                    self.field.append(self.hand[saisie-1])
                    print("Vous avez posé ", self.hand[saisie-1])
                    del self.hand[saisie-1]
                else:
                    print("Pas assez de mana pour innvoquer cette carte")

    #Fonction de phase d'attaque#
    def attack_phase(self, player2):
        print("Phase d'attaque !")
        saisie = ""
        while saisie != "end":
            print("Voici les cibles possibles : ")
            print ("-(0) ", player2.name)
            i = 0
            for element in player2.field:
                    print("-(",i,") ", element.print_card)
            print("Voici vos cartes sur le terrain :")
            i = 0
            for element in self.field:
                print("-(",i,") ", element.print_card)
            saisie = input("Saisissez le numero du serviteur que vous voulez utiliser, ou \"end\" pour passer")
            if (saisie.isnumeric() and len(self.field) >= saisie >= 0) or (saisie == "end"):
                if saisie.isnumeric():





    #Fonction de vérification de saisie (à utiliser avec l'invocation)#
    def check_input(self, saisie):
        """
        :type self: Player
        :type saisie: str
        """
        if saisie.isnumeric():
            if len(self.hand) >= saisie >= 1:
                return True
            else:
                return False
        else:
            if str(saisie) == "end":
                return True
            else:
                return False

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
            word = line.partition("|")
            while i < 7:
                tmp[i] = word[0]
                word = word[2].partition("|")
                i += 1
            print(word)
            tmp[i] = word[0].split('\n')[0]
            self.deck.append(Card(tmp[0], tmp[2], tmp[1], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7]))
        myfic.close()
