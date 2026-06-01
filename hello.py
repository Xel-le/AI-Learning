# My first Python program
def main():
    fullName = input("Input your full name: ").strip().title()
    if " " in fullName:
        firstName, lastName = fullName.split(" ", 1)
        if firstName in {"Arnela", "Arnella", "Ornela", "Ornella"} and lastName == "Loktionova":
            print(f"I love you, {firstName} <3")
        else:
            print(f"Hello, {fullName}!")
    else:
        print(f"Hello, {fullName}!")

main()
        