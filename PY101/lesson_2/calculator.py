import json

with open('messages.json', 'r') as file:
    data = json.load(file)


# welcome_message = 'Welcome to Calculator'
# input_message_1 = "Please input your first number: "
# input_message_2 = "Please input your second number: "
# operation_message = '''What operation do you want?
# 1)add 2)subtract 3)multiply 4)divide'''
# error_message_1 = "Hmm... it looks like not a valid number"
# error_message_2 = "Please input a valid operation: 1/2/3/4"

language = input("Please select your language: 1) English 2)Chinese ")

def prompt(message):
    print('==> ' + message)

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt(data[language]["welcome_message"])
continue_flag = 1

while continue_flag == 1:
    prompt(data[language]["input_message_1"])
    num1 = input()
    while invalid_number(num1):
        prompt(data[language]["error_message_1"])
        num1 = input()

    prompt(data[language]["input_message_2"])
    num2 = input()
    while invalid_number(num2):
        prompt(data[language]["error_message_2"])
        num2 = input()

    prompt(data[language]["operation_message"])
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(data[language]["error_message_3"])
        operation = input()

    if '.' not in num1 + num2:
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
    else:
        match operation:
            case "1":
                output = float(num1) + float(num2)
            case "2":
                output = float(num1) - float(num2)
            case "3":
                output = float(num1) * float(num2)
            case "4":
                if float(num2) == 0.0:
                    print('divisor can\'t be zero')
                    output = None
                else:
                    output = float(num1) / float(num2)
        output = round(output, 2)
    if output is not None:
        print(f'{data[language]["output_message"]} {output}')

    prompt(data[language]['continue_message'])
    check = input()
    continue_flag = 0 if check not in ['Y', 'y'] else 1
