LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def show(b):
    for i in range(0, 9, 3):
        print(' | '.join(b[i:i+3]))
        if i < 6: print('---------')
def winner(b):
    for a, c, d in LINES:
        if b[a] != ' ' and b[a] == b[c] == b[d]:
            return b[a]
    return None
def find_move(b, p):
    for i in range(9):
        if b[i] == ' ':
            b[i] = p; w = winner(b); b[i] = ' '
            if w: return i
    return None
def computer(b):
    m = find_move(b, 'O')                    # win
    if m is None: m = find_move(b, 'X')      # block
    if m is None:
        for i in (4, 0, 2, 6, 8, 1, 3, 5, 7):
            if b[i] == ' ':
                m = i; break
    b[m] = 'O'
def play():
    b = [' '] * 9
    while True:
        show(b)
        m = int(input('Your move (1-9): ')) - 1
        if m not in range(9) or b[m] != ' ':
            print('Invalid move'); continue
        b[m] = 'X'
        if winner(b) or ' ' not in b: break
        computer(b)
        if winner(b) or ' ' not in b: break
    show(b)
    w = winner(b)
    print(f'{w} wins!' if w else 'Draw!')
play()