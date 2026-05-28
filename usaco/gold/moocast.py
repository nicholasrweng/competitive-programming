from collections import deque

fin = open("moocast.in", "r")
fout = open("moocast.out", "w")

n = int(fin.readline())
cows = []

for i in range(n):
    x, y = map(int, fin.readline().split())
    cows.append((x, y))


def bfs(start, adj):
    visited = [False for i in range(n)]
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        if not visited[node]:
            for u in adj[node]:
                if not visited[u]:
                    queue.append(u)
                    visited[u] = True

    return all(visited)



def trial(x):
    adj = [[] for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = cows[i]
            x2, y2 = cows[j]

            if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= x:
                adj[i].append(j)
                adj[j].append(i)

    return bfs(0, adj)


lo = 0
hi = 25000 ** 2 + 25000 ** 2

while lo < hi:
    mid = (lo + hi) // 2

    if not trial(mid):
        lo = mid + 1
    else:
        hi = mid

fout.write(str(lo) + "\n")

fin.close()
fout.close()