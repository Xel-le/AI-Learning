def main():
    amount_due = int(50)
    print(f"Amount Due: {amount_due}")
    while amount_due > 0:
        insert_amount  = int(input("Insert Coin: "))
        if insert_amount in [5, 10, 25]:
            amount_due = amount_due - insert_amount
            print(f"Amount Due: {amount_due}") if amount_due > 0 else print(f"Change Owed: {0-amount_due}")
        else:
            print(f"Amount Due: {amount_due}")

main()