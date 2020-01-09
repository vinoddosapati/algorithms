import queue

#graph four directed UCS vertex

class ucs_graphfour_matrix:
    def uccs_matrix_path(self, graph, root, goal):
        pqueue = queue.PriorityQueue()
        visited = []
        pqueue.put((0, root))

        while pqueue:
            min_value_list = pqueue.get()
            min_dis = min_value_list[0]
            path_short = min_value_list[1]
            last_node = path_short[-1]

            if last_node == goal:
                visited.append(goal)
                print('->'.join(visited))
                print('->'.join(path_short))
                return min_value_list

            if last_node not in visited:
                visited.append(last_node)
                for neighbour, distance in graph[last_node].items():
                    new_min_dis = min_dis + distance
                    new_min_value_list = list(path_short)
                    new_min_value_list.append(neighbour)
                    pqueue.put((new_min_dis, new_min_value_list))


graph = {
	'A': {},
    'B': {'A' :2 },
    'C': {'A' : 2},
    'D': {'B' : 1, 'C' : 8, 'E' : 2},
    'E': {'H' : 8, 'R' : 2},
    'F': {'C' : 3, 'G' : 2},
    'G': {},
    'H': {'P' : 4, 'Q' : 4},
    'P': {'Q' : 15},
    'Q': {},
    'R': {'F' : 2},
    'S': {'D' : 3, 'E' : 9, 'P' : 1}
	}

u = ucs_graphfour_matrix()
u.uccs_matrix_path(graph, 'S', 'G')