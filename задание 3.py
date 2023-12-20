def PowerN(x,n):
    if n==0:
        return 1
    if n>0 and n%2==0:
        return PowerN(x,n//2)**2
    if n>0 and n%2!=0:
        return PowerN(x,n-1) * x
    if n<0:
        return 1 / PowerN(x,-n)
while True:
    try:
        x=float(input("Введите значение Х:"))
        n1=float(input("Введите значение N1:"))
        n2=float(input("Введите значение N2:"))
        n3=float(input("Введите значение N3:"))
        n4=float(input("Введите значение N4:"))
        n5=float(input("Введите значение N5:"))
        print("Значение функции от Х и N1:",PowerN(x,n1))
        print("Значение функции от Х и N2:",PowerN(x,n2))
        print("Значение функции от Х и N3:",PowerN(x,n3))
        print("Значение функции от Х и N4:",PowerN(x,n4))
        print("Значение функции от Х и N5:",PowerN(x,n5))
        break
    except:
        print("Введены некорректные данные. Попробуйте еще раз")

