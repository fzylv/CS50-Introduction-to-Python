import sys
import csv
from tabulate import tabulate

def main():
    check()
    info = []
    try:
        with open(sys.argv[1], "r") as file:
            read = csv.reader(file)
            for row in read:
                info.append(row)
    except FileNotFoundError:
        sys.exit("File not found")

    print(tabulate(info[1:], headers=info[0], tablefmt="grid"))

def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ =="__main__":
    main()
