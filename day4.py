 
def sum_matrix(matrix):
  sum = 0
  for row in matrix:
    for n in row:
      sum += int(n)
  return sum

def check_lst(lst):
  for n in lst:
    if not type(n) is int:
      return None
  return sum(lst)

def get_col(matrix, col_i):
  col = []
  for row in matrix:
    for i in range(len(row)):
      if i == col_i:
        col.append(row[i])
  return col

def check_win(board):
  # horizontal
  for row in board:
    if check_lst(row) != None:
      return check_lst(row)
  # vertical
  for i in range(len(board)):
    if check_lst(get_col(board, i)) != None:
      return check_lst(get_col(board, i))
  return None

def solve():

  nums = []
  boards = []

  # Get input data
  with open('test4.txt') as f:
    current_board = []
    for i, x in enumerate(f.readlines()):
      if i == 0:
        nums = x.strip().split(",")
      else:
        if x == "\n":
          boards.append(current_board)
          current_board = []
        elif x != "\n":
          line = x.strip().split(" ")
          while '' in line:
            line.remove('')
          current_board.append(line)

  continue_game = True

  # Part 1
  while continue_game:
    num = nums[0]
    for board_i, board in enumerate(boards):
      for row_i, row in enumerate(board):
        for d_i, d in enumerate(row):
          if d == num:
            boards[board_i][row_i][d_i] = int(boards[board_i][row_i][d_i])
      if check_win(board) != None:
        # current board has won
        print((sum_matrix(board) - check_win(board)) * int(num))
        continue_game = False
        break
    nums.pop(0)
