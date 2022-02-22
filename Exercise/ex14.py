from sys import argv

script, user = argv

prompt = '> '
print(f'Hi {user}, I am {script} script.')
print('I would like to ask you some questions?')
print('Do you like me?')

like = input(prompt)

print(f'Where do you live {user}?')

lives = input(prompt)

print(f'What kind of computer do you use in {lives}?')

computer = input(prompt)

print(f"""
Alright, so you said you {like} about liking me.
You live in {lives}
And you use a {computer} machine.
Awesome!
""")
