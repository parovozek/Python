a=int(input("Введите первое число "))
b=int(input("Введите второе число "))
c=int(input("Введите третье число "))

if c <= a >= b :
    print('{} - Наибольшее число '.format(a))
elif a <= b >= c:
    print('{} - Наибольшее число '.format(b))
else:
    print('{} - Наибольшее число '.format(c))