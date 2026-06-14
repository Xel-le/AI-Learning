def main():
    item = input("Item: ").lower().strip()
    if item in FRUITS:
            print(f"Calories: {FRUITS[item]}")

FRUITS = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "kiwifruit": 90,
        "cantaloupe": 50,
        "grapefruit": 60,   
        "grapes": 90,
        "honeydew melon": 50,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
}

main()