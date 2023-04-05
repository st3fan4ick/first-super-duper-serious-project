#Калькулейтор

def main():
    print("Калькулятор.\n1.Сложение.\n2.Вычитание.\n3.Деление.\n4.Умножение.")
    choice = input("Ваш выбор: ")
    if choice == 'q':
        print("Выход из программы...")
        exit()
    try:
        choice = int(choice)
        if choice > 4:
            print("Вводите только предоставленные числа!")
            main()
        elif choice < 1:
            print("Вводите только предоставленные числа!")
            main()
        elif choice == 1:
            print("Сложение")
            sum()
        elif choice == 2:
            print("Вычитание")
            subtract()
        elif choice == 3:
            print("Деление")
            divide()
        elif choice == 4:
            print("Умножение")
            multiple()
    except ValueError:
        print("Вводите только предоставленные числа!")
        main()

def sum():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Вводите только числа!")
        sum()
    else:
        print(f"Сумма чисел:{a+b}")
        main()

def subtract():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Вводите только числа!")
        subtract()
    else:
        print(f"Разность чисел:{a-b}")
        main()

def divide():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Вводите только числа!")
        divide()
    else:
        print(f"Частность чисел:{a/b}")
        main()

def multiple():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Вводите только числа!")
        multiple()
    else:
        print(f"Произведение чисел:{a*b}")
        main()

main()