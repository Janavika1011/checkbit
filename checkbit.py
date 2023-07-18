def checkbit(x,y):
    for i in range(y):
        x>>=1
    if x&1:
        print(1)
    else:
        print(0)
x = int(input())
y = int(input())
print(checkbit(x,y))
