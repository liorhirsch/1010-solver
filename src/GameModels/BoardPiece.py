from typing import List

import numpy as np


class BoardPiece:
    def __init__(self, piece_matrix, piece_index):
        self.piece_matrix: np.array = piece_matrix
        self.score: int = self.piece_matrix.sum()
        self.piece_index = piece_index

    def __repr__(self):
        return f"\n {str(self.piece_matrix)} \n"

long_5_piece = np.ones((1, 5))
long_4_piece = np.ones((1, 4))
long_3_piece = np.ones((1, 3))
long_2_piece = np.ones((1, 2))
long_1_piece = np.ones((1, 1))
full_3X3 = np.ones((3, 3))
full_2X2 = np.ones((2, 2))
reish = np.array([[1, 0], [1, 1]])

all_available_pieces_as_numpy = [
    long_5_piece,
    long_5_piece.T,
    long_4_piece,
    long_4_piece.T,
    long_3_piece,
    long_3_piece.T,
    long_2_piece,
    long_2_piece.T,
    long_1_piece,
    full_3X3,
    full_2X2,
    reish,
    np.rot90(reish),
    reish.T,
    np.rot90(reish.T)
]
ALL_AVAILABE_PIECES = np.array(list(map(lambda x: BoardPiece(x[1], x[0]), enumerate(all_available_pieces_as_numpy))))
