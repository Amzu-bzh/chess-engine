from pyglet.window import Window, mouse
from pyglet import clock
from pyglet.app import run

from pyglet.shapes import Rectangle

from board import Board
from ruleengine import RuleEngine
from bitboard import Bitboard

CASE_SIZE = 128

"""
Gmae class

- orchestrates everything
"""
class Game(Window):
    def __init__(self, width: int=1024, height: int=1024, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height
        
        self.board = Board()
        self.re = RuleEngine()

        self.turn: bool = True # True -> White | False -> Black 
        
        self.old_case_selected = None
        self.case_selected_rect = Rectangle(0, 0, CASE_SIZE, CASE_SIZE, (255, 0, 0, 0))
        self.possible_moves: list[int] = []
        self.possible_cases: list[Rectangle] = []
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:
            case_coord = (x//CASE_SIZE, y//CASE_SIZE)
            case_selected = (case_coord[1] * 8) + case_coord[0]
            if ((self.turn == True and Bitboard.get_bit(self.board.white_pieces_bb(), case_selected) == True) or (self.turn == False and Bitboard.get_bit(self.board.black_pieces_bb(), case_selected) == True)) and self.board.is_piece(case_selected):
                self.old_case_selected = (case_coord[1] * 8) + case_coord[0]
                self.case_selected_rect.x = case_coord[0] * CASE_SIZE
                self.case_selected_rect.y = case_coord[1] * CASE_SIZE
                self.case_selected_rect.color = (255, 0, 0, 100)
                self.init_possible_cases()
            elif case_selected in self.possible_moves:
                self.board.move(self.old_case_selected, case_selected)
                self.case_selected_rect.color = (255, 0, 0, 0)
                self.possible_cases = []
                self.possible_moves = []
                self.turn = not self.turn
            else:
                self.case_selected_rect.color = (255, 0, 0, 0)
                self.possible_moves = []
                self.possible_cases = []
    
    def init_possible_cases(self):
        self.possible_cases = []
        
        # self.possible_cases = self.re.get_moves(self.board.get_state())
        self.possible_moves = self.re.get_moves([])
        print(self.possible_moves)
        for possible_move in self.possible_moves:
            self.possible_cases.append(Rectangle((possible_move%8)*CASE_SIZE, (possible_move//8)*CASE_SIZE, CASE_SIZE, CASE_SIZE, (0, 0, 125, 100)))
        
    def update(self, dt):
        pass
    
    def on_draw(self):
        self.clear()
        self.board.draw()
        self.case_selected_rect.draw()
        for case in self.possible_cases:
            case.draw()
    
    def run(self, frame_rate: int=60):
        clock.schedule_interval(self.update, 1/60)
        run()