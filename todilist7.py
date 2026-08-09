tasks = []

# load tasks
try:
    f = open("tasks.txt", "r")
    tasks = [line.strip() for line in f]
    f.close()
except:
    pass

while True:
    print("\n1.Add 2.View 3.Complete 4.Delete 5.Exit")
    ch = input("Enter: ")

    if ch == "1":
        t = input("Task: ")
        tasks.append("[ ] " + t)

    elif ch == "2":
        for i in range(len(tasks)):
            print(i, tasks[i])

    elif ch == "3":
        i = int(input("Index: "))
        if "[ ]" in tasks[i]:
            tasks[i] = tasks[i].replace("[ ]", "[✓]")

    elif ch == "4":
        i = int(input("Index: "))
        tasks.pop(i)

    elif ch == "5":
        f = open("tasks.txt", "w")
        for t in tasks:
            f.write(t + "\n")
        f.close()
        break