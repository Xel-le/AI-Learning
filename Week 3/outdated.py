def main():

    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            initial_date = input("Date: ").strip().title()
        except EOFError:
            break
        else:
            if "/" in initial_date:
                try:
                    month, day, year = initial_date.split("/")
                    day, month, year = int(day), int(month), int(year)
                except ValueError:
                    pass
                else:
                    if not (1 <= int(day) <= 31) or not (1 <= int(month) <= 12):
                         pass
                    else:
                        print(f"{year}-{month:02}-{day:02}")
                        break
            elif any(months in initial_date for months in months_list):
                try:
                    month, day, year = initial_date.split(" ")
                    day = day.strip(",")
                    day, year = int(day), int(year)
                except ValueError:
                    pass
                else:
                    if not (1 <= int(day) <= 31):
                        pass
                    else:
                        try:
                            print(f"{year}-{months_list.index(month) + 1:02}-{day:02}")
                        except ValueError:
                            pass
                        else:
                            break

main()