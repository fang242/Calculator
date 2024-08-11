# print message to prompt user for an x and y 
# value and an operation you wish to be computed
# return x, y, and operation

def capture_input():
    while True:
        try: 
            x = float(input("First Argument: "))
            y = float(input("Second Argument: "))
            op = input("Select an Operation \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n Operation: ")
        except ValueError:
            print("Make sure arguments are numbers.")
            continue
        if op in ["1","2","3","4"]:
            break
        else:
            print("Make sure operation choice is 1, 2, ,3, or 4")
            continue
    return op, x, y

def calculate(op, x, y):
    while True:
        match op:
            case "1":
                return x + y
            case "2":
                return x -y
            case "3":
                return x*y
            case "4":
                return round(x/y, 3)

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
            print(f"{x} divided by {y} = {result}.")


def run():
    op1, x1, y1 = capture_input()
    result = calculate(op1, x1, y1)
    print_output(op1, x1, y1, result)
    

# don't worry about this, it is to run your code
if __name__ == '__main__':
    run()