from sys import stdin

items = []

while True:
    item = input()
    if item == "42":
        exit()
    else:
        print(item)
