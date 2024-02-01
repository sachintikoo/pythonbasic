with open("donkey.txt") as f:
    content = f.read()

content = content.replace("$%^@$^#", "######")

with open("donkey.txt", "w") as f:
    f.write(content)
