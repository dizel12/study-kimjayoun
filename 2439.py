x int(input())

for i in range(x):
    num = n - (i+1)
    for j in range(x):
        if num > 0:
            print(" ",end='')
        else:
            print("*"end='')
        num-=1;
    print()
