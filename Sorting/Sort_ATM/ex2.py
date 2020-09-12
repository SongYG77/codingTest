a = int(input())
lst = list(map(int,input().split()))
lst = sorted(lst)
ctr = 0;
for i in range(a):
    ctr += lst[i] * (a-i)
print(ctr)