a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if (c >= (a + b)) or (b >= (a + c)) or (a >= (b + c)):
    print ("Треугольника не существует")
else:
    print ("Треугольник существует")