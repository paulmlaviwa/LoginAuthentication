username = input('Enter your username: ')
password = input('Type your password: ')
hidden_password = '*' * len(password)
print(f'{username}, your password {hidden_password} is {len(hidden_password)} characters long!')