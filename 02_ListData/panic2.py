phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

# Don't panic to on tap
new_plist = ''.join(plist[1:3:1])
new_plist = new_plist + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_plist)