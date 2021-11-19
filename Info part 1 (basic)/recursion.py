# RECURSION
# is a function that calls itself
# see the calculator function below, how it is called at the end of the loop to start over


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    wordz = "second"
    keep_going = True
    while keep_going:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input(f"What's the {wordz} number?: "))
        # in the model answer, the teacher split the below line into two, using a variable called calculation_function.
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower() == "y":
            num1 = answer
            wordz = "next"
        else:
            keep_going = False
            calculator()


calculator()
