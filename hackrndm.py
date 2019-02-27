n, k = input().split(" ")

n = int(n)
k = int(k)
num_vals = input().split(" ")

num_vals = list(map(int, num_vals))

numbers = {}

for num in num_vals:
    try:
        numbers[num] += 1 
    except KeyError:
        numbers[num] = 1

num_pairs = 0

for num in numbers:
    try:
        numbers[num - k]
        num_pairs += numbers[num - k]
    except KeyError:
        pass

    try:
        numbers[num + k]
        num_pairs += numbers[num + k]
    except KeyError:
        pass

print(num_pairs // 2)
