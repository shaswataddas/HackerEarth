binary = input()
count=1
flag=1
for i in range(len(binary)-1):
    if binary[i] == binary[i+1]:
        count+=1
    else: 
        count = 0
    if count==6-1:
        print("Sorry, sorry!")
        flag=0
        break
if flag:
    print("Good luck!")
#0001111110
