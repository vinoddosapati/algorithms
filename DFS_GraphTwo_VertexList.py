from inspect import stack


class dfsgraphtwovertex:
    def dfs_graph_vetex(self,graph,root):
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

    def dfs_path_goal(self, graph, root, goal):
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


graphtwovertex = {
    'A': [],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C', 'E'],
    'E': ['H', 'R'],
    'F': ['C', 'G'],
    'G': [],
    'H': ['P', 'Q'],
    'P': ['Q'],
    'Q': [],
    'R': ['F'],
    'S': ['D', 'E', 'P']
}

g = dfsgraphtwovertex()
g.dfs_graph_vetex(graphtwovertex, 'S')
g.dfs_path_goal(graphtwovertex,'S', 'G')