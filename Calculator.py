# print message to prompt user for an x and y 
# value and an operation you wish to be computed
# return x, y, and operation

def capture_input():
    x = input("First Argument: ")
    y = input("Second Argument: ")
    op = input("Select an Operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n Operation: ")
    return op, x, y

def calculate(op, x, y):
    match op:
        case "1":
            return float(x) + float(y)
        case "2":
            return float(x) -float(y)
        case "3":
            return float(x)*float(y)
        case "4":
            return float(x)/float(y)
        case _:
            print("Wrong Operation Input")
            global op1, x1, y1
            op1, x1, y1 = capture_input()
            return calculate(op1,x1,y1)

def print_output(op, x, y, result):
    print("Result: ")
    match op:
        case "1":
            print(f"{x} plus {y} is {result}.")
        case "2":
            print(f"{x} minus {y} = {result}.")
        case "3":
            print(f"{x} times {y} = {result}.")
        case "4":
            print(f"{x} divide by {y} = {result}.")
        case _:
            print("Error: something odd has happened")
            print(f"Error:{op} - operation. {x} - first. {y} - second. {result} - result")

def run():
    global op1, x1, y1
    op1, x1, y1 = capture_input()
    result = calculate(op1, x1, y1)
    print_output(op1, x1, y1, result)
    

# don't worry about this, it is to run your code
if __name__ == '__main__':
    run()