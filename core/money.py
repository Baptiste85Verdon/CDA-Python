import math

class Money:
    # Constructeur
    def __init__(self, total=0, per_click=1, bonus_per_click=0, per_automation=1, bonus_per_automation=0, initial_interval_automation=10, bonus_interval=0):
        self.total = total
        self.per_click = per_click
        self.bonus_per_click = bonus_per_click
        self.per_automation = per_automation
        self.bonus_per_automation = bonus_per_automation
        self.initial_interval = initial_interval_automation
        self.bonus_interval = bonus_interval


    #GETTER
    def get_total(self):
        return self.total
    def get_per_click(self):
        return self.per_click
    def get_bonus_per_click(self):
        return self.bonus_per_click
    def get_per_automation(self):
        return self.per_automation
    def get_bonus_per_automation(self):
        return self.bonus_per_automation
    def get_initial_interval(self):
        return self.initial_interval
    def get_bonus_interval(self):
        return self.bonus_interval

    #SETTER
    def set_total(self, total):
        self.total = total
    def set_per_click(self, per_click):
        self.per_click = per_click
    def set_bonus_per_click(self, bonus_per_click):
        self.bonus_per_click = bonus_per_click
    def set_per_automation(self, per_automation):
        self.per_automation = per_automation
    def set_bonus_per_automation(self, bonus_per_automation):
        self.bonus_per_automation = bonus_per_automation
    def set_initial_interval(self, initial_interval):
        self.initial_interval = initial_interval
    def set_bonus_interval(self, bonus_interval):
        self.bonus_interval = bonus_interval


    #METHODS
    #AU CLIQUE
    def add_money_click(self):
        self.total += self.per_click + self.bonus_per_click
    def add_bonus_per_click(self, bonus_per_click):
        self.bonus_per_click += bonus_per_click

    #AUTOMATIQUE
    def add_money_automation(self):
        self.total += self.per_automation + self.bonus_per_automation
    def add_bonus_per_automation(self, bonus_per_automation):
        self.bonus_per_automation += bonus_per_automation
    def add_bonus_interval(self, bonus_interval):
        self.bonus_interval += bonus_interval
    def reduce_interval_automation(self, bonus_interval):
        self.initial_interval -= bonus_interval


    #CALCUL MONEY
    def sub_money_buy(self, amount):
        self.total -= amount
    def check_balance(self, amount):
        calcul = self.total - amount
        if self.total < amount and calcul < 0:
            return False
        else:
            return True

