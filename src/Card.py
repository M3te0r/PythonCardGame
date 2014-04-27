__author__ = 'Alexandre Fayette/Julien Leseine/Mathieu Pequin'


class Card:
    #Fonction d'initialisation#
    def __init__(self, name, health, attack, cost, shield, hidden, taunt, use):
        self.name = name
        self.health = health
        self.attack = attack
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

    ######################  GETTERS ##################
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_cost(self):
        return self.cost

    def get_shield(self):
        return self.shield

    def get_hidden(self):
        return self.hidden

    def get_taunt(self):
        return self.taunt

    ################### SETTERS #####################
    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.name = health

    def set_attack(self, attack):
        self.name = attack

    def set_cost(self, cost):
        self.name = cost

    def set_shield(self, shield):
        self.name = shield

    def set_hidden(self, hidden):
        self.name = hidden

    def set_taunt(self, taunt):
        self.name = taunt

    ##################### OTHERS #################

    def print(self, display_mana=True):
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

    def fight(self, card):
        self.hidden = 0
        print("Vous attaquez ", card.get_name(), " (", card.get_attack(), "|", card.get_health(), ") avec ", self.name,
              " (", self.attack, "|", self.health, ")")
        card.take_damage(self.attack)
        self.take_damage(card.attack)

    def can_attack(self):
        return self.use

    def fight_attempt(self, ennemy_field, card):
        attackable = True
        for element in ennemy_field:
            if (element.taunt == 1) and (element != card):
                attackable = False
                print("Vous ne pouvez pas attaquer cette carte, car ", element.name, " a la capacité de provocation !")
        if card.hidden == 1:
            attackable = False
            print("Ce monstre est camouflé, vous ne pouvez pas l'attaquer !")
        if attackable:
            self.fight(card)
            return True
        else:
            return False

    #D#
    def is_alive(self):
        if self.health <= 0:
            return True

        else:
            return False

    #E#
    def load_card_set(filename):
        """
        :param filename: nom du fichier
        :type filename: str
        """
        #name attack health mana
        myfic = open(filename, "r", 1)
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
            i += 1
        myfic.close()
        return deck
