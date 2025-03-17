import sys
import csv

def main():
    check()
    try:
        with open(sys.argv[1], "r") as file:
            read = csv.DictReader(file)
            student =[]
            for row in read:
                last, first = row["name"].split(", ")
                student.append({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(student)


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()

