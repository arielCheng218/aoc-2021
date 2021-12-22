
def check_lst(lst):
  if sum(lst) == 5000:
    return True
  return False

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
    if check_lst(row):
      return True
  # vertical
  for i in range(len(board)):
    if check_lst(get_col(board, i)):
      return True
  return False

def solve():

  nums = []
  boards = []

  # Get input data
  with open('test4.txt') as f:
    current_board = []
    for i, x in enumerate(f.readlines()):
      if i == 0:
        nums = x.strip().split(",")
        nums = [int(n) for n in nums]
      else:
        if x == "\n":
          boards.append(current_board)
          current_board = []
        elif x != "\n":
          line = x.strip().split(" ")
          while '' in line:
            line.remove('')
          line = [int(n) for n in line]
          current_board.append(line)

  continue_game = True

  # Part 1
  # while continue_game:
  #   num = nums[0]
  #   nums = nums[1:]
  #   for board_i, board in enumerate(boards):
  #     for row_i, row in enumerate(board):
  #       for d_i, d in enumerate(row):
  #         if d == num:
  #           boards[board_i][row_i][d_i] = 1000
  #     if check_win(board):
  #       # current board has won
  #       total = 0
  #       for row in board:
  #         for n in row:
  #           if n != 1000:
  #             total += n
  #       print(total * int(num))
  #       continue_game = False
  #       break

  # Part 2
  found = False
  while not found:
    num = nums[0]
    nums = nums[1:]
    for board_i, board in enumerate(boards):
      for row_i, row in enumerate(board):
        for d_i, d in enumerate(row):
          if d == num:
            boards[board_i][row_i][d_i] = 1000
    
    index = 0
    while index < len(boards):
      if check_win(boards[index]):
        if len(boards) > 1:
          boards.pop(index)
        else:
          found = True
          print(boards[index])
          total = 0
          for row in boards[index]:
            for n in row:
              if n != 1000:
                total += n
          print(num)
          print(total * num)
          break
      else:
        index += 1
