def main():
    camel_case = input("Input camelCase name: ")
    camel_case = transform_to_snake(camel_case)
    print(camel_case)

def transform_to_snake(camel_str):
    camel_str = list(camel_str)
    for i, c in enumerate(camel_str):
        if c.isupper() and i == 0:
            camel_str[i] = c.lower()
        elif c.isupper() and i != 0:
            camel_str[i] = "_" + c.lower()
    camel_str = "".join(camel_str)
    return camel_str

main()