from pygame import *
from colors import *

class Cell:
    def __init__(self,x,y,side,win):
        self.win = win
        self.side = side
        self.x, self.y = x, y

        self.nebgs = {}

        self.color = WHITE
        
        self.value = 0
    
    def get_empty_neb(self):
        for cell in self.nebgs.values():
            if not cell.value: return cell
        return 0

    def draw(self):
        draw.rect(self.win,self.color,Rect(self.x,self.y,self.side,self.side))
        #draw.rect(self.win,BLACK,Rect(self.x,self.y,self.side,self.side),width=1)



    