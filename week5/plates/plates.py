def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not started and s[i] == '0':
                return False
            started = True
        elif started and s[i].isalpha():
            return False

    return True


main()
