import queue

#BFS undirected graph G1 Matrix

class bfsmatrix:
    def bfsmatundirected(self, maps, matrix, root):
        visited = [root]
        queue = [root]

        while queue:
            looking_vertex_value = queue.pop(0)
            current_vertex_index = -1
            for key, value in maps.items():
                if value == looking_vertex_value:
                    current_vertex_index = key
            neighbours_index = matrix[current_vertex_index]
            index = 0
            while index < len(neighbours_index):
                if matrix[current_vertex_index][index] == 1:
                    if maps[index] not in visited:
                        visited.append(maps[index])
                        queue.append(maps[index])
                index += 1
        print('->'.join(visited))

    def bfspath(self, maps, matrix, start, goal):
        visited = [start]
        queue = [start]

        while queue:
            new_queue = queue.pop(0)
            last_node = new_queue[-1]
            if last_node == goal:
                print('->'.join(new_queue))
                return new_queue

            for key, value in maps.items():
                if value == last_node:
                    current_vertex_index = key
            neighbours_index = matrix[current_vertex_index]
            index =0

            while index < len(neighbours_index):
                if matrix[current_vertex_index][index] == 1:
                    if maps[index] not in visited:
                        visited.append(maps[index])
                        new_path_queue = list(new_queue)
                        new_path_queue.append(maps[index])
                        queue.append(new_path_queue)
                        #queue.append(maps[index])
                index += 1

maps = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H', 8 : 'P', 9 : 'Q', 10 : 'R', 11 : 'S'}
graphmat = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]

b = bfsmatrix()
b.bfsmatundirected(maps, graphmat, 'S')
b.bfspath(maps,graphmat,'S','G')