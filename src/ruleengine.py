import numpy as np
U64 = np.uint64

from bitboard import Bitboard

"""
class RuleEngine

- calculate possible moves
"""
class RuleEngine:
    @staticmethod
    def get_piece_type(state: list[list[U64]], selected_case: int) -> str:
        piece_type: str = ""
        
        for color in range(len(state)):
            for type in range(len(state[color])):
                if Bitboard.get_bit(state[color][type], selected_case):
                    if color == 0:
                        piece_type += 'w'
                    else:
                        piece_type += 'b'
                    
                    match type:
                        case 0:
                            piece_type += 'p'
                        case 1:
                            piece_type += 'r'
                        case 2:
                            piece_type += 'b'
                        case 3:
                            piece_type += 'k'
                        case 4:
                            piece_type += 'q'
                        case 5:
                            piece_type += 'K'
                    
                    return piece_type
    
    @staticmethod
    def is_checkmate(state) -> bool:
        pass
        return False

    @staticmethod    
    def get_moves(state: list[list[U64]], selected_case: int) -> list[int]:
        piece_type = RuleEngine.get_piece_type(state[0:2], selected_case)
        
        possible_moves = []
        
        turn: bool = None
        if piece_type[0] == 'w':
            turn = True
        else:
            turn = False
        
        if piece_type[1] == 'r':
            possible_moves = RuleEngine.get_moves_rook(state[2], selected_case, turn)
        
        return possible_moves
    
    @staticmethod
    def get_moves_rook(state: list[U64], selected_case: int, turn: bool) -> list[int]:
        possible_moves: list[int] = []
        for direction in range(0, 4):
            
            current_case: int = None
            limit_reached = False
            
            while not limit_reached:
                
                if current_case == None:
                    conditions = RuleEngine.contiditon_rook(direction, selected_case)
                    if conditions[0]:
                        current_case = selected_case + conditions[2]
                        possible_moves.append(current_case)
                    else:
                        limit_reached = True
                else:
                    conditions = RuleEngine.contiditon_rook(direction, current_case)
                    
                    if conditions[0]:
                        current_case += conditions[2]
                        possible_moves.append(current_case)
                        
                    elif conditions[1]:
                        limit_reached = True
        
        return possible_moves

    @staticmethod
    def contiditon_rook(direction, case) -> list:
        if direction == 0:
            return [case%8 > 0, case%8 == 0, -1]
        elif direction == 1:
            return [case%8 < 7, case%8 == 7, 1]
        elif direction == 2:
            return [case//8 < 7, case//8 == 7, 8]
        else:
            return [case//8 > 0, case//8 == 0, -8]