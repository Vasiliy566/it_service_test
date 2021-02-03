import numpy as np
# reference - https://github.com/Vasiliy566/PolitekhArchive/tree/master/Dejkstra

# calculate path from saved parent
def get_path(start_vertex, end_vertex, parent):
    path = [end_vertex]
    cur_vertex = end_vertex
    while not cur_vertex == start_vertex:
        path.append(parent[cur_vertex])
        cur_vertex = parent[cur_vertex]
    return path


def dijkstra(start_vertex, end_vertex, matrix):
    if start_vertex >= len(matrix) or end_vertex >= len(matrix) or start_vertex < 0 or end_vertex < 0:
        raise Exception("wrong indexes of start and finish vertexes")
    n = len(matrix[0])
    valid = [True] * n
    weight = [np.inf] * n
    weight[start_vertex] = 0
    parent = [-1] * n
    for i in range(n):
        min_weight = np.inf
        id_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                id_min_weight = i
        for i in range(n):
            if weight[id_min_weight] + matrix[id_min_weight][i] < weight[i]:
                weight[i] = weight[id_min_weight] + matrix[id_min_weight][i]
                parent[i] = id_min_weight
        valid[id_min_weight] = False
    return weight[end_vertex], get_path(start_vertex, end_vertex, parent)[::-1]


# replace all zeroes (means not path between vertexes) with inf
def reformat_adj_matrix(matrix):
    return np.where(matrix == 0, np.inf, matrix)
