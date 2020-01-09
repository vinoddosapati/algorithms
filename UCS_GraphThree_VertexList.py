import queue

class ucs_graph_three_matrix:

    def ucs_search_path(self, graph, root, goal):
        pqueue  = queue.PriorityQueue()
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
                    new_min_dis = min_dis+distance
                    new_min_value_list = list(path_short)
                    new_min_value_list.append(neighbour)
                    pqueue.put((new_min_dis, new_min_value_list))


graphV = {'S' : {'D' : 3, 'E' : 9, 'P' : 1},
    'A' : {'B' : 2, 'C' : 2},
    'B' : {'A' : 2, 'D' : 1},
    'C' : {'A' : 2, 'D' : 8, 'F' : 3},
    'D' : {'B' : 1, 'C' : 8, 'E' : 2, 'S' : 3},
    'E' : {'D' : 2, 'H' : 8, 'R' : 2, 'S' : 9},
    'F' : {'C' : 3, 'G' : 2, 'R' :2},
    'G' : {'F' : 2},
    'H' : {'E' : 8, 'P' : 4, 'Q' : 4},
    'P' : {'H' : 4, 'Q' : 15, 'S' : 1},
    'Q' : {'H' : 4, 'P' : 15},
    'R' : {'E' : 2, 'F' : 2}}


u = ucs_graph_three_matrix()
u.ucs_search_path(graphV, 'S', 'G')