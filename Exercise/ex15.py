from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is the details from your file '{filename}':")
print("==================================="+"-" * (len(filename)+2))

print(txt.read())

print("=================== X X X ========================")

print("Enter the file name again")
filename2 = input("> ")

print(f"Here is the details from your file '{filename2}':")
print("=================================================")

print(open(filename2).read())
