array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]
answer = []
templst = []
for i in range(len(commands)) :
    templst = array[commands[i][0]-1:commands[i][1]]
    templst = sorted(templst)
    ans = templst[commands[i][2]-1]
    answer.append(ans)

print(answer)

