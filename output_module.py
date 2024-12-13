def display_result(result, operation, a, b):
    print(f"The {operation} of {a} and {b} is {result}")
    with open("calculations.txt", "a") as file:
        file.write(f"The {operation} of {a} and {b} is {result}")
