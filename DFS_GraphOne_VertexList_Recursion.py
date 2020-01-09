from inspect import stack


class dfs_rec_graphone_vertex:
    def dfs_expand_path(self, graph, stack, visited):
        if stack:
            last_node = stack.pop()
            if last_node not in visited:
                visited.append(last_node)
                neighbours = graph[last_node]
                for neighbour in neighbours:
                    if neighbour not in visited:
                        stack.append(neighbour)
            self.dfs_expand_path(graph, stack, visited)
        else:
            print('->'.join(visited))

    def dfs_goal_path(self, graph, stack, visited, goal):
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
            self.dfs_goal_path(graph, stack, visited, goal)

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
d = dfs_rec_graphone_vertex()
stack = ['S']
d.dfs_expand_path(graphVertex, stack, [])
stack = ['S']
d.dfs_goal_path(graphVertex, stack, [], 'G')