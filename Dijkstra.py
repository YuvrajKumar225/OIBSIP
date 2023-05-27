# from heapq import *
# def dijkstra (graph,start,visited,distance):

#     distance[start]=0
#     bag=[]
#     heappush(bag,(0,start))

#     while bag:
#         d,n = heappop(bag)  # Node with minimum distance will pop
#         visited[n]=1 # become visited
#         for cd,cn in graph[n]:   # check for all adjecent node of selected node
#             # if  not visited and parent dist + new distance is less than current node's dist from source
#             if not visited[cn] and distance[n] + cd < distance[cn]:
#                 # update new distance and parent dist + new dist
#                 distance[cn] = distance[n] + cd
#                 # push new distance and node in bag
#                 heappush(bag,(distance[cn],cn))
#     print("Vertex : Shortest Distance" ,distance)

# ipt =[[1,3,2],[1,2,1],[2,3,1],[2,5,1],[3,4,2],[5,4,3]]

# n=5
# graph ={}
# distance={}
# visited={}

# for i in range (1,n+1):
#     graph[i]=[]
#     distance[i]=10**8+1
#     visited[i]=0

# for u,v,d in ipt:
#     graph[u].append([d,v])
#     graph[v].append([d,u])

# start=1 # this is source
# dijkstra(graph,start,visited,distance)








import sys
from heapq import heapify, heappush, heappop
def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data = {'A':{'cost':inf,'pred':[]},
    'B':{'cost':inf,'pred':[]},
    'C':{'cost':inf,'pred':[]},
    'D':{'cost':inf,'pred':[]},
    'E':{'cost':inf,'pred':[]},
    'F':{'cost':inf,'pred':[]}
    }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(5):
        if temp not in visited: # TODO: Reassign source
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))
if __name__ == "__main__":
    graph = {
        'A':{'B':2,'C':4},
        'B':{'A':2,'C':3,'D':8},
        'C':{'A':4,'B':3,'E':5,'D':2},
        'D':{'B':8,'C':2,'E':11,'F':22},
        'E':{'C':5,'D':11,'F':1},
        'F':{'D':22,'E':1}
    }
    source = 'A'
    destination = 'F'
    dijsktra(graph,source,destination)
