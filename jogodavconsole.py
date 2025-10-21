import random

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.mode = None
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        self.show_menu()

    def show_menu(self):
        while True:
            print("\nEscolha o Modo de Jogo:")
            print("1. Humano vs Humano")
            print("2. Humano vs Computador")
            print("3. Ver Pontuações")
            print("4. Resetar Pontuações")
            print("5. Sair")
            choice = input("Digite sua escolha: ").strip()
            if choice == '1':
                self.start_game('human')
            elif choice == '2':
                self.start_game('ai')
            elif choice == '3':
                self.show_scores()
            elif choice == '4':
                self.reset_scores()
            elif choice == '5':
                break
            else:
                print("Escolha inválida. Tente novamente.")

    def start_game(self, mode):
        self.mode = mode
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.play_game()

    def play_game(self):
        while True:
            self.print_board()
            if self.mode == 'ai' and self.current_player == 'O':
                self.ai_move()
            else:
                self.human_move()
            if self.check_winner():
                self.print_board()
                print(f"Jogador {self.current_player} venceu!")
                self.scores[self.current_player] += 1
                break
            elif self.is_draw():
                self.print_board()
                print("Empate!")
                self.scores['Draw'] += 1
                break
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def print_board(self):
        print("\nTabuleiro:")
        for i in range(3):
            print(" | ".join(self.board[i][j] if self.board[i][j] else ' ' for j in range(3)))
            if i < 2:
                print("-" * 9)

    def human_move(self):
        while True:
            try:
                row = int(input(f"Jogador {self.current_player}, digite a linha (0-2): "))
                col = int(input(f"Jogador {self.current_player}, digite a coluna (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == '':
                    self.board[row][col] = self.current_player
                    break
                else:
                    print("Movimento inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite números.")

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            print(f"Computador jogou na posição ({row}, {col})")

    def find_best_move(self):
        best_score = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner_minimax(board, 'O'):
            return 10 - depth
        if self.check_winner_minimax(board, 'X'):
            return depth - 10
        if self.is_draw_minimax(board):
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner_minimax(self, board, player):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def is_draw_minimax(self, board):
        for row in board:
            if '' in row:
                return False
        return True

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def is_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def show_scores(self):
        print(f"\nPontuações: X: {self.scores['X']} | O: {self.scores['O']} | Empates: {self.scores['Draw']}")

    def reset_scores(self):
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        print("Pontuações resetadas.")

if __name__ == "__main__":
    TicTacToe()