
# from math import inf as infinity
# from random import choice
# import platform
# import numpy as np
# from os import system
# import time as time


# Human = -1
# Computer = +1
# draw = 0
# #Initialize empty board
# board = np.zeros((3,3),dtype=np.int32)
# board
# def evaluate(curr_state):
#     if wins(curr_state, Computer):
#         score = +1
#     elif wins(curr_state, Human):
#         score = -1
#     else:
#         score = 0
#     return score

# #write your code here to assign score if computer or human wins and 0 in case of draw; return score value

# def wins(state, player):
#     win_state = [
#         [state[0, 0], state[0, 1], state[0, 2]],
#         [state[1, 0], state[1, 1], state[1, 2]],
#         [state[2, 0], state[2, 1], state[2, 2]],
#         [state[0, 0], state[1, 0], state[2, 0]],
#         [state[0, 1], state[1, 1], state[2, 1]],
#         [state[0, 2], state[1, 2], state[2, 2]],
#         [state[0, 0], state[1, 1], state[2, 2]],
#         [state[2, 0], state[1, 1], state[0, 2]],
#     ]
#     if [player, player, player] in win_state:
#         return True
#     else:
#         return False
    
    

# # def wins(state, player):#return True or False by checking all possibilites of win for human or computer
# #     win_state = [ [player, player, player], [player, player, player], [player, player, player] ] #all possible winning states
# #     if np.array_equal(state, win_state):
# #         return True
# #     for i in range(3):
# #         if np.array_equal(state[i], win_state[i]):
# #             return True
# #     for i in range(3):
# #         if np.array_equal(state[:,i], win_state[i]):
# #             return True
# #     if np.array_equal(state.diagonal(), win_state[0]):
# #         return True
# #     if np.array_equal(np.fliplr(state).diagonal(), win_state[0]):
# #         return True
# #     return False
# #write your code here to check if computer or human wins; return True if wins else return False


# def game_over(state):
#     return wins(state, Human) or wins(state, Computer)


# def empty_cells(state):
#     cells = []
#     for x, row in enumerate(state):
#         for y, cell in enumerate(row):
#             if cell == 0:
#                 cells.append([x, y])
#     return cells



# def valid_move(x, y):
#     if [x, y] in empty_cells(board):
#         return True
#     else:
#         return False
    

# def set_move(x, y, player):
#     if valid_move(x, y):
#         board[x, y] = player
#         return True
#     else:
#         return False
    

# def minimax(state, depth, player):
#     if player == Computer:
#         best = [-1, -1, -infinity]
#     else:
#         best = [-1, -1, +infinity]
#     if depth == 0 or game_over(state):
#         score = evaluate(state)
#         return [-1, -1, score]
#     for cell in empty_cells(state):
#         x, y = cell[0], cell[1]
#         state[x, y] = player
#         score = minimax(state, depth - 1, -player)
#         state[x, y] = 0
#         score[0], score[1] = x, y
#         if player == Computer:
#             if score[2] > best[2]:
#                 best = score
#         else:
#             if score[2] < best[2]:
#                 best = score
#     return best


# def alpha_beta_pruning(state, depth, player, alpha, beta):
#     if player == Computer:
#         best = [-1, -1, -infinity]
#     else:
#         best = [-1, -1, +infinity]
#     if depth == 0 or game_over(state):
#         score = evaluate(state)
#         return [-1, -1, score]
#     for cell in empty_cells(state):
#         x, y = cell[0], cell[1]
#         state[x, y] = player
#         score = alpha_beta_pruning(state, depth - 1, -player, alpha, beta)
#         state[x, y] = 0
#         score[0], score[1] = x, y
#         if player == Computer:
#             if score[2] > best[2]:
#                 best = score
#             if best[2] > alpha:
#                 alpha = best[2]
#             if alpha >= beta:
#                 break
#         else:
#             if score[2] < best[2]:
#                 best = score
#             if best[2] < beta:
#                 beta = best[2]
#             if alpha >= beta:
#                 break
#     return best


