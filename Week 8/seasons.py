import datetime
from sys import exit
from num2words import num2words

def main():
    current_date = datetime.date.today()
    try:
        birth_date = datetime.date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        exit("Invalid date")
    print(f"{calculate_minutes(current_date, birth_date)} minutes")

def calculate_minutes(c_date, b_date):
    delta = c_date - b_date
    return num2words(delta.days * 24 * 60).capitalize()

if __name__ == "__main__":
    main()
