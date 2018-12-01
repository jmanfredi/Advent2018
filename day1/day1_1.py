with open("input.txt") as file:

    data = file.readlines()

    sum = 0
    
    for line in data:
        sum = sum + int(line)

    print(sum)
