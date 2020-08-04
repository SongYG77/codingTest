from collections import deque
prices = [1,2,3,2,3]
answer = []
q = deque(prices)
count = 0;
q = deque(prices)
while q:
    n = q.popleft()
    for i in q :
        count += 1
        if n > i :
            break
    answer.append(count)
    count=0
print(answer)
# 드디어 성공! 
