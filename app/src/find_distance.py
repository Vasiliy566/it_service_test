import numpy as np
# reference - https://github.com/Vasiliy566/PolitekhArchive/tree/master/Dejkstra

def get_path(start_vertex, end_vertex, parent):
    path = [end_vertex]
    cur_vertex = end_vertex
    while not cur_vertex == start_vertex:
        path.append(parent[cur_vertex])
        cur_vertex = parent[cur_vertex]
    return path


# !matrix should be a symmetric!
def dijkstra(start_vertex, end_vertex, matrix):
    N = len(matrix[0])
    valid = [True] * N
    weight = [np.inf] * N
    weight[start_vertex] = 0
    parent = [-1] * N
    for i in range(N):
        min_weight = np.inf
        ID_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
                parent[i] = ID_min_weight
        valid[ID_min_weight] = False
    return weight[end_vertex], get_path(start_vertex, end_vertex, parent)[::-1]


def reformat_adj_matrix(matrix):
    return np.where(matrix == 0, np.inf, matrix)
