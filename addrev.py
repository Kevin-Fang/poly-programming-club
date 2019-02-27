from sys import stdin

cases = int(stdin.readline())

def reverse_int(val):
    return int(str(val)[::-1])

# reverse string
for i in range(cases):
    first, second = [x for x in stdin.readline().split()]
    print(reverse_int(reverse_int(first) + reverse_int(second)))
