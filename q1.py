# -------------------------------- Graph Data -------------------------------- #
graph = {
    'A': ['B', 'H'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D', 'F'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F', 'H'],
    'H': ['A', 'E', 'G']
}

# -------------------------- Fucntion Implementation ------------------------- #
def getPossiblePaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = getPossiblePaths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def getShortestPath(graph, start, end):
    path = getPossiblePaths(graph, start, end)
    return min(path, key=len)

# --------------------------------- Execution -------------------------------- #

possiblePaths = getPossiblePaths(graph, 'A', 'B')
shortestPath = getShortestPath(graph, 'A', 'B')

for path in possiblePaths:
    print(path)

print(shortestPath)
