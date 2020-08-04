prices = [1,2,3,2,3]
lstlen = len(prices)
answer = []
for i in range(lstlen) :
    answer.append(lstlen-i-1)
for i in range(lstlen) :
    a = lstlen-1 - i;
    for j in range(len(prices)) :
        if prices[j]>prices[a] :
            answer[j] = a-j;
    prices.pop()
print(answer)
#정확성 통과 효율성 불통