from queue import Queue
class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
        self.m_directed = directed
        self.m_adj_list = {node: set() for node in self.m_nodes}

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))
        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    def bfs_traversal(self, start_node):
        visited = set()
        queue = Queue()
        queue.put(start_node)
        visited.add(start_node)

        while not queue.empty():
            current_node = queue.get()
            print(current_node, end = " ")
            for (next_node, weight) in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    visited.add(next_node)

graph = Graph(5, directed=False)

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)

graph.bfs_traversal(0)

# Reuslt : 0 1 2 4 3