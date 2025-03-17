def main():
    camel_case = input("camelCase: ")
    snake_case= convert(camel_case)
    print("")

def convert(camel_case):
    for char in camel_case:
        if char.isupper():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")


main()
