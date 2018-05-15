word = str(input("Напишите слово, для проверки является ли оно палиндромом: "))
x = len(word)
i = 0
x = x - 1
a = 0
while x - i >= i:
    if word[x - i] == word[i]:
        i += 1
    else:
        a = 1
        break
if a == 1:
  print("Слово не является палиндромом")
else:
  print("Слово является палиндромом")