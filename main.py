from pygame import *
from random import randint, choice

from filed import Field
from life import Life

from rules import *

from colors import *
from tests import *

W,H = 1920, 1080

win = display.set_mode((W,H))
timer = time.Clock()

field = Field(460, 40, win,cell_size=10,w=1000,h=1000)
Life.spawn(1000, field)

while True:
    for e in event.get():
        if e.type == KEYDOWN and e.key == K_ESCAPE: exit()

    win.fill(WHITE)

    check_nebgs(field)
    for l in Life.all_lifes: l.move()

    field.draw()
    timer.tick()
    display.update()