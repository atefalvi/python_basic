from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying content from {from_file} to {to_file}")

data = open(from_file).read()

print(data)