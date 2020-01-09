import queue


class astaralgo:
    def astaralgopath(self, h, graph, root, goal):
        pqueue = queue.PriorityQueue()
        pqueue.put((0, 0, root))
        visited = []
        while pqueue:
            priority_node = pqueue.get()
            #print(priority_node)
            last_path = priority_node[2]
            last_node = last_path[-1]
            dist_before = priority_node[1]
            total_cost = priority_node[0]

            if last_node == goal:
                visited.append(goal)
                print('->'.join(visited))
                print('->'.join(last_path))
                break

            if last_node not in visited:
                visited.append(last_node)
                #print(visited)
                for neighbour, distance in graph[last_node].items():
                    h_n = h[neighbour]
                    new_dist_before = dist_before + distance
                    new_total_cost = new_dist_before + h_n
                    new_last_path = list(last_path)
                    new_last_path.append(neighbour)
                    pqueue.put((new_total_cost, new_dist_before, new_last_path))


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

h = {'A' : 5,'B' : 7,'C' : 4,'D' : 7,'E' : 5,'F' : 2,'G' : 0,'H' : 11,'P' : 14,'Q' : 12,'R' : 3,'S' : 0}

astar = astaralgo()
astar.astaralgopath(h, graphV, 'S', 'G')