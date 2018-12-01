
sum = 0

values = {}
values[sum] = 1

reachTwice = 99
foundIt = False

while not foundIt:
    print("Opening file...")
    with open("input.txt") as file:
        
        data = file.readlines()    
        for line in data:
            sum = sum + int(line)
            if sum in values:
                print("Found it")
                reachTwice = sum
                foundIt = True
                break
            else:
                print(f"Adding {sum} to dictionary")
                values[sum] = 1
            
print(reachTwice)
    
