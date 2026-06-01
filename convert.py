def main():
    text = input("Input your text: ")
    if ":)" in text:
        text = text.replace(":)", "🙂")
    if ":(" in text:
        text = text.replace(":(", "🙁")
    print(text)

main()