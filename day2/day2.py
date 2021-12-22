
def solve():

  horizontal = 0
  depth = 0

  with open('test2.txt') as f:
    lst = [str(x).strip() for x in f.readlines()]

  # Part 1
  # for line in lst:
  #   num = int(line[-1])
  #   if "up" in line:
  #     depth -= num
  #   if "down" in line:
  #     depth += num
  #   if "forward" in line:
  #     horizontal += num
  
  # print(horizontal * depth)

  # Part 2

  aim = 0
  for line in lst:
    num = int(line[-1])
    if "down" in line:
      aim += num
    if "up" in line:
      aim -= num
    if "forward" in line:
      horizontal += num
      depth += aim * num
  
  print(horizontal * depth)

