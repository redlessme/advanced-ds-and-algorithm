import math
from collections import defaultdict
from FHeap import makeHeap

class Graph:
    def __init__(self, n):
        self.nodes = set(range(1,n+1))
        self.edges = defaultdict(list)
        self.distances = {}


    def add_edge(self, vertex1, vertex2, distance):
        self.edges[vertex1].append(vertex2)# {2: [2, 5], 1: [2]})
        self.edges[vertex2].append(vertex1)  #beacuse it is undirected graph
        self.distances[vertex1, vertex2] = distance #{(1, 2): 8}
        self.distances[vertex2, vertex1] = distance


def init_distance(graph,s):
    distance={s:0}
    for vertex in graph.nodes:
        if vertex!=s:
            distance[vertex]=math.inf
    # print(distance)
    return distance

def dijkstra(graph,s):
    finalized=set()
    distance=init_distance(graph,s)
    fheap=makeHeap()
    fheap.insert(0,s)

    while fheap.n>0:
        pair=fheap.extract_min()
        v=pair.value
        vdist=pair.key
        finalized.add(v)
        neighbors=graph.edges[v]
        for u in neighbors:
            if u not in finalized:
                if distance[u]>vdist+graph.distances[v,u]:
                    fheap.insert(vdist+graph.distances[v,u],u)
                    distance[u]=vdist+graph.distances[v,u]
    return distance
if __name__ == '__main__':
    edgesList = []
    with open('text0.txt', 'r') as f:
        num = int(f.readline())
        data = f.readlines()
        for line in data:
            line = line.strip('\n')
            line = line.split(' ')
            line[0] = int(line[0])
            line[1] = int(line[1])
            line[2] = int(line[2])
            edgesList.append(line)
    graph1 = Graph(num)
    for i in range(len(edgesList)):
        graph1.add_edge(edgesList[i][0], edgesList[i][1], edgesList[i][2])
    distance=dijkstra(graph1,1)
    print(distance)

