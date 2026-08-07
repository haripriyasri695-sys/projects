tasks = ["Study", "Practice"]

file = open("tasks.txt", "w")

for t in tasks:
    file.write(t + "\n")

file.close()

print("Saved!")