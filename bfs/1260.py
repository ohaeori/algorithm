#https://www.acmicpc.net/problem/1260

from collections import deque 

n,m,v=map(int,input().split())

graph_dic={i:set() for i in range(1,1+n)} #int int


for _ in range(m):
    temp=list(map(int,input().split()))
    graph_dic[temp[0]].add(temp[1])
    graph_dic[temp[1]].add(temp[0])



stack=[v]
visited=[]

while stack:
    temp=stack.pop()
    if temp not in visited:
        visited.append(temp)
        stack +=sorted(graph_dic[temp]-set(visited),reverse=True)


for i in visited:print(i,end=' ')

print()
queue=deque([v])
visited=[]

while queue:
    temp=queue.popleft()
    if temp not in visited:
        visited.append(temp)
        queue +=sorted(graph_dic[temp]-set(visited))

for i in visited:print(i,end=' ')