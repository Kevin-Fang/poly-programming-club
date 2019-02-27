input_time = int(input())

if input_time < 0:
    print("total second must be a positive integer")
    exit()

num_hours = input_time // 3600
num_seconds = input_time % 3600
num_minutes = num_seconds // 60
num_seconds = num_seconds % 60

print("{}:{}:{}".format(str(num_hours).zfill(2), str(num_minutes).zfill(2), str(num_seconds).zfill(2)))
