n = int(input("Введите число n: ")) # Ввод числа, до которого будет считать сумму
summa = 0 # Число, от которого идет подсчет суммы
for i in range(1, n+1): # Цикл for с шагом
    summa += i # Сумма чисел: число + (число + 1)
print(f"Сумма всех чисел от 1 до {n} равна {summa}") # Вывод суммы чисел от 1 до n