
def decode_output(output, str_to_num):
  result = [""] * 4
  for i in range(len(output)):
    result[i] = str_to_num[output[i]]
  print(int(''.join([str(x) for x in result])))
  return int(''.join([str(x) for x in result]))

def solve():

  data = []

  str_len_to_num = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
  }

  with open('day8.txt') as f:
    for x in f.readlines():
      line = str(x).strip().split(" | ")
      data.append([[''.join(sorted(x)) for x in line[0].strip().split()], [''.join(sorted(x)) for x in line[1].strip().split()]])

  sum = 0

  for line in data:
    unique = line[0]
    output = line[1]
    str_to_num = {}
    num_to_str = {}
    # get all the unique values first
    for s in unique:
      # if the string is of any of the known unique lengths, can decode directly
      if len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7:
        num = str_len_to_num[len(s)]
        str_to_num[s] = num
        num_to_str[num] = s
    unique = [x for x in unique if len(x) != 2 and len(x) != 3 and len(x) != 4 and len(x) != 7]
    # deduce the other values
    for s in unique:
      # if the string is of length 6, it is either 6, 0 or 9
      if len(s) == 6:
        # if the string contains all the segments of a 4 it has to be 9
        count = 0
        for char in s:
          if char in num_to_str[4]:
            count += 1
        if count == 4:
          num_to_str[9] = s
          str_to_num[s] = 9
          continue
        # if the string has 3 segments in common with 7 it is 0
        count = 0
        for char in s:
          if char in num_to_str[7]:
            count += 1
        if count == 3:
          num_to_str[0] = s
          str_to_num[s] = 0
          continue
        # if the loop is still continuing the string is 6
        num_to_str[6] = s
        str_to_num[s] = 6
        continue
      elif len(s) == 5:
        # if the string has 2 segments common with 1 it is 3
        count = 0
        for char in s:
          if char in num_to_str[1]:
            count += 1
        if count == 2:
          num_to_str[3] = s
          str_to_num[s] = 3
          continue
        # if the string has 3 segments in common with 4 it is 5
        count = 0
        for char in s:
          if char in num_to_str[4]:
            count += 1
        if count == 3:
          num_to_str[5] = s
          str_to_num[s] = 5
          continue
        # if the loop is still continuing the string is 2
        num_to_str[2] = s
        str_to_num[s] = 2
        continue
    # decode output
    sum += decode_output(output, str_to_num)
      
  print(sum)

  

