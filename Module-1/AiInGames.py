import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(' | '.join(colored(cell) for cell in row))
        if row != board[6:9]:
            print(Fore.CYAN + '---------')
    print()

def player_choice():
    while True:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
        if symbol in ['X', 'O']:
            return (symbol, 'O' if symbol == 'X' else 'X')
        print(Fore.RED + "Invalid choice. Please enter X or O.")

def player_move(board, symbol):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1].isdigit():
                board[move - 1] = symbol
                break
            else:
                print(Fore.RED + "Invalid move. Try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number (1-9).")

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board[:]
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                print(Fore.MAGENTA + f"AI moves to {i+1}")
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board[:]
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                print(Fore.MAGENTA + f"AI blocks at {i+1}")
                return
    move = random.choice([i for i in range(9) if board[i].isdigit()])
    board[move] = ai_symbol
    print(Fore.MAGENTA + f"AI moves to {move+1}")

def check_win(board, symbol):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in win_patterns)

def check_full(board):
    return all(not cell.isdigit() for cell in board)

def play_game():
    print(Fore.CYAN + "🎮 Welcome to Tic-Tac-Toe!")
    name = input(Fore.GREEN + "Enter your name: ")
    
    while True:
        board = [str(i) for i in range(1, 10)]
        player_symbol, ai_symbol = player_choice()
        turn = 'Player' if random.choice([True, False]) else 'AI'
        print(Fore.CYAN + f"{turn} goes first!")

        while True:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"🎉 Congratulations, {name}! You won!")
                    break
                turn = 'AI' if not check_full(board) else None
            elif turn == 'AI':
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "😞 AI won! Better luck next time.")
                    break
                turn = 'Player' if not check_full(board) else None

            if turn is None:
                display_board(board)
                print(Fore.YELLOW + "It's a tie!")
                break

        again = input(Fore.CYAN + "\nDo you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print(Fore.GREEN + "Thanks for playing! 👋")
            break

if __name__ == "__main__":
    play_game()
