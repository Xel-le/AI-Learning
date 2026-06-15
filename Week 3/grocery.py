def main():
    item_list = []
    while True:
        try:
            item = input().strip().lower()
        except EOFError:
            unique = sorted(set(item_list))
            for u in unique:
                print(f"{item_list.count(u)} {u.upper()}")
            break
        else:
            item_list.append(item)


main()