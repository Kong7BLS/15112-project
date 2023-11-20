import math, random

def set_mines(mines_num: int = 4, n: int = 6):
    mine_map = [[0 for col in range(n)] for row in range(n)]
    count_mine = 0
    while count_mine < mines_num:
        row = random.randint(0, n)
        col = random.randint(0, n)
        if (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 1):
            continue
        else:
            if mine_map[row][col] != -1:
                count_mine += 1
                mine_map[row][col] = -1
    return mine_map

def set_hints(mine_map: list[list[int]]):
    can_solve = False
    while not can_solve:
        for row in range(len(mine_map)):
            for col in range(len(mine_map[0])):
                pass
    
    pass

def set_hints_helper(hint_num = 5):
    pass