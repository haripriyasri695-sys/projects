tasks = [["Study", False], ["Practice", False]]

for i, t in enumerate(tasks, 1):
    status = "✔" if t[1] else "✘"
    print(i, t[0], status)

n = int(input("Mark complete number: "))
tasks[n-1][1] = True

print(tasks)