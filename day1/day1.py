
def solve():
  count = 0
  with open('test1.txt') as f:
    lst = [int(x) for x in f.readlines()]

  # Part 1
  for i in range(len(lst)):
    if i != 0:
      prev = lst[i - 1]
      if lst[i] > prev:
        count += 1

  count = 0
  # Part 2
  for i in range(1, len(lst) - 1):
    sum = lst[i - 1] + lst[i] + lst[i + 1]
    prev = lst[i - 2] + lst[i - 1] + lst[i]
    if sum > prev:
      count += 1
  
  print(count)
