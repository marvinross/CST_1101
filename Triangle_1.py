rows = 5
for i in range(1, rows + 1):
    
    for x in range(rows - i):
        print(" ", end="")
    
    for y in range(2 * i - 1):
        print("*", end="")
    print()