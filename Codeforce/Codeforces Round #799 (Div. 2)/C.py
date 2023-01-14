t = int(input())
ans = []

def solve(board):
    for r in range(1,6):
        for c in range(1,6):
            if board[r][c] == '#' and board[r-1][c-1] == '#' and board[r+1][c-1] == '#' and board[r-1][c-1] == '#' and board[r-1][c+1] == '#':
                return (r,c)

#for _ in range(t):
    board = []
    #for r in range(8):
print(t)
    #ans.append(solve(board))

for a in ans:
    print(a)