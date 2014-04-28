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

    #fonction de prise de dégâts#
    def take_damage(self, card):
        self.health -= card.attack

    #Fonction de pioche avec remplissage du deck à partir du cimetière si vide#
    def pickUp(self):
        if len(self.deck) == 0:
            while len(self.cemetery) > 0:
                self.deck.append(self.cemetery[0])
                del self.cemetery[0]
        print("Vous avez pioché : ", self.deck[0].name)
        self.hand.append(self.deck[0])
        del self.deck[0]

    #Fonction de message de début de tour#
    def turn_message(self):
        print("C'est à votre tour, ", self.name, " ! Il vous reste ", self.health)

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
            while self.check_input(saisie) == False:
                saisie = input("Mauvaise saisie, veuillez recommencer")
            if saisie.isnumeric():
                saisie = int(saisie)
                if self.mana >= self.hand[saisie-1].cost:
                    self.mana -= self.hand[saisie-1].cost
                    self.field.append(self.hand[saisie-1])
                    print("Vous avez posé ", self.hand[saisie-1].name)
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
                    print("-(",i,")", end=" ")
                    element.print_card(False)
            print("Voici vos cartes sur le terrain :")
            i = 1
            for element in self.field:
                print("-(",i,")", end= " ")
                element.print_card(False)
            saisie = input("Saisissez le numero du serviteur que vous voulez utiliser, ou \"end\" pour passer")
            target = ""
            if (saisie.isnumeric() and len(self.field) >= int(saisie) >= 0) or (saisie == "end"):
                if saisie.isnumeric():
                    while (saisie.isnumeric() and len(self.field) >= int(saisie) >= 0 and self.field[int(saisie)-1].use == 0) == False and (saisie == "end") == False:
                        saisie = input("Ce serviteur est en repos ou déjà utilisé, choisissez-en un autre")
                    if saisie.isnumeric():
                        choice = int(saisie)
                        saisie = ""
                        while self.field[choice-1].fight_attempt(player2, saisie) == False:
                            saisie = input("Entrez le numéro de la cible")
            else:
                print("Mauvaise saisie")



    #Fonction de vérification de saisie (à utiliser avec l'invocation)#
    def check_input(self, saisie):
        """
        :type self: Player
        :type saisie: str
        """
        if saisie.isnumeric():
            if len(self.hand) >= int(saisie) >= 1:
                return True
            else:
                return False
        else:
            if str(saisie) == "end":
                return True
            else:
                return False

    #fonction d'affichage des morts et clean du field#
    def clean_after(self):
        print("Morts ", self.name, " : ")
        for element in self.field:
            if element.health == 0:
                print("-",element.name)
        i = 0
        while i < len(self.field):
            if self.deck[i].health == 0:
                self.cemetery.append(self.deck[i])
                del self.deck[i]
                while self.deck[i].health == 0:
                    self.cemetery.append(self.deck[i])
                    del self.deck[i]
            i += 1

    #Fonction de tour complet#
    def player_turn(self, player2):
        self.turn_message()
        print("Terrain adverse : ")
        print("------------------------------------------------")
        for element in player2.field:
            element.print_card(False)
        print("------------------------------------------------")
        print("Votre terrain")
        for element in self.field:
            element.print_card(False)
        print("------------------------------------------------")
        self.wake_cards()
        self.pickUp()
        self.initiate_mana()
        self.invoke_cards()
        self.attack_phase(player2)
        self.clean_after()

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
            tmp[i] = word[0].split('\n')[0]
            self.deck.append(Card(tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4]), int(tmp[5]), int(tmp[6]), int(tmp[7])))
        myfic.close()
