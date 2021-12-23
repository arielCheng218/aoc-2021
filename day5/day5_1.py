
from collections import Counter

def solve():

  lst = []
  coords = []
  temp = []

  # Process input
  with open('test5.txt') as f:
    for x in f.readlines():
      x = x.replace(' -> ', '|')
      split_i = x.index('|')
      p1 = x[:split_i]
      p2 = x[split_i + 1:]
      lst.append([int(x) for x in p1.split(",")] + [int(x) for x in p2.split(",")])

  # Filter - only horizontal and vertical lines
  for l in lst:
    if l[0] == l[2]:
      temp.append(l)
    elif l[1] == l[3]:
      temp.append(l)
  temp = lst

  # Find all coordinates lines will cover
  for line_coords in lst:
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

  # Find duplicates in coordinate list
  vertical_horizontal_dupes = [pt for pt in Counter(coords).values() if pt > 1]

  print(len(vertical_horizontal_dupes))

