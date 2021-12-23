
from collections import Counter

def get_slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)

def solve():

  input_coord_pairs = []
  horizontal_vertical_lines = []
  diagonal_lines = []
  coords = []

  # Process input
  with open('test5.txt') as f:
    for x in f.readlines():
      x = x.replace(' -> ', '|')
      split_i = x.index('|')
      p1 = x[:split_i]
      p2 = x[split_i + 1:]
      input_coord_pairs.append([int(x) for x in p1.split(",")] + [int(x) for x in p2.split(",")])

  # Filter - only horizontal, vertical, 45 degrees lines
  for l in input_coord_pairs:
    if l[0] == l[2]:
      horizontal_vertical_lines.append(l)
    elif l[1] == l[3]:
      horizontal_vertical_lines.append(l)
    else:
      if abs(get_slope(l[0], l[1], l[2], l[3])) == 1:
        diagonal_lines.append(l)

  # Find all coordinates horizontal & vertical lines will cover
  for line_coords in horizontal_vertical_lines:
    if line_coords[0] == line_coords[2]:
      # vertical line - y values will vary
      if line_coords[1] < line_coords[3]:
        for y in range(line_coords[1], line_coords[3] + 1):
          coords.append((line_coords[0], y))
      else:
        for y in range(line_coords[3], line_coords[1] + 1):
          coords.append((line_coords[0], y))
    elif line_coords[1] == line_coords[3]:
      # horizontal line - x values will vary
      if line_coords[0] < line_coords[2]:
        for x in range(line_coords[0], line_coords[2] + 1):
          coords.append((x, line_coords[1]))
      else:
       for x in range(line_coords[2], line_coords[0] + 1):
          coords.append((x, line_coords[1]))

  # Find all coordinates diagonal lines will cover
  for line_coords in diagonal_lines:
    if get_slope(line_coords[0], line_coords[1],line_coords[2], line_coords[3]) == 1:
      # slope is positive
      if line_coords[0] < line_coords[2]:
        i = 0
        for n in range(line_coords[0], line_coords[2] + 1):
          coords.append((n, line_coords[1] + i))
          i += 1
      else:
        i = 0
        for n in range(line_coords[2], line_coords[0] + 1):
          coords.append((n, line_coords[3] + i))
          i += 1
    elif get_slope(line_coords[0], line_coords[1],line_coords[2], line_coords[3]) == -1:
      # slope is negative
      if line_coords[0] < line_coords[2]:
        i = 0
        for n in range(line_coords[0], line_coords[2] + 1):
          coords.append((n, line_coords[1] - i))
          i += 1
      else:
        i = 0
        for n in range(line_coords[2], line_coords[0] + 1):
          coords.append((n, line_coords[3] - i))
          i += 1

  # Find duplicates in coordinate list
  dupes = [pt for pt in Counter(coords).values() if pt > 1]

  print(len(dupes))

