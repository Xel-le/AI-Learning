def main ():
    answer = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))
    if isTrue(answer.lower()):
        print("Yes")
    else:
        print("No")


def isTrue(str):
    return str in {"42", "forty two", "forty-two"}

main()