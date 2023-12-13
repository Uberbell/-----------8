import random
def f(x):
    suma=0
    for i in x:
        if i>0:
            suma+=i
    return suma
a=[random.randint(-100,100) for i in range(20)]
b=[random.randint(-100,100)for i in range(15)]
c=[random.randint(-100,100) for i in range(10)]
m=(f(a)+f(b)+f(c))/2
print("Число М равно:",m)

