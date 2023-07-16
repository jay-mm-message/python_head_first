boxA = [1, 2, 3, 4, 5]
boxB = boxA[2:4:1].copy()
#boxB = boxA.copy()

print(list(boxB))
print(list(boxA))

letters = "Don't panic!"
lettersB = list(letters)[2::2].copy()

print(list(letters))
print(list(lettersB))