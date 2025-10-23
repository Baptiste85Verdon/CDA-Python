from xmlrpc.client import Boolean

from pyexpat.errors import messages

from core.money import Money


class Augment:
    instances = []
    # Constructeur
    def __init__(self,augment_id ,title, price, bonus_type, bonus_amount, bought: Boolean, time_bought, max_time_bought, condition_amount, condition_id, condition_type, money: Money, pos_x, pos_y ):
        self.augment_id = augment_id
        self.title = title
        self.price = price
        self.bonus_type = bonus_type
        self.bonus_amount = bonus_amount
        self.bought = bought
        self.time_bought = time_bought
        self.max_time_bought = max_time_bought
        self.condition_amount = condition_amount
        self.condition_id = condition_id
        self.condition_type = condition_type
        self.money = money
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.instances.append(self)


    #GETTER
    def get_augment_id(self):
        return self.augment_id
    def get_title(self):
        return self.title
    def get_price(self):
        return self.price
    def get_bonus_type(self):
        return self.bonus_type
    def get_bonus_amount(self):
        return self.bonus_amount
    def get_time_bought(self):
        return self.time_bought
    def get_bought(self):
        return self.bought
    def get_max_time_bought(self):
        return self.max_time_bought
    def get_condition_amount(self):
        return self.condition_amount
    def get_condition_id(self):
        return self.condition_id
    def get_condition_type(self):
        return self.condition_type
    def get_money(self):
        return self.money
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y

    #SETTER
    def set_title(self, title):
        self.title = title
    def set_price(self, price):
        self.price = price
    def set_bonus_amount(self, bonus_amount):
        self.bonus_amount = bonus_amount
    def set_pos_x(self, pos_x):
        self.pos_x = pos_x
    def set_pos_y(self, pos_y):
        self.pos_y = pos_y

    #METHODS

    def buy_bonus(self):
        #EN FONCTION DU TYPE -> DIFFERENT MESSAGE ET METHODE D'ACTION
        #self.bonus_type == 1 --> bonus_per_click
        #self.bonus_type == 2 --> bonus_per_automation
        #self.bonus_type == 3 --> bonus_interval

        if self.time_bought < self.max_time_bought: #Si pas déjà acheté
            if self.money.check_balance(self.price): #Si assez de money
                # Si c'est un bonus par clic
                if self.bonus_type == 1:
                    message = f"Vous avez acheté ce bonus pour {self.price} Or \nVotre bonus par clic a augmenté de {self.bonus_amount} \nIl est maintenant niveau {self.time_bought+1} sur {self.max_time_bought}"
                    self.money.add_bonus_per_click(self.bonus_amount)
                # Si c'est un bonus par clic automatique
                elif self.bonus_type == 2:
                    message = f"Vous avez acheté ce bonus pour {self.price} Or \nVotre bonus par clic automatique a augmenté de {self.bonus_amount} \nIl est maintenant niveau {self.time_bought+1} sur {self.max_time_bought}"
                    self.money.add_bonus_per_automation(self.bonus_amount)
                # Si c'est un bonus pour réduire l'interval
                else:
                    message = f"Vous avez acheté ce bonus pour {self.price} Or \nL'interval de vos clics automatiques à réduit de {self.bonus_amount} \nIl est maintenant niveau {self.time_bought+1} sur {self.max_time_bought}"
                    self.money.reduce_interval_automation(self.bonus_amount)
                self.money.sub_money_buy(self.price)
                self.bought = True
                self.time_bought += 1

            else :
                message = f"Vous n'avez pas assez d'argent pour acheter ce bonus\n{self.money.get_total()} Or sur {self.price} nécessaire"
        else :
            message = f"Ce bonus est déjà au niveau max ! \nNiveau {self.time_bought} sur {self.max_time_bought}"
        return message

    def check_condition(self):
        message = ''
        #EN FONCTION DU TYPE -> DIFFERENT MESSAGE ET METHODE D'ACTION
        # self.condition_type == 1 --> augment
        # self.condition_type == 2 --> per_click
        # self.condition_type == 3 --> per_automation
        # self.condition_type == 4 --> interval
        # On vérifie si notre bonus possède une condition et son type
        if self.condition_type == 1:
            # Si condition 1, on parcourt la liste des bonus créés
            for augment in self.instances :
                # Si l'id du bonus correspond avec celui de la condition
                if augment.get_augment_id() == self.condition_id:
                    # On compare le niveau de ce bonus comparé à la condition
                    if augment.get_time_bought() >= self.condition_amount:
                        # Si il est supérieur ou égal, on effectue l'achat du bonus en appelant la fonction
                        message = self.buy_bonus()
                    else:
                        message = f"Les conditions ne sont pas remplies pour acheter ce bonus.\nIl vous faut acheter le bonus suivant encore {self.condition_amount-augment.get_time_bought()} fois.\n'{augment.get_title()}'"

        elif self.condition_type == 2:
            # Si condition 2, on récupère le montant généré par clic
            if self.money.get_per_click()+self.money.get_bonus_per_click() >= self.condition_amount:
                message = self.buy_bonus()
            else:
                message = f"Les conditions ne sont pas remplies pour acheter ce bonus. \nIl vous faut avoir un montant de {self.condition_amount} Or par clic"
        elif self.condition_type == 3:
            # Si condition 3, on récupère le montant généré par clic automatique
            if self.money.get_per_automation()+self.money.get_bonus_per_automation() >= self.condition_amount:
                message = self.buy_bonus()
            else:
                message = f"Les conditions ne sont pas remplies pour acheter ce bonus. \nIl vous faut avoir un montant de {self.condition_amount} Or par clic automatique"
        elif self.condition_type == 4:
            # Si condition 4, on récupère l'interval entre les générations automatique
            if self.money.get_initial_interval()-self.money.get_bonus_interval() <= self.condition_amount:
                message = self.buy_bonus()
            else:
                message = f"Les conditions ne sont pas remplies pour acheter ce bonus. \nIl vous faut avoir un temps entre chaque clic automatique inférieur ou égal à {self.condition_amount}"
        elif self.condition_type == 0:
            message = self.buy_bonus()
        return message


