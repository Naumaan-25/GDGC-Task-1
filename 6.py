with open("practice.txt", "w") as f:
    f.write("Visca Barca!")

with open("practice.txt", "r") as f:
    content = f.read()
    print(content)