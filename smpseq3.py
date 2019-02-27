num_first = input()
#num_first = 5
first_line = input().split(" ")
#first_line = "-2 -1 0 1 4".split(" ")

first_line = list(map(int, first_line))

num_second = input()
#num_second = 6

second_line = input().split(" ")

#second_line = "-3 -2 -1 1 2 3".split(" ")
second_line = list(map(int, second_line))

from collections import defaultdict

included = defaultdict(lambda: 0)
for num in second_line:
    included[num] += 1
    

for num in first_line:
    if included[num] == 0:
        print(num, end = " ")

print()
