from collections import deque
'''
num = int(input())
lst1 = []
for i in range(num) :
    lst1.append(int(input()))
'''

num = 5
lst1 = [7,8,13,15,16]
d = deque(lst1)
hacker = 0
d = sorted(d)
while d:
    if d[0] > 1 :
        temp = d[0] - 1

    d.remove(max(d))
print(str(hacker))