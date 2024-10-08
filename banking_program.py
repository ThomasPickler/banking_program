


def show_balance():
    print(f'Your balance is ${balance:.2f}')


def deposit():
    amount = float(input('Enter the amout to be deposited: '))

    if amount < 0:
        print('The amount should be greater than 0.00')
        return 0
    else:
        return amount


def withdraw():
    amount = float(input('Enter amount to be withdrawn: '))

    if amount > balance:
        print('Insufficient funds')
        return 0
    elif amount < 0:
        print('Amount must be greater than 0.00')
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print('Bank of Python')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    choice = input('Enter a number (1-4): ')

    if choice == '1':
        show_balance()
    if choice == '2':
        balance += deposit()
    if choice == '3':
        balance -= withdraw()
    if choice == '4':
        is_running = False
    else:
        print('Choose a number between 1 and 4.')

print('Exiting the program.')