CURRENT_BALANCE = 5000


def atm_withdrawal(withdrawal_amount):
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False

    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False

    if withdrawal_amount > CURRENT_BALANCE:
        print(f"Error: Insufficient balance. Available: {CURRENT_BALANCE}")
        return False

    remaining_balance = CURRENT_BALANCE - withdrawal_amount
    print(f"Withdrawal successful. Amount: {withdrawal_amount}")
    print(f"Remaining balance: {remaining_balance}")
    return True



withdrawal_amount = int(input("Enter withdrawal amount: "))
result = atm_withdrawal(withdrawal_amount)
print(f"Return: {result}")

# --- Test Cases ---

print("Test 1: Valid withdrawal (2000)")
atm_withdrawal(2000)

print("\nTest 2: Invalid amount - not greater than 0 (-500)")
atm_withdrawal(-500)

print("\nTest 3: Invalid amount - not a multiple of 500 (300)")
atm_withdrawal(300)

print("\nTest 4: Invalid amount - insufficient balance (6000)")
atm_withdrawal(6000)
