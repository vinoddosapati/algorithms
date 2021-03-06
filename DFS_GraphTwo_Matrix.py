class dfs_graph_two_matrix:
    def dfs_matrix(self,maps, graph, root):
        visited = []
        stack = [root]

        while stack:
            current_node = stack.pop()
            current_index = -1
            if current_node not in visited:
                visited.append(current_node)
                for key, value in maps.items():
                    if value == current_node:
                        current_index = key
                index = 0
                while index < len(graph[current_index]):
                    if graph[current_index][index] == 1:
                        stack.append(maps[index])
                    index += 1

        print('->'.join(visited))

    def dfs_path_end(self, map, graph, root, goal):
        visited = []
        stack = [root]

        while stack:
            #print(stack)
            new_path = stack.pop()
            last_node = new_path[-1]
            if last_node == goal:
                print('->'.join(new_path))
                return new_path
            last_node_index = -1
            if last_node not in visited:
                visited.append(last_node)
                for key, value in map.items():
                    if value == last_node:
                        last_node_index = key
                index = 0
                while index < len(graph[last_node_index]):
                    if graph[last_node_index][index] == 1:
                        new_path_stack = list(new_path)
                        new_path_stack.append(map[index])
                        stack.append(new_path_stack)
                    index += 1

maps = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H', 8 : 'P', 9 : 'Q', 10 : 'R', 11 : 'S'}
graphtwomatrix = [[0,0,0,0,0,0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0,0,0,0,0,0],
                  [0,1,1,0,1,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,1,0,0,1,0],
                  [0,0,1,0,0,0,1,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,1,1,0,0],
                  [0,0,0,0,0,0,0,0,0,1,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,1,0,0,0,0,0,0],
                  [0,0,0,1,1,0,0,0,1,0,0,0]]

g = dfs_graph_two_matrix()
g.dfs_matrix(maps, graphtwomatrix, 'S')
g.dfs_path_end(maps, graphtwomatrix, 'S', 'G')