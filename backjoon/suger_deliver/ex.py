N = int(input())
ctr = 0
while True:
    if N%5 == 0 : break
    if N<0 :
        break
    N=N-3
    ctr += 1
ctr += int(N/5)
if(N<0) : print(-1)
else : print(ctr)
