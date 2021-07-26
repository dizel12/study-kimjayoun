import math
def add_func(a,b):
    return float(a)+float(b)

def minus_func(a,b):
    return float(a)-float(b)

def mult_func(a,b):
    return float(a)*float(b)

def div_func(a,b):
    return a/b

def root_func(a):
    return math.isqrt(a)

def abs_func(a):
    return math.fabs(a)

def poly_func(a,b,c):
    t = b**2 - 4*a*c
    if  t < 0:
        return 0, 0
    x = (-b + math.isqrt(b*b-4*a*c))/2*a
    y = (-b - math.isqrt(b*b-4*a*c))/2*a
    if t==0:
        return x, x
    else:
        return x, y

def facto_func(a):
    return math.factorial(a)

arr = list(map(str, input().split()))
result = arr[0]
for i in range(1,len(arr)):
    #print(i, arr[i])
    if arr[i] == '+':
        i+=1
        result = add_func(result, arr[i])
    if arr[i] == '-':
        i+=1
        result = minus_func(result, arr[i])

print(result)
