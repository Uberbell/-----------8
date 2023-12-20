import random
def f(x):
    suma=0
    for i in x:
        if i>0:
            suma+=i
    return suma
a=[random.randint(-10,1) for i in range(20)]
b=[random.randint(-10,1)for i in range(15)]
c=[random.randint(-10,5) for i in range(10)]
m=(f(a)+f(b)+f(c))/2
print("Число М равно:",m)
print(a, "\n", b, "\n", c)

