import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))


def dijkstra(graph, start_node):
    weights = {node: float('infinity') for node in graph.nodes}
    weights[start_node] = 0

    heap = [(0, start_node)]
    heapq.heapify(heap)

    while heap:
        current_weight, current_node = heapq.heappop(heap)

        for neighbor, weight_sum in graph.edges[current_node]:
            weight_sum = current_weight + weight_sum
            if weight_sum < weights[neighbor]:
                weights[neighbor] = weight_sum
                heapq.heappush(heap, (weight_sum, neighbor))

    return weights


# Приклад використання:
if __name__ == "__main__":
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)

    start_node = "A"

    shortest_paths = dijkstra(g, start_node)

    for node, distance in shortest_paths.items():
        print(f"Shortest path from {start_node} to {node}: {distance}")
