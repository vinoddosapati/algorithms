import queue

#Graph 2 directed vertexlist BFS

class bfsgraphtwoundirect:
    def bfsvertex(self, graph, root):
        visited = [root]
        queue = [root]

        while queue:
            looking_vertex = queue.pop(0)
            vertex_neighbours = sorted(graph[looking_vertex])
            #print('current vertex: ', looking_vertex, ' and its neighbours: ', vertex_neighbours)
            for neighbour in vertex_neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
        print('->'.join(visited))

    def bfs_path(self, graph, root, goal):
        currentlist = [root]
        queue = [root]

        while queue:
            new_queue = queue.pop(0)
            last_node = new_queue[-1]
            if last_node == goal:
                print('->'.join(new_queue))
                return new_queue
            for neighbour in sorted(graph[last_node]):
                currentlist.append(last_node)
                if neighbour not in currentlist:
                    new_list_path = list(new_queue)
                    new_list_path.append(neighbour)
                    queue.append(new_list_path)

graphtwovertex = {
    'A' : [],
    'B' : ['A'],
    'C' : ['A'],
    'D' : ['B', 'C', 'E'],
    'E' : ['H', 'R'],
    'F' : ['C', 'G'],
    'G' : [],
    'H' : ['P', 'Q'],
    'P' : ['Q'],
    'Q' : [],
    'R' : ['F'],
    'S' : ['D', 'E', 'P']
}

b = bfsgraphtwoundirect()
b.bfsvertex(graphtwovertex, 'S')
b.bfs_path(graphtwovertex,'S','G')