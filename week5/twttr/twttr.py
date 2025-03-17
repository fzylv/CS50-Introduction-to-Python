def main():
    text = input("Input: ")
    updated_text = shorten(text)
    print("Output:", updated_text)


def shorten(word):
    text_wv = ""
    for letter in word:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            text_wv += letter
    return text_wv


if __name__ == "__main__":
    main()
