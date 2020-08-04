'''
import math
for _ in range(int(input())):
    low,high,num = map(int,input().split())
    if low>=high:
        print('-1','-1')
    else:
        min_sound = math.ceil(low/num)
        max_sound = high//num
        if min_sound > 0 and max_sound > 0 or abs(min_sound)<=abs(max_sound):
            print(min_sound,max_sound)
        else:
            print('-1','-1')
'''
import math
t=int(input())
for _ in range(t):
    l,r,s=map(int,input().split())

    m=math.ceil(l/s)
    n=r//s

    if(s>r):
        print("-1 -1")
    else:
        if(m<=n):
            print(m,n)
        else:
            print("-1 -1")
