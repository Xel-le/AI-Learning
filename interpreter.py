def main():
    expression = str(input("Expression: ")).strip()

    x, y, z = expression.split(" ", 2)

    match y:
        case "+":
            print(int(x)+int(z))
        case "-":
            print(int(x)-int(z))
        case "/":
            print(int(x)/int(z))
        case "*":
            print(int(x)*int(z))
        case "%":
            print(int(x)%int(z))
        case _:
            print("Unknown operation")
    
main()