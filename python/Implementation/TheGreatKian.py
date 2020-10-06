'''
The great Kian is looking for a smart prime minister. He's looking for a guy who can solve the OLP (Old Legendary Problem). OLP is an old problem (obviously) that no one was able to solve it yet (like P=NP).

But still, you want to be the prime minister really bad. So here's the problem:

Given the sequence a1, a2, ..., an find the three values a1 + a4 + a7 + ..., a2 + a5 + a8 + ... and a3 + a6 + a9 + ... (these summations go on while the indexes are valid).

INPUT:
5
1 2 3 4 5

'''

n = int(input())
ls = list(map(int,input().split()))
temp = [0,0,0]

for i in range(len(ls)):
    if i%3==0:
        temp[0]+=ls[i]
    elif i%3==1:
        temp[1]+=ls[i]
    else:
        temp[2]+=ls[i]

print(temp[0],temp[1],temp[2])
