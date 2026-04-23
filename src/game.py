from pyglet.window import Window, mouse
from pyglet import clock
from pyglet.app import run

from pyglet.shapes import Rectangle

from board import Board

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
        
        self.case_selected = None
        self.case_selected_rect = Rectangle(0, 0, CASE_SIZE, CASE_SIZE, (255, 0, 0, 0))
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button & mouse.LEFT:
            case_coord = (x//CASE_SIZE, y//CASE_SIZE)
            self.case_selected = (case_coord[1] * 8) + case_coord[0]
            if self.board.is_piece(self.case_selected):
                self.case_selected_rect.x = case_coord[0] * CASE_SIZE
                self.case_selected_rect.y = case_coord[1] * CASE_SIZE
                self.case_selected_rect.color = (255, 0, 0, 100)
            else:
                self.case_selected_rect.color = (255, 0, 0, 0)
        
    def update(self, dt):
        pass
    
    def on_draw(self):
        self.clear()
        self.board.draw()
        self.case_selected_rect.draw()
    
    def run(self, frame_rate: int=60):
        clock.schedule_interval(self.update, 1/60)
        run()