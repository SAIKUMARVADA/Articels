from models import Account
accounts = {}
current_id = 1


def create_account(name, email, initial_deposit):
    global current_id
    acc = Account(
        account_number=current_id,
        name=name,
        email=email,
        balance=initial_deposit
    )
    accounts[current_id] = acc
    current_id += 1
    return acc

def get_account(account_number):
    return accounts.get(account_number)

def deposit(account_number, amount):
    acc = get_account(account_number)
    if acc:
        acc.balance += amount
        return acc
    return None

def withdraw(account_number, amount):
    acc = get_account(account_number)
    if acc and acc.balance >= amount:
        acc.balance -= amount
        return acc
    return None

def delete_account(account_number):
    return accounts.pop(account_number, None)

def transaction_history(account_number):
    return get_account(account_number)

def email_update(account_number, new_email):
    acc = get_account(account_number)
    if acc:
        acc.email = new_email
        return acc
    raise Exception("Account not found")

# Add a pin dictionary
account_pins = {}

def change_pin(account_id, old_pin, new_pin):
    if account_id not in accounts:
        raise Exception("Account not found")
    
    current_pin = account_pins.get(account_id)
    if current_pin is not None and current_pin != old_pin:
        raise ValueError("Old PIN does not match")

    account_pins[account_id] = new_pin
    return {"account_number": account_id}
