'''
You are given an array of integers of size . You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.


SAMPLE INPUT

5
1000000001 1000000002 1000000003 1000000004 1000000005

'''

n = int(input())
array = list(map(int,input().split()))

print(sum(array))
