prices = [1,2,3,2,3]
lstlen = len(prices)
answer = []
flg = 1
for i in range(lstlen) :
    a = lstlen-1 - i;
    for j in range(len(prices)) :
        if flg == 1:
            if prices[j]>prices[a] :
                answer.append(a-j);
            else :
                answer.append(lstlen - j - 1)
        else :
            if prices[j]>prices[a] :
                answer[j] =a-j;
    prices.pop()
    flg = 0
print(answer)
#정확성 통과 효율성 불통2