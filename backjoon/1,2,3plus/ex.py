#백준 9095 내 코드
from math import factorial
p = int(input())
n = []
for i in range(p):
    n.append(int(input()))
for q in n:
    count = 0
    a = q // 3
    for i in range(a+1) :
        temp = q - (3 * i)
        b = temp // 2
        for j in range(b+1) :
            c = temp - (2*j)
            sum = i+j+c
            k = i
            l = j
            if k ==0 :
                k=1
            if l ==0 :
                l=1
            if c == 0:
                c=1
            tt = factorial(sum)//(factorial(k) *factorial(l) * factorial(c))
            count += tt
    print(count)