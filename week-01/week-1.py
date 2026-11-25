def say_hello():
    print('Hello World')

#parameters gebruiken.
def greet_player(name):
    print(f"Welcome, {name}!")

greet_player ("Steve")
greet_player ("Alex")

def show_player(name, health):
    print(f"Player: {name}")
    print(f"Health: {health}")

show_player("Steve", 100)


#waarden teruggeven met return.
def calculate_damage(attack, defense):
    damage = attack - defense
    return damage

total_damage = calculate_damage(30, 10)

print(total_damage)


#lokale variabelen.
def calculate_price():
    price = 50
    return price

total_price = calculate_price()
print(total_price)


#Functies combineren met bestaande python-code
def check_gold(gold, price):
    if gold >= price:
        return True
    else:
        return False

can_buy = check_gold(100, 50)

if can_buy:
    print("You can buy this item!")
else:
    print("Not enough gold!")


#Naming conventions.
def show_inventory():
    pass
def calculate_price():
    pass
def buy_item():
    pass

