from random import randint
from colors import *

def rand_nebs_test(field):
    rtmp = randint(0,len(field.cells))
    field.cells[rtmp].color = RED
    for nebg in field.cells[rtmp].nebgs.values():
        nebg.color = GREEN