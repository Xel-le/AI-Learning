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
                    if int(day) > 31 or int(month) > 12:
                         pass
                    else:
                        print(f"{year}-{month}-{day}")
                        break
                    break
            elif any(months in initial_date for months in months_list):
                try:
                    month, day, year = initial_date.split(" ")
                    day = day.strip(",")
                    day, year = int(day), int(year)
                except ValueError:
                    pass
                else:
                    if int(day) > 31:
                        pass
                    else:
                        print(f"{year}-{months_list.index(month)}-{day}")
                        break
                    break

main()