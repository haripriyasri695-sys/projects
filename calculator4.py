# Day 4 Calculator App

print("===== Smart Calculator =====")
print("Type 'exit' to quit")
print("Type 'history' to see last 3 calculations")
print("Type 'clear' to clear history")
print("Example: 5 + 3 * 2")

history = []  # list to store past calculations

while True:
    expression = input("\nEnter calculation: ")

    # Exit condition
    if expression.lower() == "exit":
        print("Calculator closed.")
        break

    # Show history
    elif expression.lower() == "history":
        if len(history) == 0:
            print("No history available.")
        else:
            print("Last calculations:")
            for item in history[-3:]:
                print(item)
        continue

    # Clear history
    elif expression.lower() == "clear":
        history.clear()
        print("History cleared.")
        continue

    # Calculation with error handling
    try:
        result = eval(expression)
        output = f"{expression} = {result}"
        print("Result:", result)

        history.append(output)  # store in history

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except:
        print("Error: Invalid input!")