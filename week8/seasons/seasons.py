from datetime import date
import re
import sys
import inflect

def main():
    birthday = input("Date of Birth: ")

    try:
        year, month, day = check_birthday(birthday)
        birth_day = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid Date")

    dtoday = date.today()
    diff = dtoday - birth_day
    total_minutes = diff.days * 24 * 60

    # Convert number to words
    p = inflect.engine()
    output = p.number_to_words(total_minutes, andword="").capitalize()

    print(output + " minutes")

def check_birthday(birthday):
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", birthday):
        year, month, day = birthday.split("-")

        try:
            date(int(year), int(month), int(day)) 
            return year, month, day
        except ValueError:
            pass

    raise ValueError("Invalid date")

if __name__ == "__main__":
    main()
