try:
    c = int(input("Введите символ: "))
    print("Введеный символ - число")
except ValueError:
    print("Введеный символ не является числом")