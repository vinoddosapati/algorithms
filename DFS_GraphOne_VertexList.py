from inspect import stack

#Graph one Undirected VertexList DFS

class graphtwoundir:
    def dfsvertex(self, graph, root):
        visited = []
        stack = [root]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
            neighbours = graph[vertex]
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)
        print('->'.join(visited))

    def dfs_goalpath(self, graph, root, goal):
        visited = []
        stack = [root]

        while stack:
            last_path = stack.pop()
            last_node = last_path[-1]
            if last_node == goal:
                print('->'.join(last_path))
                return last_path
            if last_node not in visited:
                visited.append(last_node)
                for neighbour in graph[last_node]:
                    if neighbour not in visited:
                        new_path = list(last_path)
                        new_path.append(neighbour)
                        stack.append(new_path)

graphVertex = {'S': ['D', 'E', 'P'], 'A': ['B', 'C'], 'C': ['A', 'D', 'F'], 'D': ['B', 'C', 'E', 'S'],
               'B': ['A', 'D'],
               'G': ['F'],
               'E': ['D', 'H', 'R', 'S'],
               'F': ['C', 'G', 'R'],
               'H': ['E', 'P', 'Q'],
               'P': ['H', 'Q', 'S'],
               'Q': ['H', 'P'],
               'R': ['E', 'F']
               }
b = graphtwoundir()
b.dfsvertex(graphVertex,'S')
b.dfs_goalpath(graphVertex,'S','G')