class Graph:
    def __init__(self, num_nodes, directed = True):
        self.num_nodes = num_nodes
        self.nodes = range(num_nodes)
        self.list_edges=[]
        self.directed = directed
        self.adj_matrix =[[0 for i in self.nodes] for j in self.nodes]
        self.adj_list ={node:set() for node in self.nodes}

    def add_edge_list(self, node1, node2, weight):
        self.list_edges.append([node1, node2, weight])
        if not self.directed:
            self.list_edges.append([node2, node1, weight])

    def add_adj_matrix(self, node1, node2, weight):
        self.adj_matrix[node1][node2] = weight
        if not self.directed:
            self.adj_matrix[node2][node1] = weight

    def add_adj_list(self, node1, node2, weight):
        self.adj_list[node1].Add(node2, weight)
        if not self.directed:
            self.adj_list[node2].Add(node1, weight)

    '''def dfs(self, start, target,path =[], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
            for (neighbour, weight) in self.adj_list([start]):
                if neighbour not in visited:
                    result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return path'''

    def dfs(self, start, target, path =[], visited =set()):
        path.append(start)
        visited.append(start)
        if start == target:
            return path
        for (neighbour, weight) in self.adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, weight, path,visited)
            if result is not None:
                return result
        path.pop()
        return path


    def bfs(self):
