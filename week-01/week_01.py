naam = input("wat is je naam?")
gold = 100
inventory = []

while True:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    keuze = input("Maak een keuze:")

    if keuze == "1":
        if gold >= 50:
            gold -= 50
            inventory.append("sword")
            print("Sword gekocht!")
        else:
            print("Niet genoeg gold!")

    elif keuze == "5":
        print("Inventory:", inventory)

    elif keuze == "6":
        print("Bedankt voor je bezoek", naam)
        print("Gold over:", gold)
        break