import numpy as np
array = np.random.randint(0,1000, int(input('Введите количество элементов массива: ')))

print('Элементы массива: ')
for i in range(0,len(array)):
    print(array[i], end=' ')

print('\n')
print('Максимальный элемент массива: {str}'.format( str = np.amax(array)))
