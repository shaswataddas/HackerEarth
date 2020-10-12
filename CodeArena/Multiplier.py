t = int(input())
for i in range(t):
    lower, upper, val = map(int, input().split())
    count=0
    for j in range(lower,upper+1):
        count+=1 if j%val==0 else 0
    print(count)
