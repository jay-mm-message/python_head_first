phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

# Don't panic to on tap
print() # display from the next line
for i in range(3):
    plist.pop()
    print(plist)
print(plist)
plist.pop(0)
plist.remove("'")
print(plist)
plist.extend([plist.pop(), plist.pop()])
print(plist)
plist.insert(2, plist.pop(3))
print(plist)

print()
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)