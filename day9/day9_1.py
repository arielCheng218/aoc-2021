
def get_adjacents(grid, j, i):
    adjacents = []
    if i + 1 < len(grid[0]):
        adjacents.append(grid[j][i+1])
    if i - 1 >= 0:
        adjacents.append(grid[j][i-1])
    if j + 1 < len(grid):
        adjacents.append(grid[j+1][i])
    if j - 1 >= 0:
        adjacents.append(grid[j-1][i])
    return adjacents

def solve():
  heightmap = []
  low_pts = 0
  count = 0

  # Get input
  with open('day9.txt') as f:
    heightmap = [[int(n) for n in x.strip()] for x in f.readlines()]

  for row_i in range(len(heightmap)):
    for col_i in range(len(heightmap[row_i])):
      if heightmap[row_i][col_i] < min(get_adjacents(heightmap, row_i, col_i)):
        low_pts += 1 + heightmap[row_i][col_i]

  print(low_pts + count)