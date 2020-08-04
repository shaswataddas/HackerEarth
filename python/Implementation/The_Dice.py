seq = input()
count=0
if '7' in seq or '8' in seq or '9' in seq or '0' in seq:
    print(-1)
if seq[-1]=='6':
    print(-1)
else:
    for i in seq:
        if i !='6':
            count+=1
    print(count)
