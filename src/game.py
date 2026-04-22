from pyglet.window import Window
from pyglet import clock
from pyglet.app import run

from board import Board

"""
Gmae class

- orchestrates everything
"""
class Game(Window):
    def __init__(self, width: int=1280, height: int=720, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height
        
        self.board = Board()
    
    def update(self, dt):
        pass
    
    def on_draw(self):
        self.clear()
        # self.board.draw()
    
    def run(self, frame_rate: int=60):
        clock.schedule_interval(self.update, 1/60)
        run()