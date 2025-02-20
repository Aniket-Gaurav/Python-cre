import os


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


operations = {
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
    "/": divide_numbers
}


first_number = float(input("Enter the first number: "))

print("Available operations:")
for operation in operations:
    print(operation)

while True:
    chosen_operation = input("Pick an operation: ")
    second_number = float(input("Enter the second number: "))

    calculation_function = operations[chosen_operation]
    result = calculation_function(first_number, second_number)

    print(f"{first_number} {chosen_operation} {second_number} = {result}")

    should_continue = input(
        f"Enter 'y' to continue calculations with {result} or 'n' to exit: "
    ).lower()

    if should_continue == "y":
        first_number = result
        os.system('cls')
    else:
        break