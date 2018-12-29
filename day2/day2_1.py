twoCount = 0
threeCount = 0

with open("input.txt") as file:
  data = file.readlines()
  for line in data:
    count = {}
    print(line)
    for c in line:
      #print(c)
      if c in count:
        count[c] = count[c] + 1
      else: count[c] = 1

    #Now, check if we have exactly 2 or exactly 3 of any letters
    foundTwo = False
    foundThree = False
    for key, value in count.items():
      print(f'Key is {key} and value is {value}')
      if value == 2 and not foundTwo: 
        twoCount += 1
        foundTwo = True
      if value == 3 and not foundThree: 
        threeCount += 1
        foundThree = True

checkSum = twoCount * threeCount

print(f'twoCount is {twoCount}')
print(f'threeCount is {threeCount}')
print(f'checkSum is {checkSum}')