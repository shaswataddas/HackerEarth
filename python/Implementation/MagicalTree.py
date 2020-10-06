'''
The little Monk loves to play with strings. One day he was going to a forest. On the way to the forest he saw a Big Tree(The magical tree of the forest). The magic of the tree was that, every leaf of the tree was in the format of string(having some value). Monk wants to have these type of leaves. But he can take only one. Help Monk to choose the most valuable leaf.

Format of the leaf:

a+b+c-d+c+d-x-y+x........, i.e. it contains a string holding a mathematical expression, and the value of that expression will be value of that particular leaf.

INPUT: 
4
8-6+2+4+3-6+1
1+1+1+1
2+3+6+8-9
2+7+1-6

OUTPUT:
10
'''

t = int(input())
a=[]
while t>0:
    exp = input()
    i,temp = 0,0
    
    while i<len(exp):
        if exp[i] =='+':
            temp+=int(exp[i+1])
            i+=2
        elif exp[i] =='-':
            temp-=int(exp[i+1])
            i+=2
        else:
            temp = int(exp[i])
            i+=1
    a.append(temp)
    t-=1
print(max(a))
