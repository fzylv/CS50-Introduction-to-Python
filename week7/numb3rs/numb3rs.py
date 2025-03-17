import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"

    if re.match(pattern, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
