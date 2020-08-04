for _ in range(int(input())):
    s = input()
    count=0
    for j in range(len(s)):
        if(s[j] in 'AEIOUaeiou'):
            count += (len(s)-j)*(j+1)
    print(count)
