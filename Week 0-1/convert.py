def main():
    text = convert(input("Input your text: "))
    print(text)

def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    return string

main()