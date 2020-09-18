a= int(input())
lst = []
for i in range(a):
    lst.append(list(map(str,input().split())))
lst.sort(key = lambda x : int(x[0]))
for i in lst:
    print(i[0],i[1])