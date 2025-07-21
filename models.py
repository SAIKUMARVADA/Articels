from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    email: str
    initial_deposit: float

class Account(BaseModel):
    account_number: int
    name: str
    email: str
    balance: float

class Transaction(BaseModel):
    account_number: int
    amount: float

class EmailUpdate(BaseModel):
    account_number:int
    old_email: str
    new_email: str

class ChangePin(BaseModel):
    account_number:int
    old_pin: str
    new_pin:str