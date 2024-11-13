WELCOME = "Welcome to mortgage calculator"
MESSAGE_1 = "Please input your loan amount ($): "
MESSAGE_2 = "Please input the annual percentage Rate(APR, %): "
MESSAGE_3 = "Please input your loan duration (years): "
ERROR_MESSAGE = "Please input a valid number"
OUTPUT_MESSAGE = "The calcuated monthly_payment is"

def prompt(message):
    print(f'==> {message}')

def is_invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True
    return False


prompt(WELCOME)

prompt(MESSAGE_1)
loan_amount = input()
while is_invalid_number(loan_amount):
    prompt(ERROR_MESSAGE)
    loan_amount = input()

prompt(MESSAGE_2)
annual_rate = input()
while is_invalid_number(annual_rate):
    prompt(ERROR_MESSAGE)
    annual_rate = input()
while float(annual_rate) <= 0:
    prompt(ERROR_MESSAGE)
    annual_rate = input()


prompt(MESSAGE_3)
year_duration = input()
while is_invalid_number(year_duration):
    prompt(ERROR_MESSAGE)
    year_duration = input()

monthly_rate = float(annual_rate) / 12 * 0.01
month_duration = float(year_duration) * 12
loan_amount = float(loan_amount)

monthly_payment = loan_amount * \
    (monthly_rate / (1 - (1 + monthly_rate)**(-month_duration)))

monthly_payment = round(monthly_payment, 3)

print(f'{OUTPUT_MESSAGE} ${monthly_payment}')


