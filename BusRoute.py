import heapq
from collections import defaultdict
# import database

def get_routes(bus_stops, source, destination):
    graph = defaultdict(list)
    for bus_stop, buses in bus_stops.items():
        for bus, next_stop in buses.items():
            graph[bus_stop].append((bus, next_stop))

    queue = [(0, source, [])]
    visited = set()
    top_routes = []

    while queue:
        cost, current_stop, route = heapq.heappop(queue)

        if current_stop == destination:
            heapq.heappush(top_routes, (cost, route))
            if len(top_routes) > 2:
                heapq.heappop(top_routes)
        elif current_stop not in visited:
            visited.add(current_stop)
            for bus, next_stop in graph[current_stop]:
                heapq.heappush(queue, (cost + 1, next_stop, route + [(bus, next_stop)]))

    return top_routes


def format_routes(routes, source):
    if not routes:
        print("No routes found.")
    else:
        for i, (cost, route) in enumerate(routes, start=1):
            print(f"Route {i}:")
            print(f"Step 1: Start at {source}")
            for j, (bus, stop) in enumerate(route, start=2):
                print(f"Step {j}: Take {bus} to {stop}")
            print(f"Total cost: {cost}\n")



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

source = input("Enter the source bus stop :")
destination = input("Enter the destination bus stop :")

routes = get_routes(bus_stops, source, destination)

format_routes(routes,source)
