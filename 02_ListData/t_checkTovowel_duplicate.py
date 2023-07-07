
vowels = ['a', 'e', 'i', 'o', 'u']

word = 'hello world'
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(list(vowels))
print(word)
print(list(found))