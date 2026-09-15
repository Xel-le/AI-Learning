import validators
from sys import exit

def main():
    try:
        print(validate(input("What's your email? ")))
    except EOFError:
        exit()

def validate(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    main()