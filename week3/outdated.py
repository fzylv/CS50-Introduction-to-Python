months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            break
    except ValueError:
        try:
            cmonth, cday, year = date.split(" ")
            for x in range(len(months)):
                if cmonth == months[x]:
                    month = x + 1
                    break


            if not cday.endswith(","):
                continue
            day = int(cday.replace(",", ""))
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except (ValueError, IndexError):
            print("Invalid date format. Please enter again.")
            pass

print(f"{year}-{month:02d}-{day:02d}")
