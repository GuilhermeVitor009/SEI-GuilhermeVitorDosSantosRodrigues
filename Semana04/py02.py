message = """Bobby\'s World is a great cartoon 
from the 1990's"""
print(len(message))
print(message[0])
print(message[0:5])
print(message[6:])
print(message)
print(message.upper())
print(message.lower())
print(message.count('d'))
print(message.find('l'))
new_message = message.replace('World', 'Universe')
print(new_message)
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome'
print(message)
message = '{} {} .Welcome'.format(greeting, name)
print(message)
message = f'{greeting} {name}. Welcome!!'
print(message)
message = f'{greeting} {name.upper()}. Welcome!!'
print(message)
print(dir(name))
print(help(str.lower))
print(help(str))
