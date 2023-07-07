
vowels = ['a', 'e', 'i', 'o', 'u']

#word = 'hello world'
word = input('Provide a word to search for vowels: ')
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(list(vowels))
print(word)
print(list(found))