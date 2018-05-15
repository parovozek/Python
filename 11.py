import re
 
def count(s):
    return len(re.split('\s+', s))
 
word = 'Lorem ipsum congue non    at ut sagittis, vivamus metus lectus auctor rutrum magna lorem bibendum eros amet eget in maecenas sit massa lectus '
print("Колличество слов")
print(count(word) )