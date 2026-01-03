board = [' '] * 9

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

def check_winner(player):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win)

def play():
    current = 'X'
    for _ in range(9):
        print_board()
        pos = int(input(f"Player {current}, choose (1-9): ")) - 1
        if board[pos] == ' ':
            board[pos] = current
            if check_winner(current):
                print_board()
                print(f"🎉 Player {current} wins!")
                return
            current = 'O' if current == 'X' else 'X'
        else:
            print("❌ Position already taken")
    print("🤝 Draw!")

play()
