import random

# Função para imprimir o tabuleiro
def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i * 3 + j + 1], end=" | ")
        print("\n---------")

# Função para verificar se o jogo terminou
def game_over(board):
    # Verificar as condições de vitória
    for i in range(3):
        if board[i * 3 + 1] == board[i * 3 + 2] == board[i * 3 + 3] != " ":
            return True
        if board[i + 1] == board[i + 4] == board[i + 7] != " ":
            return True
    if board[1] == board[5] == board[9] != " " or board[3] == board[5] == board[7] != " ":
        return True

    # Verificar se há espaços vazios
    if " " not in board[1:]:
        return True

    return False

# Função para a jogada do computador
def computer_move(board):
    while True:
        move = random.randint(1, 9)  # Escolhe um número aleatório entre 1 e 9
        if board[move] == " ":
            board[move] = "X"
            break

# Função para a jogada do usuário
def user_move(board):
    while True:
        move = input("Digite um número de 1 a 9 para fazer sua jogada: ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9 and board[move] == " ":
                board[move] = "O"
                break

# Função principal do jogo
def play_game():
    board = [" "] * 10  # Cria um tabuleiro vazio

    # Colocar a primeira jogada do computador no meio do tabuleiro
    board[5] = "X"
    print_board(board)

    # Loop principal do jogo
    while True:
        user_move(board)
        print_board(board)
        if game_over(board):
            break

        computer_move(board)
        print_board(board)
        if game_over(board):
            break

    # Verificar o resultado do jogo
    if "X" in board:
        print("Você perdeu! O computador ganhou.")
    elif "O" in board:
        print("Parabéns! Você ganhou.")
    else:
        print("Empate!")

# Iniciar o jogo
play_game()
