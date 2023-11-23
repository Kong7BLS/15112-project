import math, random

n = 6
mines_num = 4
mine_map= [[0 for col in range(n)] for row in range(n)]


def set_mines():
    count_mine = 0
    while count_mine < mines_num:
        val1 = random.randint(0, 6)
        row = val1
        val2 = random.randint(0, 6)
        col = val2 
        if (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 0):
            continue
        else:
            if mine_map[row][col] != -1:
                count += 1
                mine_map[row][col] = -1
def set_hints():
    cansolve = False
    while not cansolve:
        for row in range(len(mine_map)):
            for col in range(len(mine_map[0])):
             pass
    
    pass

def set_hintshelper(hint_num = 5):
    pass