# def computer_turn_alphabeta(c_choice, h_choice):
#     depth = len(empty_cells(board))
#     if depth == 0 or game_over(board):
#         return
#     clean()
#     print(f'Computer turn [{c_choice}]')
#     print_board(board, c_choice, h_choice)
#     move = alpha_beta_pruning(board, depth, Computer, -infinity, +infinity)
#     set_move(move[0], move[1], Computer)
#     time.sleep(1)

# def clean():
#     if platform.system() == 'Windows':
#         system('cls')
#     else:
#         system('clear')


# def print_board(state, c_choice, h_choice):
#     chars = {
#         -1: h_choice,
#         +1: c_choice,
#         0: ' '
#     }
#     str_line = '---------------'
#     print('---------------')
#     for row in state:
#         for cell in row:
#             symbol = chars[cell]
#             print(f'| {symbol} |', end='')
#         print()
#         print(str_line)
#     print()

# def computer_turn(c_choice, h_choice):
#     depth = len(empty_cells(board))
#     if depth == 0 or game_over(board):
#         return
#     clean()
#     print(f'Computer turn [{c_choice}]')
#     print_board(board, c_choice, h_choice)
#     if depth == 9:
#         x = choice([0, 1, 2])
#         y = choice([0, 1, 2])
#     else:
#         move = minimax(board, depth, Computer)
#         x, y = move[0], move[1]
#     set_move(x, y, Computer)
#     time.sleep(1)

# def human_turn(c_choice, h_choice):
#     depth = len(empty_cells(board))
#     if depth == 0 or game_over(board):
#         return
#     move = -1
#     clean()
#     print(f'Human turn [{h_choice}]')
#     print_board(board, c_choice, h_choice)
#     while move < 1 or move > 9:
#         try:
#             move = int(input('Use numpad (1..9): '))
#             coord = [int((move - 1) / 3), (move - 1) % 3]
#             can_move = set_move(coord[0], coord[1], Human)
#             if not can_move:
#                 print('Bad move')
#                 move = -1
#         except (EOFError, KeyboardInterrupt):
#             print('Bye')
#             exit()
#         except (KeyError, ValueError):
#             print('Bad choice')

# def main():
#     clean()
#     h_choice = ''  # X or O
#     c_choice = ''  # X or O
#     first = ''  # if human is the first
#     # Human chooses X or O to play
#     while h_choice != 'O' and h_choice != 'X':
#         try:
#             print('')
#             h_choice = input('Choose X or O\nChosen: ').upper()
#         except (EOFError, KeyboardInterrupt):
#             print('Bye')
#             exit()
#         except (KeyError, ValueError):
#             print('Bad choice')
#     # Setting computer's choice
#     if h_choice == 'X':
#         c_choice = 'O'
#     else:
#         c_choice = 'X'
#     # Human may starts first
#     clean()
#     while first != 'Y' and first != 'N':
#         try:
#             first = input('First to start?[y/n]: ').upper()
#         except (EOFError, KeyboardInterrupt):
#             print('Bye')
#             exit()
#         except (KeyError, ValueError):
#             print('Bad choice')
#     # Main loop of this game
#     while len(empty_cells(board)) > 0 and not game_over(board):
#         if first == 'N':
#             #computer_turn(c_choice, h_choice)
#             computer_turn_alphabeta(c_choice, h_choice)
#             first = ''
#         human_turn(c_choice, h_choice)
#         #computer_turn(c_choice, h_choice)
#         computer_turn_alphabeta(c_choice, h_choice)
#     # Game over message
#     if wins(board, Human):
#         clean()
#         print(f'Human turn [{h_choice}]')
#         print_board(board, c_choice, h_choice)
#         print('YOU WIN!')
#     elif wins(board, Computer):
#         clean()
#         print(f'Computer turn [{c_choice}]')
#         print_board(board, c_choice, h_choice)
#         print('YOU LOSE!')
#     else:
#         clean()
#         print_board(board, c_choice, h_choice)
#         print('DRAW!')
#     exit()

# if __name__ == '__main__':
#     main()
    










