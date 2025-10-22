from xmlrpc.client import Boolean
from core.money import Money


class Augment:
    # Constructeur
    def __init__(self,title, price, bonus_amount, bought: Boolean, money: Money, pos_x, pos_y ):
        self.title = title
        self.price = price
        self.bonus_amount = bonus_amount
        self.bought = bought
        self.money = money
        self.pos_x = pos_x
        self.pos_y = pos_y

    #GETTER
    def get_title(self):
        return self.title
    def get_price(self):
        return self.price
    def get_bonus_amount(self):
        return self.bonus_amount
    def get_bought(self):
        return self.bought
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
        message = f"Vous avez acheté ce bonus pour {self.price} Or \nVotre bonus par clic a augmenté de {self.bonus_amount}"
        if not self.bought:
            if self.money.check_balance(self.price):
                self.money.add_bonus(self.bonus_amount)
                self.money.sub_money_buy(self.price)
                self.bought = True
            else :
                message = f"Vous n'avez pas assez d'argent pour acheter ce bonus\n{self.money.get_total()} Or sur {self.price} nécessaire"
        else :
            message = f"Vous avez déjà acheté ce bonus !"
        return message