import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import inf

graph = {'A': {'C': 5, 'D': 1, 'E': 2},
         'B': {'H': 1, 'G': 3},
         'C': {'I': 2, 'D': 3, 'A': 5},
         'D': {'C': 3, 'A': 1, 'H': 2},
         'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1},
         'G': {'F': 1, 'B': 3, 'H': 2},
         'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
         'I': {'C': 2, 'H': 2}}

def longSearch(source, target, graph):
    graph_key_list = list(graph)
    length = len(graph_key_list)
    costs = dict.fromkeys(graph_key_list, -inf)

    #pull first value for removal and readd
    temp = dict.fromkeys(list(costs.keys())[0])

    #create new dictionary with only the first key in the built cost array
    tempCost = dict.fromkeys(temp, 0)

    #Update costs with new value for initial index
    costs.update(tempCost)
    #updtating travel costs
    parents = {}
    nextNode = source
    while nextNode != target:
        for neighbor in graph[nextNode]:
            if graph[nextNode][neighbor] + costs[nextNode] > costs[neighbor]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                parents[neighbor] = nextNode
            del graph[neighbor][nextNode]
        del costs[nextNode]
        nextNode = max(costs, key=costs.get)

    return parents


def longestPath(source, target, searchResult):
    node = target
    backpath = [target]
    path = []
    while node != source:
        backpath.append(searchResult[node])
        node = searchResult[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])
    return path

result = longSearch('A', 'B', graph)
print('longest path={}'.format(longestPath('A', 'B', result)))

#graph construction
G = nx.Graph()
P = nx.Graph()

q = list(graph.items())

while q:
    v, d = q.pop()
    for nv, nd in d.items():
        G.add_edge(v, nv)


np.random.seed(1)

pos = nx.spring_layout(G, seed=6)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
nx.draw_networkx_edges(G, pos, width=6)


#plot path
output = longestPath('A', 'B', result)
length = len(output)

for i in range(0, length-1):
        P.add_edge(output[i], output[i+1])
nx.draw_networkx_edges(P, pos, width=6, alpha=1, edge_color="r", style="dashed")

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
