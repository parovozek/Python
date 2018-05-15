x = int(input('Введите x = '))

print('Натуральные делители в порядке возрастания, числа {}:'.format(x))
for i in range(1,x+1):
    if x % i == 0:
      print(i,end = ' ')