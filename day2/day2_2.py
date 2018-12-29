with open("input.txt") as file1:
  data1 = file1.readlines()
  line_num_1 = 0
  for line1 in data1:
    #print(line1)
    with open("input.txt") as file2:
      data2 = file2.readlines()
      line_num_2 = 0
      for line2 in data2:
        #print(line2)
        if (len(line1) != len(line2)): 
            continue
        else:
            num_chars_diff = 0 
            for i,c in enumerate(line1):
                if num_chars_diff > 1:
                    break
                if line1[i] != line2[i]:
                    num_chars_diff += 1
            if num_chars_diff == 1:
                print(f"Found it: lines {line_num_1} and {line_num_2}")
                print(f"Line 1: {line1}")
                print(f"Line 2: {line2}")
        line_num_2 += 1
    line_num_1 += 1