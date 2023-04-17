value = input("Введите значения: ")
spisok = value.split()
slovar = {}
for i in range(1, len(spisok)+1):
    slovar[i] = spisok[i-1]

print(str(slovar).replace(', ', '\n').replace('{', '').replace('}', '').replace("'", ""))