
def solve():
  with open('test5.txt') as f:
    lst = [str(x).strip() for x in f.readlines()]

  print(lst)