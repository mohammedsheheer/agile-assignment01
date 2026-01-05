balance = 10000

withdrawAmount = input("Enter the amount to be withdrawn(in Rs): ")

if(withdrawAmount % 100 == 0 and withdrawAmount > 0 and withdrawAmount < balance):
    balance -= withdrawAmount
    print("Withdrawal successful!")
    print(f"Current balance is {balance}")
