n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)  #한 행에서 작은 수
    result = max(min_value, result)  #max 큰수 뽑기

print(result)
'''
입력예시1
3 3
3 1 2 
4 1 4
2 2 2 
출력예시1: 2

입력예시2
2 4
7 3 1 8 
3 3 3 4
출력예시2: 3
'''
