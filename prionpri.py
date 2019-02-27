import math
num_lines = int(input())

for i in range(num_lines):
    num = int(input())
    # only need to go to sqrt(n)
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")
