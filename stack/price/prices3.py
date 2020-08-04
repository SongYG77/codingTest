prices = [1,2,3,2,3]
lstlen = len(prices)
templst = prices[:]
count = 0
answer = []
for i in range(lstlen) :
    for j in range(len(templst)) :
        count+=1
        if prices[i] > templst[j]:
            break
    answer.append(count-1)
    count = 0
    templst.remove(prices[i])
print(answer)
#정확성 통과 효율성 불통3