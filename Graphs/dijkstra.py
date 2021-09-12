graph = { "a" : {'b':3,'c':4,'d':7},
          "b" : {'c':1, "f":5},
          "c" : {'f':6, "d":2},
          "d" : {'e':3, "g":6},
          "e" : {'g':3, "h":4},
          "f" : {'e':1, "h":8},
          'g' : {'h':2},
          'h' : {'g':2}
        }  
def dijkstra(graph,start,goal):

    shortest_dist = {}
    track_unvivsted = {}
    unvisited_nodes = graph
    infinity = 999999
    track_path = []

# Assigning infinity and 0 to starting and other nodes
    for node in unvisited_nodes:
        shortest_dist[node] = infinity
    shortest_dist[start] = 0

    while unvisited_nodes:

        # Checking minimum distance node and swapping it with shortest distance
        min_distance_node = None

        for node in unvisited_nodes:
            if min_distance_node is None:
                min_distance_node =  node
            elif shortest_dist[node] < shortest_dist[min_distance_node]:
                min_distance_node = node
        

        # checking and swapping minimum weight and relaxation of visited node

        path_options = graph[min_distance_node].items()

        for child_node,weight in path_options:
            if weight + shortest_dist[min_distance_node] < shortest_dist[child_node]:
                shortest_dist[child_node] = weight+shortest_dist[min_distance_node]
            
        unvisited_nodes.pop(min_distance_node)

        # Tracing optimal path 

    current_node = goal

    while current_node != start:
        try:
            track_path.insert(0,current_node)
            current_node = track_unvivsted[current_node]
            
        except KeyError:
            print("Shortest Path unreachable")
            break

    track_path.insert(0,start)

    # Ending condition for the algorithm
    if shortest_dist[goal] != infinity:
        print("Shortest Distance",str(shortest_dist[goal]))
        print("Path:",str(track_path))


dijkstra(graph,'a','h') 