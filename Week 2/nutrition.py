def main():
    item = input("Item: ").lower().strip()
    calories = match_fruit(item)
    print(f"Calories: {calories}")

def match_fruit(fruit):
    match fruit:
        case "apple":
            return 130
        case "avocado":
            return 50
        case "banana":
            return 110
        case "cantaloupe":
            return 50
        case "grapefruit":
            return 60       
        case "grapes":
            return 90
        case "honeydew melon":
            return 50
        case "lemon":
            return 15
        case "lime":
            return 20
        case "nectarine":
            return 60
        case "orange":
            return 80
        case "peach":
            return 60
        case "pear":
            return 100
        case "pineapple":
            return 50
        case "plums":
            return 70
        case "straberries":
            return 50
        case "sweet cherries":
            return 100
        case "tangerine":
            return 50
        case "watermelon":
            return 80
    
main()