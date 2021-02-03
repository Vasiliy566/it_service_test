from unittest import TestCase
import numpy as np
from pathlib import Path
import datetime
import logging

from app.src.find_distance import reformat_adj_matrix, dijkstra

logger = logging.getLogger(__name__)

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

    def test_performance_dijkstra(self):
        for item in [test_distances, np.load(open(file_to_open, "rb"))]:
            start_time = datetime.datetime.now()
            dijkstra(0, len(item) - 1, reformat_adj_matrix(item))
            end_time = datetime.datetime.now()
            logger.info(f"{end_time - start_time} takes to calculate dijkstra on {len(item)}x{len(item[0])} adj matrix")
