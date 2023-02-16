'''1zad
a = int(input())
if a>40:
    print("боковое")
else:
    print("купе")
if a % 2 == 0:
    print("верхнее")
else:
    print("нижнее")




b = int(input())
if b % 4 == 0 and b % 100 != 0 or b % 400 == 0:
    b = str(b)
    print("год ", b, " високосный")
else:
    print("год не високосный")

'''
n = int(input())
text = ""
