from itertools import permutations
numbers = [3,30,34,5,9]
answer = ''
numbers = list(map(str,numbers))
numbers.sort(key=lambda x : x*3,reverse=True)
answer = ''.join(numbers)