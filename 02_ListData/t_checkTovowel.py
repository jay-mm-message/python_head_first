
vowels = ['a', 'e', 'i', 'o', 'u']

word = 'hello world'

for letter in word:
    if letter in vowels:
        print(letter)

print(list(vowels))
print(word)