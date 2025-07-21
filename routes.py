import json
import os

from fastapi import APIRouter, HTTPException
from models import AccountCreate, Transaction, EmailUpdate, ChangePin, Account
from utility import (
    create_account,
    get_account,
    deposit,
    withdraw,
    delete_account,
    transaction_history,
    email_update,
    change_pin,
)

DATA_FILE = os.path.join("storage", "data.json")

def read_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

router = APIRouter()


@router.post("/create")
def create(ac: AccountCreate):
    acc = create_account(ac.name, ac.email, ac.initial_deposit)
    return {"message": "Account created", "account": acc}


@router.get("/balance/{acc_no}")
def get_balance(acc_no: int):
    acc = get_account(acc_no)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"balance": acc.balance}


@router.post("/deposit")
def do_deposit(txn: Transaction):
    acc = deposit(txn.account_number, txn.amount)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": "Deposit successful", "balance": acc.balance}


@router.post("/withdraw")
def do_withdraw(txn: Transaction):
    acc = withdraw(txn.account_number, txn.amount)
    if not acc:
        raise HTTPException(status_code=400, detail="Insufficient funds or account not found")
    return {"message": "Withdrawal successful", "balance": acc.balance}


@router.delete("/delete/{acc_no}")
def delete(acc_no: int):
    acc = delete_account(acc_no)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": "Account deleted"}


@router.get("/transaction_history/{acc_no}")
def get_transaction_history(acc_no: int):
    acc = transaction_history(acc_no)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"balance": acc.balance}


@router.put("/email/update")
def update_user_email(request: EmailUpdate):
    try:
        result = email_update(request.account_number, request.new_email)
        return {"message": "Email updated successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/change_pin", summary="Change account PIN")
def change_account_pin(req: ChangePin):
    try:
        result = change_pin(
            account_id=req.account_number,
            old_pin=req.old_pin,
            new_pin=req.new_pin,
        )
        return {
            "message": "PIN changed successfully",
            "data": result
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to change PIN")
