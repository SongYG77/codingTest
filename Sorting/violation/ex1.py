#https://www.acmicpc.net/problem/16678
num = 5
lst1 = [1,1,1,5,7]
lst1 = sorted(lst1)
hacker = 0
next_num = 1
lst1 = sorted(lst1)
for i in lst1:
    if i >= next_num :
        hacker += i-next_num
        next_num+=1
print(str(hacker))








