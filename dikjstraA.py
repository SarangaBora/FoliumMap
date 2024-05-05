import heapq
from collections import defaultdict

def dijkstra(graph, source):
    distances = defaultdict(lambda: float('inf'))
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        dist_u, u = heapq.heappop(queue)
        if dist_u > distances[u]:
            continue
        for v, weight in graph[u]:
            if dist_u + weight < distances[v]:
                distances[v] = dist_u + weight
                heapq.heappush(queue, (distances[v], v))
    return distances

def get_routes(bus_stops, source, destination):
    graph = defaultdict(list)
    for bus_stop, buses in bus_stops.items():
        for bus, next_stop in buses.items():
            graph[bus_stop].append((next_stop, 1))  # Assuming each bus ride has a cost of 1

    distances = dijkstra(graph, source)
    shortest_distance = distances[destination]
    shortest_path = [destination]
    while shortest_path[-1] != source:
        shortest_path.append(min(graph[shortest_path[-1]], key=lambda x: distances[x[0]])[0])
    shortest_path.reverse()
    
    # Finding the buses to take along the shortest path
    buses_to_take = []
    current_stop = shortest_path[0]
    for next_stop in shortest_path[1:]:
        for bus, next_stop_bus in bus_stops[current_stop].items():
            if next_stop_bus == next_stop:
                buses_to_take.append((bus, current_stop, next_stop))
                break
        current_stop = next_stop
    
    return shortest_distance, buses_to_take


def format_routes(shortest_distance, buses_to_take, source, destination):
    if shortest_distance == float('inf'):
        print("No routes found.")
    else:
        print(f"Optimal route from {source} to {destination} (Distance: {shortest_distance} stops):")
        for i, (bus, source_stop, dest_stop) in enumerate(buses_to_take, start=1):
            print(f"Step {i}: Take {bus} from {source_stop} to {dest_stop}")
        print("\n")

# bus_stops = {
#     'A': {'Bus1': 'B', 'Bus2': 'C'},
#     'B': {'Bus1': 'A', 'Bus2': 'D', 'Bus3': 'E','Bus6':'G'},
#     'C': {'Bus2': 'A', 'Bus3': 'F'},
#     'D': {'Bus1': 'B', 'Bus4': 'G'},
#     'E': {'Bus3': 'B', 'Bus4': 'H'},
#     'F': {'Bus2': 'C'},
#     'G': {'Bus1': 'D','Bus6':'B'},
#     'H': {'Bus4': 'E','Bus5':'I'},
#     'I': {'Bus5':'H'}
# }

bus_stops = {                   #This is also a python dictionary
    'A': {'Bus1': 'B', 'Bus2': 'C'},
    'B': {'Bus1': 'A', 'Bus2': 'D', 'Bus3': 'E'},
    'C': {'Bus2': 'A', 'Bus3': 'F'},
    'D': {'Bus1': 'B', 'Bus4': 'G'},
    'E': {'Bus3': 'B', 'Bus4': 'H'},
    'F': {'Bus2': 'C'},
    'G': {'Bus1': 'D'},
    'H': {'Bus4': 'E','Bus5':'I'},
    'I': {'Bus5':'A'}
}
source = input("Enter the source bus stop: ")
destination = input("Enter the destination bus stop: ")

shortest_distance, buses_to_take = get_routes(bus_stops, source, destination)

format_routes(shortest_distance, buses_to_take, source, destination)
