import math, random

def set_mines(mines_num: int = 4, n: int = 6) -> list[list[int]]:
    mine_map = [[0 for col in range(n)] for row in range(n)]
    count_mine = 0
    while count_mine < mines_num:
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        if (row == 0 and col == 0) or (row == 1 and col == 0) or (row == 0 and col == 1):
            continue
        else:
            if mine_map[row][col] != -1:
                count_mine += 1
                mine_map[row][col] = -1
    return mine_map

demo1 = ["and", ["mine", 1, "y"], ["mine", 3, "y"]]
demo = ["not", ["and", ["exists", "y", demo1], ["exists", "y", ["mine", 2, "y"]]]]

def pretty(exp) -> str:
    if exp[0] == "mine":
        x, y = exp[1], exp[2]
        return f"mine({str(x)}, {str(y)})"
    if exp[0] == "not":
        return f"¬({pretty(exp[1])})"
    if exp[0] == "and" or exp[0] == "or":
        op = "∧" if exp[0] == "and" else "∨"
        return f"({pretty(exp[1])} {op} {pretty(exp[2])})"
    if exp[0] == "exists" or exp[0] == "forall":
        op = "∀" if exp[0] == "forall" else "∃"
        return f"{op}{pretty(exp[1])}. {pretty(exp[2])}"
    return exp

def check_hints(mine_map: list[list[int]], exp) -> bool:
    pass

def set_hints(mine_map: list[list[int]]):
    can_solve = False
    while not can_solve:
        for row in range(len(mine_map)):
            for col in range(len(mine_map[0])):
                pass
    pass

def set_hints_helper(hint_num = 5):
    pass