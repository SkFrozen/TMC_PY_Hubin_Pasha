def calculater(number_1: int, number_2: int, action: str) -> int:
    """Receives 2 numbers and performes an action and return result"""
    if action == "-":
        return number_1 - number_2
    elif action == "+":
        return number_1 + number_2
    elif action == "*":
        return number_1 * number_2
    elif action == "/":
        return number_1 / number_2


try:
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    action = input("Enter an action what do you like to use, example (+, -, *, /): ")
    if "+, -, *, /".find(action) == -1:
        raise TypeError("Action not found")
    print(round(calculater(num_1, num_2, action), 3))
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
except ValueError as e:
    print("Enter valid data:", e)
