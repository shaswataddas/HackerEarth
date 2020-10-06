'''
As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. She solved some problems and felt very confident. Later being a fan of Hackerearth, she gave a problem to her friends to solve. They will be given a string containing only lower case characters (a-z), and they need to find that by using the characters of the given string, how many times they can print "hackerearth"(without quotes). As they are new to programming world, please help them.
'''

from math import *
n = int(input())
s = input()
temp = []

temp.append(floor(s.count('h')/2))
temp.append(floor(s.count('a')/2))
temp.append(floor(s.count('e')/2))
temp.append(floor(s.count('r')/2))
temp.append(s.count('c'))
temp.append(s.count('k'))
temp.append(s.count('t'))

print(min(temp))
