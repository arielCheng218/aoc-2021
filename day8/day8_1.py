
def solve():
  
  output = []

  with open('day8.txt') as f:
    for x in f.readlines():
      line = str(x).strip().split(" | ")
      output.append(line[1].strip().split())

  count = 0
  for line in output:
    for record in line:
      if len(record) == 2 or len(record) == 4 or len(record) == 3 or len(record) == 7:
        count += 1

  print(count)
