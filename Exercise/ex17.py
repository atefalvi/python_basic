from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying content from {from_file} to {to_file}")

print(f"Does output file exist: {exists(to_file)}")

data = open(from_file).read()

open(to_file, 'w').write(data)

print("Copy complete")

open(from_file).close()
open(to_file).close()
