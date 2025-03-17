houses =["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

house = input("What is your Hogwarts house? ")

if house in houses:
    print(f"Welcome to {house}!")
else:
    print("Please enter a valid house name!")
