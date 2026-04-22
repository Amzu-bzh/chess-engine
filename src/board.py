import numpy as np
U64 = np.uint64

from bitboard import Bitboard

"""
Board class

- save state of the game
- manage piece display

Bitboards
index 0 -> bottom left
index 63 -> top right
"""
class Board:
    def __init__(self):
        self.wp = U64(0)
        self.wk = U64(0)
        self.wb = U64(0)
        self.wr = U64(0)
        self.wq = U64(0)
        self.wK = U64(0)
        
        self.bp = U64(0)
        self.bk = U64(0)
        self.bb = U64(0)
        self.br = U64(0)
        self.bq = U64(0)
        self.bK = U64(0)

        self.init_pieces()
    
    def init_pieces(self):
        for i in range(0, 8):
            self.init_pawns(i)
            self.init_knights(i)
            self.init_bishops(i)
            self.init_rooks(i)
            self.init_queens(i)
            self.init_kings(i)
            
    def init_pawns(self, i: int) -> None:
        self.wp = Bitboard.set_bit(self.wp, 8+i)
        self.bp = Bitboard.set_bit(self.bp, 48+i)

    def init_knights(self, i: int) -> None:
        if i == 0 or i == 7:
            self.wk = Bitboard.set_bit(self.wk, i)
            self.bk = Bitboard.set_bit(self.bk, 56+i)
    
    def init_bishops(self, i: int) -> None:
        if i == 1 or i == 6:
            self.wb = Bitboard.set_bit(self.wb, i)
            self.bb = Bitboard.set_bit(self.bb, 56+i)
    
    def init_rooks(self, i: int) -> None:
        if i == 2 or i == 5:
            self.wr = Bitboard.set_bit(self.wr, i)
            self.br = Bitboard.set_bit(self.br, 56+i)
    
    def init_queens(self, i: int) -> None:
        if i == 3:
            self.wq = Bitboard.set_bit(self.wq, i)
            self.bq = Bitboard.set_bit(self.bq, 56+i)
    
    def init_kings(self, i: int) -> None:
        if i == 4:
            self.wK = Bitboard.set_bit(self.wK, i)
            self.bK = Bitboard.set_bit(self.bK, 56+i)
