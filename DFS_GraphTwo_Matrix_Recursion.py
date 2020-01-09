from inspect import stack


class dfs_rec_graphtwo_matrix:
    def dfs_extendpath_rec_matrix(self, map, graph, stack, visited):
        if stack:
            last_node = stack.pop()
            if last_node not in visited:
                visited.append(last_node)
                current_node_key = -1
                for key, value in map.items():
                    if value == last_node:
                        current_node_key = key
                neighbours_loc = graph[current_node_key]
                index = 0
                while index < len(neighbours_loc):
                    if neighbours_loc[index] == 1:
                        neighbour = map[index]
                        if neighbour not in visited:
                            stack.append(neighbour)
                    index += 1
            self.dfs_extendpath_rec_matrix(map, graph, stack, visited)
        else:
            print('->'.join(visited))


    def dfs_matrix_rec_path_two(self, map, graph, stack, visited, goal):
        if stack:
            last_path = stack.pop()
            last_node = last_path[-1]
            if last_node not in visited:
                visited.append(last_node)
                if last_node == goal:
                    print('->'.join(last_path))
                    return last_path

                current_node_key = -1
                for key, value in map.items():
                    if value == last_node:
                        current_node_key = key
                neighbours_loc = graph[current_node_key]
                index = 0
                while index < len(neighbours_loc):
                    if neighbours_loc[index] == 1:
                        neighbour = map[index]
                        if neighbour not in visited:
                            new_last_path = list(last_path)
                            new_last_path.append(neighbour)
                            stack.append(new_last_path)
                    index += 1
            self.dfs_matrix_rec_path_two(map, graph, stack, visited, goal)
        else:
            print('Cant find goal')



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

d = dfs_rec_graphtwo_matrix()
stack = ['S']
d.dfs_extendpath_rec_matrix(maps, graphtwomatrix, stack, [])
stack = ['S']
d.dfs_matrix_rec_path_two(maps, graphtwomatrix, stack, [], 'G')