tasks = []

try:
    with open("tasks.txt", "r") as f:
        tasks = [line.strip() for line in f]
except:
    pass

print(tasks)