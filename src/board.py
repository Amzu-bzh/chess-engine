import numpy as np
U64 = np.uint64

from pyglet.shapes import Rectangle
from pyglet.image import load
from pyglet.sprite import Sprite

from bitboard import Bitboard

CASE_SIZE = 128

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
        self.init_sprites()
    
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
        if i == 2 or i == 5:
            self.wk = Bitboard.set_bit(self.wk, i)
            self.bk = Bitboard.set_bit(self.bk, 56+i)
    
    def init_bishops(self, i: int) -> None:
        if i == 1 or i == 6:
            self.wb = Bitboard.set_bit(self.wb, i)
            self.bb = Bitboard.set_bit(self.bb, 56+i)
    
    def init_rooks(self, i: int) -> None:
        if i == 0 or i == 7:
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

    def init_sprites(self):
        i_wp = load("assets/white-pawn.png")
        i_wk = load("assets/white-knight.png")
        i_wb = load("assets/white-bishop.png")
        i_wr = load("assets/white-rook.png")
        i_wq = load("assets/white-queen.png")
        i_wK = load("assets/white-king.png")
        
        self.s_wp = Sprite(i_wp)
        self.s_wk = Sprite(i_wk)
        self.s_wb = Sprite(i_wb)
        self.s_wr = Sprite(i_wr)
        self.s_wq = Sprite(i_wq)
        self.s_wK = Sprite(i_wK)
        
        i_bp = load("assets/black-pawn.png")
        i_bk = load("assets/black-knight.png")
        i_bb = load("assets/black-bishop.png")
        i_br = load("assets/black-rook.png")
        i_bq = load("assets/black-queen.png")
        i_bK = load("assets/black-king.png")
        
        self.s_bp = Sprite(i_bp)
        self.s_bk = Sprite(i_bk)
        self.s_bb = Sprite(i_bb)
        self.s_br = Sprite(i_br)
        self.s_bq = Sprite(i_bq)
        self.s_bK = Sprite(i_bK)     
    
    def draw(self):
        self.draw_grid()
        self.draw_pieces()
    
    def draw_grid(self):
        for i in range(0, 4):
            for j in range(0, 8):
                x = j%8
                y = j//8 + i*2
                if x%2 == 0:
                    Rectangle(x*CASE_SIZE, (y*CASE_SIZE)+128, CASE_SIZE, CASE_SIZE, (255, 206, 158, 255)).draw()
                    Rectangle(x*CASE_SIZE, (y*CASE_SIZE), CASE_SIZE, CASE_SIZE, (209, 139, 71, 255)).draw()
                else:
                    Rectangle(x*CASE_SIZE, (y*CASE_SIZE), CASE_SIZE, CASE_SIZE, (255, 206, 158, 255)).draw()
                    Rectangle(x*CASE_SIZE, (y*CASE_SIZE)+128, CASE_SIZE, CASE_SIZE, (209, 139, 71, 255)).draw()
    
    def draw_pieces(self):
        for i in range(0, 64):
            x = CASE_SIZE * (i%8)
            y = CASE_SIZE * (i//8)
            
            if Bitboard.get_bit(self.wp, i):
                self.s_wp.x = x
                self.s_wp.y = y
                self.s_wp.draw()
            if Bitboard.get_bit(self.wk, i):
                self.s_wk.x = x
                self.s_wk.y = y
                self.s_wk.draw()
            if Bitboard.get_bit(self.wb, i):
                self.s_wb.x = x
                self.s_wb.y = y
                self.s_wb.draw()
            if Bitboard.get_bit(self.wr, i):
                self.s_wr.x = x
                self.s_wr.y = y
                self.s_wr.draw()
            if Bitboard.get_bit(self.wq, i):
                self.s_wq.x = x
                self.s_wq.y = y
                self.s_wq.draw()
            if Bitboard.get_bit(self.wK, i):
                self.s_wK.x = x
                self.s_wK.y = y
                self.s_wK.draw()
            
            if Bitboard.get_bit(self.bp, i):
                self.s_bp.x = x
                self.s_bp.y = y
                self.s_bp.draw()
            if Bitboard.get_bit(self.bk, i):
                self.s_bk.x = x
                self.s_bk.y = y
                self.s_bk.draw()
            if Bitboard.get_bit(self.bb, i):
                self.s_bb.x = x
                self.s_bb.y = y
                self.s_bb.draw()
            if Bitboard.get_bit(self.br, i):
                self.s_br.x = x
                self.s_br.y = y
                self.s_br.draw()
            if Bitboard.get_bit(self.bq, i):
                self.s_bq.x = x
                self.s_bq.y = y
                self.s_bq.draw()
            if Bitboard.get_bit(self.bK, i):
                self.s_bK.x = x
                self.s_bK.y = y
                self.s_bK.draw()
    
    def white_pieces_bb(self):
        return self.wp | self.wk | self.wb | self.wr | self.wq | self.wK
    
    def black_pieces_bb(self):
        return self.bp | self.bk | self.bb | self.br | self.bq | self.bK

    def pieces(self):
        return self.white_pieces_bb() | self.black_pieces_bb()
    
    def is_piece(self, square: int):
        pieces_bb = self.white_pieces_bb() | self.black_pieces_bb()
        
        return Bitboard.get_bit(pieces_bb, square)
    
    def move(self, start_square: int, end_square: int):
        # White piece is captured
        if Bitboard.get_bit(self.wp, end_square):
            self.wp = Bitboard.clear_bit(self.wp, end_square)
        elif Bitboard.get_bit(self.wk, end_square):
            self.wk = Bitboard.clear_bit(self.wk, end_square)
        elif Bitboard.get_bit(self.wb, end_square):
            self.wb = Bitboard.clear_bit(self.wb, end_square)
        elif Bitboard.get_bit(self.wr, end_square):
            self.wr = Bitboard.clear_bit(self.wr, end_square)
        elif Bitboard.get_bit(self.wq, end_square):
            self.wq = Bitboard.clear_bit(self.wq, end_square)
        elif Bitboard.get_bit(self.wK, end_square):
            self.wK = Bitboard.clear_bit(self.wK, end_square)
        
        # White piece capture
        if Bitboard.get_bit(self.wp, start_square):
            self.wp = Bitboard.clear_bit(self.wp, start_square)
            self.wp = Bitboard.set_bit(self.wp, end_square)
        elif Bitboard.get_bit(self.wk, start_square):
            self.wk = Bitboard.clear_bit(self.wk, start_square)
            self.wk = Bitboard.set_bit(self.wk, end_square)
        elif Bitboard.get_bit(self.wb, start_square):
            self.wb = Bitboard.clear_bit(self.wb, start_square)
            self.wb = Bitboard.set_bit(self.wb, end_square)
        elif Bitboard.get_bit(self.wr, start_square):
            self.wr = Bitboard.clear_bit(self.wr, start_square)
            self.wr = Bitboard.set_bit(self.wr, end_square)
        elif Bitboard.get_bit(self.wq, start_square):
            self.wq = Bitboard.clear_bit(self.wq, start_square)
            self.wq = Bitboard.set_bit(self.wq, end_square)
        elif Bitboard.get_bit(self.wK, start_square):
            self.wK = Bitboard.clear_bit(self.wK, start_square)
            self.wK = Bitboard.set_bit(self.wK, end_square)
        
        # Black piece is captured
        if Bitboard.get_bit(self.bp, end_square):
            self.bp = Bitboard.clear_bit(self.bp, end_square)
        elif Bitboard.get_bit(self.bk, end_square):
            self.bk = Bitboard.clear_bit(self.bk, end_square)
        elif Bitboard.get_bit(self.bb, end_square):
            self.bb = Bitboard.clear_bit(self.bb, end_square)
        elif Bitboard.get_bit(self.br, end_square):
            self.br = Bitboard.clear_bit(self.br, end_square)
        elif Bitboard.get_bit(self.bq, end_square):
            self.bq = Bitboard.clear_bit(self.bq, end_square)
        elif Bitboard.get_bit(self.bK, end_square):
            self.bK = Bitboard.clear_bit(self.bK, end_square)
        
        # Black piece capture
        if Bitboard.get_bit(self.bp, start_square):
            self.bp = Bitboard.clear_bit(self.bp, start_square)
            self.bp = Bitboard.set_bit(self.bp, end_square)
        elif Bitboard.get_bit(self.bk, start_square):
            self.bk = Bitboard.clear_bit(self.bk, start_square)
            self.bk = Bitboard.set_bit(self.bk, end_square)
        elif Bitboard.get_bit(self.bb, start_square):
            self.bb = Bitboard.clear_bit(self.bb, start_square)
            self.bb = Bitboard.set_bit(self.bb, end_square)
        elif Bitboard.get_bit(self.br, start_square):
            self.br = Bitboard.clear_bit(self.br, start_square)
            self.br = Bitboard.set_bit(self.br, end_square)
        elif Bitboard.get_bit(self.bq, start_square):
            self.bq = Bitboard.clear_bit(self.bq, start_square)
            self.bq = Bitboard.set_bit(self.bq, end_square)
        elif Bitboard.get_bit(self.bK, start_square):
            self.bK = Bitboard.clear_bit(self.bK, start_square)
            self.bK = Bitboard.set_bit(self.bK, end_square)
    
    def get_state(self) -> list[list[U64]]:
        return [[self.wp, self.wr, self.wb, self.wk, self.wq, self.wK], [self.bp, self.br, self.bb, self.bk, self.bq, self.bK], [self.black_pieces_bb(), self.white_pieces_bb()]]