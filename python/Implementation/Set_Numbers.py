'''
for _ in range(int(input())):
    num = int(input())
    i=0
    while True:
        if 2**i<=num:
            i+=1
        else:
            break
    print((2**(i-1))-1)
'''
for _ in range(int(input())):
    x=int(input())
    bi=bin(x)
    l=len(bi)-2
    res=2**l-1
    if res>x:
        print((2**(l-1))-1)
    else:
        print(res)
