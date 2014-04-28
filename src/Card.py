__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'

from src import *

class Card:
    #Fonction d'initialisation#
    def __init__(self, name, health, attack, cost, shield, hidden, taunt, use):
        self.name = name
        self.attack = attack
        self.health = health
        self.cost = cost
        self.shield = shield
        self.hidden = hidden
        self.taunt = taunt
        self.use = use

    #Redéfinition de la fonction d'égalité " == " (pas identité) #
    def __eq__(self, other):
         return (self.name == other.name and self.health == other.health and self.attack == other.attack and
                self.cost == other.cost and self.shield == other.shield and self.hidden == other.hidden and
                self.taunt == other.taunt)


    def print_card(self, display_mana=True):
        if self.shield != 0:
            shield = "S:" + str(self.shield)
        else:
            shield = ""

        if self.hidden != 0:
            hidden = "H"
        else:
            hidden = ""

        if self.taunt != 0:
            taunt = "T"
        else:
            taunt = ""

        if display_mana:
            print(self.name, "(", self.attack, "/", self.health, ") :", self.cost, " ", shield, " ", hidden, " ", taunt)

        else:
            print(self.name, " ( ", self.attack, "/", self.health, ") ", shield, " ", hidden, " ", taunt)

    #C#
    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
            self.health -= abs(self.shield)
        else:
            self.health -= damage

    def fight_card(self, card):
        self.hidden = 0
        print("Vous attaquez ", card.get_name(), " (", card.get_attack(), "|", card.get_health(), ") avec ", self.name,
              " (", self.attack, "|", self.health, ")")
        card.take_damage(self.attack)
        self.take_damage(card.attack)

    def fight_attempt(self, player2, idx):
        if idx == 0:
            for element in player2.field:
                if (element.taunt == 1):
                    print("Impossible d'attaquer le joueur, ", element.name, " a la capacité de provocation")
                    return False
                player2.take_damage(self)
                return True
        attackable = True
        for element in player2.field:
            if (element.taunt == 1) and (element != player2.field[idx-1]):
                attackable = False
                print("Vous ne pouvez pas attaquer cette carte, car ", element.name, " a la capacité de provocation !")
        if player2.field[idx-1].hidden == 1:
            attackable = False
            print("Ce monstre est camouflé, vous ne pouvez pas l'attaquer !")
        if attackable:
            self.fight_card(player2.field[idx-1])
            return True
        else:
            return False

