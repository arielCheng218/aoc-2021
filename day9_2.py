
import math

def solve():

  heightmap = []

  # Get input
  with open('day9.txt') as f:
    heightmap = [[int(n) for n in x.strip()] for x in f.readlines()]

  groups = []

  def count_groups(i, j):
    if j < 0 or j >= len(heightmap) or i < 0 or i >= len(heightmap[0]) or heightmap[j][i] == 9 or heightmap[j][i] == -1:
      return
    heightmap[j][i] = -1
    groups[-1] += 1
    count_groups(i + 1, j)
    count_groups(i - 1, j)
    count_groups(i, j + 1)
    count_groups(i, j - 1)
  
  for i in range(0, len(heightmap)):
    for j in range(0, len(heightmap[0])):
      groups.append(0)
      count_groups(j, i)

  print(groups)

  print(math.prod(sorted(groups, reverse=True)[:3]))