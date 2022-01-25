#Calculator
#Ввод числа a
print ("Введите число а:")
a = int(input())

#Ввод числа b
print ("Введите число b:")
b = int(input())

#Выбор действия
print ("Выберите действие: (от 1 до 4)")
print ("1 - Сложить a + b")
print ("2 - Вычесть a - b")
print ("3 - Умножить a + b")
print ("4 - Разделить a + b")
n = int(input())

if n == 1:
	print ("Сумма a + b =", a + b)
if n == 2:
	print ("Разность a - b =", a - b)
if n == 3:
	print ("Произведение a * b =", a * b)
if n == 4:
	print ("Частное a / b =", a / b)