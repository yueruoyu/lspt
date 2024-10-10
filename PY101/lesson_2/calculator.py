
welcome_message = 'Welcome to Calculator'
message1 = "Please input your first number: "
message2 = "Please input your second number: "
message3 = '''What operation do you want?
1)add 2)subtract 3)multiply 4)divide'''
error_message1 = "Hmm... it looks like not a valid number"
error_message2 = "Please input a valid operation: 1/2/3/4"

def prompt(message):
    print('==> ' + message)

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(welcome_message)

prompt(message1)
num1 = input()
while invalid_number(num1):
    prompt(error_message1)
    num1 = input()

prompt(message2)
num2 = input()
while invalid_number(num2):
    prompt(error_message1)
    num2 = input()

prompt(message3)
operation = input()
while operation not in ['1', '2', '3', '4']:
    prompt(error_message2)
    operation = input()

match operation:
    case "1":
        output = int(num1) + int(num2)
    case "2":
        output = int(num1) - int(num2)
    case "3":
        output = int(num1) * int(num2)
    case "4":
        if int(num2) == 0:
            print('divisor can\'t be zero')
            output = None
        else:
            output = int(num1) / int(num2)

if output is not None:
    print(f'The result is {output}')
