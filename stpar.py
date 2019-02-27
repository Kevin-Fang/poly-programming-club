length = int(input())

while length > 0:
    truck_order = list(map(int, input().split(" ")))

    current_inc = 1
    stored_trucks = []

    pointer = 0
    while pointer < len(truck_order):
        curr_truck = truck_order[pointer]
        if curr_truck == current_inc:
            current_inc += 1
            pointer += 1
            pass
        elif len(stored_trucks) > 0 and stored_trucks[-1] == current_inc:
            truck_order.insert(pointer, stored_trucks.pop())
            current_inc += 1
            pointer += 1
        else:
            stored_trucks.append(truck_order.pop(pointer))

    for i in stored_trucks[::-1]:
        truck_order.append(i)

    
    found = False
    for i, x in enumerate(truck_order[:-1]):
        if x != truck_order[i + 1] - 1:
            found = True
    if found == False:
        print("yes")
    else:
        print("no")
    length = int(input())
