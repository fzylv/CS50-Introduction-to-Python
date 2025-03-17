vowels = ['a','e','i','o','u', 'A','E','I','O','U']
text = input("Input: ")
for vowel in text:
    if vowel not in vowels:
        print(vowel, end="")
