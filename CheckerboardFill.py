

def cover(board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)
    s = side // 2

    offsets = (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # print(top + dy_outer, left + dx_outer)
            if not board[top+dy_outer][left+dx_outer]:          # Searches for the missing CORNER
                # print('Not found', lab)
                board[top+s+dy_inner][left+s+dx_inner] = lab    # Sets every center piece except the one in the cuadrant of the missing corner

    lab += 1
    if s > 1:                                                   # Divides the board in subboards of min length = 2
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(board, lab, top+dy, left+dx, s)
    return lab


board = [[0]*8 for i in range(8)]
board[0][0] = -1

cover(board)

for row in board:
    print((" %2i"*8) % tuple(row))                              # 2i: The number of min digits. The number of times the string is repeated must be the same as the len of the tuple
