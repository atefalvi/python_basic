def print_two(*args):
    arg1, arg2, arg3 = args
    print(args)
    print(type(args))
    print(f"arg1: {arg1} | agr2: {arg2}")
    
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} | agr2: {arg2}")

def print_nth():
    print("i got nothing")

print_two("Atef","Maria","Zar")
print_two_again("Dog","Cat")
print_nth()
