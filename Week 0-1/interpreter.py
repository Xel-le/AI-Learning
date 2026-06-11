def main():
    expression = str(input("Expression: ")).strip()

    x, y, z = expression.split(" ", 2)

    match y:
        case "+":
            print(f"{int(x)+int(z):.1f}")
        case "-":
            print(f"{int(x)-int(z):.1f}")
        case "/":
            print(f"{int(x)/int(z):.1f}")
        case "*":
            print(f"{int(x)*int(z):.1f}")
        case "%":
            print(f"{int(x)%int(z):.1f}")
        case _:
            print("Unknown operation")
    
main()