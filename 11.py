t = open('Poems.txt')
r = t.read()
if 'twinkle' in r :
    print("Yes twinkle is present in txt file")
else:
    print("No its not present")
t.close()