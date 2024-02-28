
rows = 6
num = 1  
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        if num < 19:
            print(" ", end=" ") 
        print(num, end="  ")
        num += 1
    print()

