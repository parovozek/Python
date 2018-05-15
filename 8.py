import numpy as np
array = np.random.randint(-100,100, (int(input('Введите количество элементов массива: '))))
print('Рандомные числа массива: ')
for i in range(0,len(array)):
    print(array[i], end=' ')

for i in range(1, len(array) - 1):
    if ((array[i-1] > 0) and (array[i+1] > 0)):
        str = 'существуют'
    else:
        str = 'не существуют'
print('\n')
print('Cоседние элементы с одинаковым знаком {} в массиве'.format(str))