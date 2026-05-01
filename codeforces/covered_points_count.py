n = int(input())

coordcompression = set()

segments = []
for i in range(n):
    x,y = map(int, input().split())
    segments.append((x,y))
    coordcompression.add(x)
    coordcompression.add(y+1)


coordcompression = sorted(list(coordcompression))
coordcompression_dict = {v: i for i, v in enumerate(coordcompression)}

covered = [0 for i in range(len(coordcompression))]

for x,y in segments:
    covered[coordcompression_dict[x]] += 1
    covered[coordcompression_dict[y+1]] -= 1

for i in range(1, len(covered)):
    covered[i] += covered[i-1]

answer = 0
num_each = [0 for i in range(n+1)]
for i in range(len(covered)-1):
    num_each[covered[i]] += coordcompression[i+1] - coordcompression[i]

for i in range(1, n+1):
    print(num_each[i], end = " ")





