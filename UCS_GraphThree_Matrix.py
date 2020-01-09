import queue


class dfs_matrix_graphthree:
    def dfs_short_path_matrix(self, map, graph, root, goal):
        pqueue = queue.PriorityQueue()
        pqueue.put((0, root))
        visited = []
        while pqueue:
            short_path = pqueue.get()
            dis_short_path = short_path[0]
            path_min = short_path[1]
            last_node = path_min[-1]
            last_node_index = -1
            if last_node == goal:
                visited.append(goal)
                print('->'.join(visited))
                print('->'.join(path_min))
                return path_min
            for key, value in map.items():
                if value == last_node:
                    last_node_index = key
            neighbours = graph[last_node_index]
            if last_node not in visited:
                visited.append(last_node)
                temp_Iteration = 0
                while temp_Iteration < len(neighbours):
                    if neighbours[temp_Iteration] > 0:
                        neighbour = map[temp_Iteration]
                        distance = neighbours[temp_Iteration]
                        if neighbour not in visited:
                            new_short_path = list(path_min)
                            new_short_path.append(neighbour)
                            new_min_dis = dis_short_path + distance
                            pqueue.put((new_min_dis, new_short_path))
                    temp_Iteration += 1



maps = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'P', 9: 'Q', 10: 'R', 11: 'S'}
graphmat = [[0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 8, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 1, 8, 0, 2, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 2, 0, 0, 0, 8, 0, 0, 2, 9],
            [0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0, 4, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 15, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 4, 15, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 9, 0, 0, 0, 1, 0, 0, 0]]

u = dfs_matrix_graphthree()
u.dfs_short_path_matrix(maps, graphmat, 'S', 'G')