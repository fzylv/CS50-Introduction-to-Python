import validators

email = input("Enter an email address: ")

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
