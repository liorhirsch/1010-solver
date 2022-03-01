from itertools import product
from typing import List

import numpy as np

from .BoardPiece import BoardPiece, ALL_AVAILABE_PIECES


class Board1010:
    def __init__(self, size=10, num_of_pieces_in_each_step=3):
        self.size = size
        self.num_of_pieces_in_each_step = num_of_pieces_in_each_step
        self.board_matrix = np.zeros((self.size, self.size))
        self.available_actions: List[BoardPiece] = []

    def peek_make_move(self, action_index, location):
        board_copy = self.board_matrix.copy()
        available_actions_copy = self.available_actions.copy()

        board_after_move = self.make_move(action_index, location).copy()

        self.board_matrix = board_copy
        self.available_actions = available_actions_copy
        return board_after_move

    def make_move(self, action_index, location: np.array):
        if action_index >= len(self.available_actions):
            raise Exception("Not Valid action index!")

        chosen_action = self.available_actions[action_index]
        output = self.__put_piece(chosen_action, location)

        if output is None:
            raise Exception("Invalid action")

        self.available_actions = np.delete(self.available_actions, action_index)
        return output

    def __put_piece(self, piece: BoardPiece, location: np.array):
        is_valid = self.is_action_valid(piece, location)

        if not is_valid:
            return None

        piece_shape = piece.piece_matrix.shape
        piece_reach_loc = location + piece_shape

        self.board_matrix[location[0]: piece_reach_loc[0], location[1]: piece_reach_loc[1]] += piece.piece_matrix
        self.__clear_full_rows_cols()
        return self.board_matrix

    def __clear_full_rows_cols(self):
        rows_to_clear = np.where(np.sum(self.board_matrix, axis=1) == self.size)
        print(rows_to_clear)
        cols_to_clear = np.where(np.sum(self.board_matrix, axis=0) == self.size)
        print(cols_to_clear)

        self.board_matrix[rows_to_clear, :] = 0
        self.board_matrix[:, cols_to_clear] = 0

    def is_action_valid(self, piece: BoardPiece, location: np.array):
        if type(location) is not np.array:
            location = np.array(location)

        piece_shape = piece.piece_matrix.shape
        piece_reach_location = location + piece_shape
        is_inside_board = np.all(piece_reach_location <= self.size)

        if not is_inside_board:
            return False

        joint_area_to_piece_location = self.board_matrix[location[0]: piece_reach_location[0],
                                       location[1]: piece_reach_location[1]]
        return np.all((joint_area_to_piece_location + piece.piece_matrix) < 2)

    def sample_possible_actions(self):
        if len(self.available_actions) > 0:
            raise Exception("available_actions is not clear yet")

        sampled_pieces_indexes = np.random.randint(0, len(ALL_AVAILABE_PIECES), self.num_of_pieces_in_each_step)
        self.available_actions = ALL_AVAILABE_PIECES[sampled_pieces_indexes]

    def is_game_over(self):
        all_possible_locations = product(range(10), range(10))

        for curr_possible_piece in self.available_actions:
            if not any(map(lambda loc: self.is_action_valid(curr_possible_piece, loc), all_possible_locations)):
                return True

        return False
