from unittest import TestCase
import numpy as np
from pathlib import Path

from app.src.find_distance import reformat_adj_matrix, dijkstra

data_folder = Path("app/data/")
file_to_open = data_folder / "matrix_distance"
test_distances = np.array([(0, 5, 2, 0), (5, 0, 2, 1), (2, 2, 0, 15), (0, 1, 15, 0)])


class Test(TestCase):
    def test_reformat_adj_matrix(self):
        distances = test_distances
        zeros_in_matrix = len(np.where(distances == 0))
        distances = reformat_adj_matrix(distances)
        assert zeros_in_matrix == len(np.where(distances == np.inf))

    def test_dijkstra_distance(self):
        distances = reformat_adj_matrix(test_distances)
        distance, _ = dijkstra(0, 3, distances)
        assert distance == 5.0

    def test_dijkstra_path(self):
        distances = reformat_adj_matrix(test_distances)
        _, path = dijkstra(0, 3, distances)
        assert path == [0, 2, 1, 3]

