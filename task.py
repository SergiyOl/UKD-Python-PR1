while True : 
    x = int(input("Введіть перше число: "))
    a = int(input("Введіть друге число: "))
    b = int(input("Введіть третє число: "))
    if x < 0 or a < 0 or b < 0 :
        print("Якесь з чисел відємне")
    elif x == 0 and a == 0 and b == 0 :
        print("всі числа дорівнюють нулю")
    else :
        break

result = (x**2 + a*x + b)**0.5/(x**4 + a*x + b)**0.5

print("Змінні: " + "x = " + str(x) + ", a = "+ str(a) + ", b = " + str(b) + ". Результат: " + str(result))