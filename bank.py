def main():
    #Prompted not to use separate function due to case being too specific and unlikely to be reused
    greeting = str(input("Greeting: ")).strip().lower()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
