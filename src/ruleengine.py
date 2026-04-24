import numpy as np
U64 = np.uint64

from bitboard import Bitboard

from random import randint

"""
class RuleEngine

- calculate possible moves
"""
class RuleEngine:
    @staticmethod
    def is_checkmate(state) -> bool:
        pass
        return False

    @staticmethod    
    def get_moves(state: list[U64]) -> list[int]:
        possible_moves = []
        
        for i in range(0, 5):
            possible_moves.append(randint(0, 63))
        
        return possible_moves