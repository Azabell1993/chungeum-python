# 전역 변수
current_value = 0

def add(number):
    global current_value
    current_value += number
    print(f"Added {number}: Current Value = {current_value}")

def subtract(number):
    global current_value
    current_value -= number
    print(f"Subtracted {number}: Current Value = {current_value}")

def multiply(number):
    global current_value
    current_value *= number
    print(f"Multiplied by {number}: Current Value = {current_value}")

def divide(number):
    global current_value
    if number != 0:
        current_value /= number
        print(f"Divided by {number}: Current Value = {current_value}")
    else:
        print("Cannot divide by zero.")

def reset():
    global current_value
    current_value = 0
    print(f"Reset: Current Value = {current_value}")

# Demonstration of the calculator functions
add(5)        # Should update current_value to 5
subtract(3)   # Should update current_value to 2
multiply(10)  # Should update current_value to 20
divide(2)     # Should update current_value to 10
reset()       # Should reset current_value to 0