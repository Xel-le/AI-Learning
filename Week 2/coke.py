def main():
    amount_due = int(50)
    print(f"Amount Due: {amount_due}")
    while amount_due > 0:
        while True:
            insert_amount  = int(input("Insert Coin: "))
            if insert_amount in [5, 10, 25]:
                break
            print(f"Amount Due: {amount_due}")
        amount_due = amount_due - insert_amount
        print(f"Amount Due: {amount_due}") if amount_due >= 0 else print(f"Change Owed: {0-amount_due}")

main()