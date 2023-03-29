class VendingMachine(object):

    def __init__(self, water: int, milk: int, coffee: int, recipe: dict, coins: dict) -> None:
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.recipe = recipe
        self.coins = coins
        self.money = self.cal_remaining_money()

    def cal_remaining_money(self):
        return self.coins["quarter"]*0.25 + self.coins["dime"]*0.1 + self.coins["nickle"]*0.05 + self.coins["penny"]*0.01
     
    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Coins: {self.coins}")
        self.money = self.cal_remaining_money()
        print(f"Money: ${round(self.money, 2)}")

    def cal_payment(self, q, d, n, p):
        return float(0.25*q+0.1*d+0.05*n+0.01*p)
    
    def payment(self, drink):

        q = int(input("How many quarters? "))
        d = int(input("How many dimes? "))
        n = int(input("How many nickles? "))
        p = int(input("How many pennies? "))
        payment = self.cal_payment(q,d,n,p)
        if payment < recipe[drink]["money"]:
            print("You don't pay enough money. Sorry I can't make drink.")
            return False, False
        
        d_pay = {
            "quarter": q,
            "dime": d,
            "nickle": n,
            "penny": p,
        }

        return payment, d_pay

    def cal_change(self, drink, payment, d_pay):
        def _cal_change(change, coin, price):
            coin_num = 0
            while coin_num <= self.coins[coin] and change >= price:
                change = round(change - price, 2)
                coin_num += 1
            return coin_num, round(change, 2) 
        
        price = recipe[drink]["money"]
        change = round(payment - price, 2)
        # print(payment)
        # print(price)
        # print(change)
        # add coins temporaly
        for k, v in d_pay.items():
            self.coins[k] += v

        q, change = _cal_change(change, "quarter", 0.25)
        d, change = _cal_change(change, "dime", 0.1)
        n, change = _cal_change(change, "nickle", 0.05)
        p, change = _cal_change(change, "penny", 0.01)
        change_coins = {
            "quarter": q,
            "dime": d,
            "nickle": n,
            "penny": p,
        }
        # print(change_coins)
        # print(change)

        if change == float(0):
            for k, v in change_coins.items():
                self.coins[k] -= v
            print("Don't forget receive change.")
            return True
        
        else:
            for k, v in d_pay.items():
                self.coins[k] -= v
            print("We don't have change. Sorry.")
            return False

    def make_drink(self, drink: str):
        payment, d_pay = self.payment(drink)
        if payment == False:
            return
        b = self.cal_change(drink, payment, d_pay)
        if b == False:
            return
        
        self.water = self.water - self.recipe[drink]["water"]
        self.milk = self.milk - self.recipe[drink]["milk"]
        self.coffee = self.coffee - self.recipe[drink]["coffee"]
        if self.water < 0 or self.milk < 0 or self.coffee < 0:
            self.water = self.water + self.recipe[drink]["water"]
            self.milk = self.milk + self.recipe[drink]["milk"]
            self.coffee = self.coffee + self.recipe[drink]["coffee"]
            return print("We have no ingredient. Sorry.")



if __name__ == "__main__":
    recipe = {"espresso": {"water": 20, "milk": 10, "coffee": 12, "money": 1.2},
              "latte": {"water": 30, "milk": 20, "coffee": 14, "money": 1.7}, 
              "cappuccino": {"water": 10, "milk": 30, "coffee": 17, "money": 2.0}}
    
    coins = {"quarter": 10, "dime": 10, "nickle": 10, "penny": 10}
    vm = VendingMachine(300, 200, 100, recipe, coins)
    on = True
    while on:
        i = input("What would you like? (espresso/latte/cappuccino and report/exit): ").lower()

        if i == "report":
            vm.report()

        elif i == "espresso" or i == "latte" or i == "cappuccino":
            vm.make_drink(i)
        
        elif i == "exit":
            on = False
            print("See you next time. Have a good day!")

        