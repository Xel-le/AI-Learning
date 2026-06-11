def main():
    amount_due = int(50)
    print(f"Amount due: {amount_due}")
    while True:
        while True:
            insert_amount  = int(input("Insert coin: "))
            if insert_amount in [5, 10, 25]:
                break
            print(f"Amount due: {amount_due}")
        amount_due = amount_due - insert_amount
        print(f"Amount due: {amount_due}") if amount_due >= 0 else print(f"Amount owed: {0-amount_due}")
        if amount_due < -100:
            print("That is enough")
            break

main()