import queue

class ucs_graph_three_matrix:

    def ucs_search_path(self, graph, root, goal):
        pqueue  = queue.PriorityQueue()
        visited = []
        pqueue.put((0, root))

        while pqueue:
            min_value_list = pqueue.get()
            #print(min_value_list)
            min_dis = min_value_list[0]
            path_short = min_value_list[1]
            last_node = path_short[-1]

            if last_node == goal:
                visited.append(goal)
                print('Expanded path', '->'.join(visited))
                print('lowest cost path','->'.join(path_short))
                return min_value_list

            if last_node not in visited:
                visited.append(last_node)
                for neighbour, distance in graph[last_node].items():
                    new_min_dis = distance
                    new_min_value_list = list(path_short)
                    new_min_value_list.append(neighbour)
                    pqueue.put((new_min_dis, new_min_value_list))


graphV = {'S' : {'D' : 7, 'E' : 5, 'P' : 14},
    'A' : {'B' : 7, 'C' : 4},
    'B' : {'A' : 5, 'D' : 7},
    'C' : {'A' : 5, 'D' : 7, 'F' : 2},
    'D' : {'B' : 7, 'C' : 4, 'E' : 5, 'S' : 70},
    'E' : {'D' : 7, 'H' : 11, 'R' : 3, 'S' : 70},
    'F' : {'C' : 4, 'G' : 0, 'R' :3},
    'G' : {'F' : 2},
    'H' : {'E' : 5, 'P' : 14, 'Q' : 12},
    'P' : {'H' : 11, 'Q' : 12, 'S' : 70},
    'Q' : {'H' : 11, 'P' : 14},
    'R' : {'E' : 5, 'F' : 2}}


u = ucs_graph_three_matrix()
u.ucs_search_path(graphV, 'S', 'G')