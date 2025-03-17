import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if pattern:
        time_groups = pattern.groups()
        if int(time_groups[1]) > 12 or int(time_groups[5]) > 12:
            raise ValueError
        start_time = format_time(time_groups[1], time_groups[2], time_groups[3])
        end_time = format_time(time_groups[5], time_groups[6], time_groups[7])
        return f"{start_time} to {end_time}"
    else:
        raise ValueError


def format_time(hour, minute, am_pm):
    if am_pm == "PM" and int(hour) != 12:
        nhour = int(hour) + 12
    elif am_pm == "AM" and int(hour) == 12:
        nhour = 0
    else:
        nhour = int(hour)

    if minute is None:
        nminute = "00"
    else:
        nminute = minute

    return f"{nhour:02d}:{nminute}"


if __name__ == "__main__":
    main()
