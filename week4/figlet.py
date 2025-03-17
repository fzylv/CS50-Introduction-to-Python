from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and sys.argv[1] =="-f" or sys.argv[1] =="--font":
    font = sys.argv[2]

    if font not in figlet.getFonts():
        sys.exit("Please enetr valid font")
else:
    sys.exit(1)


figlet.setFont(font=font)
intp = input("Input: ")

print(figlet.renderText(intp))

