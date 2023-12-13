def SumRange(a,b,c):
    suma=0
    suma2=0
    if a>b or b>c:
        return 0
    else:
        for i in range(a,b+1):
            suma+=i
        for i in range(b,c+1):
            suma2+=i
    return suma,suma2

try:
    a=int(input("Введите число А:"))
    b=int(input("Введите число В:"))
    c=int(input("Введите число С:"))
    print("Сумма целых чисел от А до В и от В до С:",SumRange(a,b,c))
except:
    print("Введено неккоректные данные. Попробуйте еще раз")

