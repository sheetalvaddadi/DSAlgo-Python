class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.directed = directed

        self.list_of_edges = []
        self.adj_matrix = [[0 for i in range(self.num_of_nodes)] for j in range(self.num_of_nodes)]
        self.adj_list = {node: set() for node in range(self.num_of_nodes)}

    def add_edge(self, node1, node2, weight=1):
        self.list_of_edges.append([node1, node2, weight])

        if (not self.directed):
            self.list_of_edges.append([node1, node2, weight])

    def add_edge_adj_matrix(self, node1, node2, weight=1):
        self.adj_matrix[node1][node2] = weight

        if (not self.directed):
            self.adj_matrix[node2][node1] = weight

    def add_edge_adj_list(self, node1, node2, weight=1):
        self.adj_list[node1].add((node2, weight))

        if (not self.directed):
            self.adj_list[node2].add((node1, weight))

    def print_edge_list(self):
        num_of_edges = len(self.list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i + 1, ": ", self.list_of_edges[i])

    def print_adj_matrix(self):
        print(self.adj_matrix)

    def print_adj_list(self):
        for key in self.adj_list.keys():
            print("node", key, ": ", self.adj_list[key])

if __name__ =="__main__":
    graph = Graph(5)

    graph.add_edge(0, 0, 25)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 15)
    graph.add_edge(4, 2, 7)
    graph.add_edge(4, 3, 11)
    graph.print_edge_list()

    print("-------------------------")

    graph.add_edge_adj_matrix(0, 0, 25)
    graph.add_edge_adj_matrix(0, 1, 5)
    graph.add_edge_adj_matrix(0, 2, 3)
    graph.add_edge_adj_matrix(1, 3, 1)
    graph.add_edge_adj_matrix(1, 4, 15)
    graph.add_edge_adj_matrix(4, 2, 7)
    graph.add_edge_adj_matrix(4, 3, 11)
    graph.print_adj_matrix()

    print("-------------------------")

    graph.add_edge_adj_list(0, 0, 25)
    graph.add_edge_adj_list(0, 1, 5)
    graph.add_edge_adj_list(0, 2, 3)
    graph.add_edge_adj_list(1, 3, 1)
    graph.add_edge_adj_list(1, 4, 15)
    graph.add_edge_adj_list(4, 2, 7)
    graph.add_edge_adj_list(4, 3, 11)

    graph.print_adj_list()
