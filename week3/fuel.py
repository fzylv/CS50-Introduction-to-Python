def main():
    fraction =get_fraction()
    percentage =round(fraction * 100)

    if percentage <=1:
       print("E")
    elif percentage >= 99:
        print("F")
    else:
       print(f"{percentage}%")

def get_fraction():
    while True:
        try:
            uinput = input("Fraction: ")
            x, y = uinput.split("/")
            x, y = int(x), int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            return x/y

        except(ValueError, ZeroDivisionError):
            pass


main()
