import time
start = time.time()
str1 = 'AAAABBBBB'
Sang = ['A','B','C']
Chang = ['B','A','B','C']
Hyeun = ['C','C','A','A','B','B']
score = [0, 0, 0]
name = []
for i in range(len(str1)) :
    if Sang[i%3] == str1[i] : score[0] +=1
    if Chang[i % 4] == str1[i]: score[1] += 1
    if Hyeun[i % 6] == str1[i]: score[2] += 1
print(max(score))
if score[0] == max(score) : name.append('Adrian')
if score[1] == max(score) : name.append('Bruno')
if score[2] == max(score) : name.append('Goran')
for i in range(len(name)) :
    print(name[i])
print("time :", time.time() - start)