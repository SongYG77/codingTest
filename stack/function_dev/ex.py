from collections import deque
progresses = [93,30,55]
speeds = [1,30,5]
answer = []
d1= deque(progresses)
d2 = deque(speeds)
c=0
while d1:
    d1 = deque(map(lambda x,y : x+y,d1,d2))
    while d1 and d1[0] > 99:
        d1.popleft()
        d2.popleft()
        c+=1
    if c > 0 :
        answer.append(c)
        c=0
print(answer)
