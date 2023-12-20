def SumRange(a,b):
    suma=0
    if a>b :
        return 0
    else:
        for i in range(a,b+1):
            suma+=i
    return suma

try:
    a=int(input("Введите число А:"))
    b=int(input("Введите число В:"))
    c=int(input("Введите число С:"))
    print("Сумма целых чисел от А до В: ",SumRange(a,b))
    print("Сумма целых чисел от В до С: ",SumRange(b,c))
except:
    print("Введено неккоректные данные. Попробуйте еще раз")

