def main():
    emoji=input("Enter emoticon: ")
    converted = convert(emoji)
    print(converted)

def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji


main()


