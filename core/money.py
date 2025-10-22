class Money:
    # Constructeur
    def __init__(self, total=0, per_click=1, bonus=0):
        self.total = total
        self.per_click = per_click
        self.bonus = bonus

    #GETTER
    def get_total(self):
        return self.total
    def get_per_click(self):
        return self.per_click
    def get_bonus(self):
        return self.bonus

    #SETTER
    def set_total(self, total):
        self.total = total
    def set_per_click(self, per_click):
        self.per_click = per_click
    def set_bonus(self, bonus):
        self.bonus = bonus

    #METHODS
    def add_money_click(self):
        self.total += self.per_click + self.bonus
    def sub_money_buy(self, amount):
        self.total -= amount
    def add_bonus(self, bonus):
        self.bonus += bonus
    def check_balance(self, amount):
        calcul = self.total - amount
        if self.total < amount and calcul < 0:
            return False
        else:
            return True

