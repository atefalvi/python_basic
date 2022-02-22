from sys import argv

script, filename = argv

txt = open(filename)

print(f"You are opening file: '{filename}'")
print("-" * 9 + "start" + "-"*9)
print(txt.read())
print("-" * 10 + "end" + "-"*10)


print(f"Do you want to erase {filename}?")
print("If yes pressure RETURN or else CTRL + C")
input("> ")

target = open(filename, 'w')

target.truncate()
print("File is erased")
print("==============")

print(f"Reloading: '{filename}'")
print("-" * 9 + "start" + "-"*9)
print(txt.read())
print("-" * 10 + "end" + "-"*10)

print(f"Let add new lines to {filename}")

line1 = input("What is your name? ")
line2 = input("Say something random: ")

target.write(line1+"\n")
# target.write(line1)
target.write(line2)

target.close()


