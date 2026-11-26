
#opdracht week-02 winkelmenu
gold = 100
inventory = []

def show_menu():
    print("\n===Fantasy Item shop ===")
    print("1. Buy Sward ( 50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (10 gold)")
    print("4. Show Gold")
    print("5. Show inventory")
    print("6. Exit Shop")

def show_inventory(inventory):
    if len(inventory) == 0:
        for item in inventory:
            print("-", item)

def can_buy(gold, price):
    if gold >= price:
        return True
    else:
        return False

def buy_item(gold, inventory, item_name, price):
    if can_buy(gold, price):
        gold -= price
        inventory.append(item_name)

        print(f"Je hebt een {item_name} gekocht!")
        print(f"Je hebt nog {gold} gold.")
    else:
        print("Niet genoeg gold!")

    return gold

while True:
    show_menu()

    choice = input("Maak je keuze: ")

    match choice:
        case "1":
            gold = buy_item(gold, inventory, "Sward", 50)

        case "2":
            gold = buy_item(gold, inventory, "Shield", 40)

        case "3":
            gold = buy_item(gold, inventory, "Potion", 10 )

        case "4":
            print(f"Je hebt{gold} gold.")

        case "5":
            show_inventory(inventory)

        case "6":
            print("Bedankt voor het bezoeken van de winkel!")

        case _:
            print("Ongeldige keuze.")