def main():
    expression = str(input("Expression: ")).strip()

    x, y, z = expression.split(" ", 2)

    match y:
        case "+":
            print(f"{int(x)+int(z):.f1}")
        case "-":
            print(f"{int(x)-int(z):.f1}")
        case "/":
            print(f"{int(x)/int(z):.f1}")
        case "*":
            print(f"{int(x)*int(z):.f1}")
        case "%":
            print(f"{int(x)%int(z):.f1}")
        case _:
            print("Unknown operation")
    
main()