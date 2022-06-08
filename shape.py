from typing import NamedTuple, List, Tuple
import numpy as np


class Shape:
    '''Tis class will be used for create shapes for game tetris'''
    def __init__(self,
                 position: list[int],
                 body: list[list[int]],
                 fill_simbol='0'):
        self.position = position
        self.body = body
        self.fill_simbol = fill_simbol

    def _rotate(self, matrix: list[list[int]]):
        self.body = np.dot(self.body, matrix)

    def rotate_right(self):
        right_matrix = [[0, 1],
                        [-1, 0]]
        self._rotate(right_matrix)

    def rotate_left(self):
        left_matrix = [[0, -1],
                       [1, 0]]
        self._rotate(left_matrix)

    def _move_to(self, new_coord: list[int]):
        self.position = new_coord

    def step_down(self):
        x = self.position[0]
        y = self.position[1]
        self._move_to([x, y+1])

    def get_absolute_coords(self) -> list[list[int]]:
        return np.array(self.position) + np.array(self.body)


