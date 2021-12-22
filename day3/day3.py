
def get_most_common(lst, i):
  zeros = 0
  ones = 0
  for s in lst:
    if s[i] == "0":
      zeros += 1
    else:
      ones += 1
  if zeros > ones:
    return "0"
  elif ones > zeros:
    return "1"
  else:
    return "1"


def solve():

  with open('test3.txt') as f:
    lst = [str(x).strip() for x in f.readlines()]

  zeros = [0] * 12

  gamma = ["0"] * 12
  epsilon = ["0"] * 12

  most_common = ["0"] * 12

  # Part 1
  for line in lst:
    for char_i in range(len(line)):
      if line[char_i] == "0":
        zeros[char_i] += 1
  
  for i, num_zeros in enumerate(zeros):
    num_ones = len(lst) - num_zeros
    if num_zeros > num_ones:
      gamma[i] = "0"
      epsilon[i] = "1"
      most_common[i] = "0"
    else:
      gamma[i] = "1"
      epsilon[i] = "0"
      most_common[i] = "1"
  
  gamma = int("".join(gamma), 2)
  epsilon = int("".join(epsilon), 2)

  print(gamma * epsilon)

  # Part 2
  oxygen = lst
  co2 = lst

  i = 0
  while len(oxygen) > 1:
    oxygen = [s for s in oxygen if s[i] == get_most_common(oxygen, i)]
    i += 1

  i = 0
  while len(co2) > 1:
    co2 = [s for s in co2 if s[i] != get_most_common(co2, i)]
    if len(co2) == 1:
      print(co2)
    i += 1

  oxygen = int("".join(oxygen[0]), 2)
  co2 = int("".join(co2[0]), 2)

  print(oxygen * co2)