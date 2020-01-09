class dfs_vertex_rec_graphtwo:
    def dfs_path_find_rec(self, graph, stack, visited):
        if stack:
            last_node = stack.pop()
            if last_node not in visited:
                visited.append(last_node)
                neighbours = graph[last_node]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        stack.append(neighbour)
            self.dfs_path_find_rec(graph, stack, visited)
        else:
            print('->'.join(visited))


    def dfs_goal_search_path(self, graph, stack, visited, goal):
        if stack:
            last_path = stack.pop()
            last_node = last_path[-1]
            if last_node == goal:
                print('->'.join(last_path))
                return last_path
            if last_node not in visited:
                visited.append(last_node)
                neighbours = graph[last_node]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        new_last_path = list(last_path)
                        new_last_path.append(neighbour)
                        stack.append(new_last_path)
            self.dfs_goal_search_path(graph, stack, visited, goal)


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
d = dfs_vertex_rec_graphtwo()
stack = ['S']
d.dfs_path_find_rec(graphtwovertex, stack, [])
stack = ['S']
d.dfs_goal_search_path(graphtwovertex, stack, [], 'G')