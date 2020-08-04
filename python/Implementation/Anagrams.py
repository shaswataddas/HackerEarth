def anagram(s1,s2):
    CHAR = 26
    lst1 = [0]*CHAR
    lst2 = [0]*CHAR

    for i in s1:
        lst1[ord(i)-ord('a')] +=1
    for i in s2:
        lst2[ord(i)-ord('a')] +=1

    result = 0
    for i in range(26):
        result += abs(lst1[i] - lst2[i])
    print(result) 


t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    anagram(s1,s2)
