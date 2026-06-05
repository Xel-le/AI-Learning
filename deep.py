def main ():
    answer = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?"))
    if isTrue(answer.strip().lower()):
        print("Yes")
    else:
        print("No")


def isTrue(s):
    return s in {"42", "forty two", "forty-two"}

main()