def show_balence(balence):
    print(f"Your current balance is: ₹{balence:.2f}")

def deposit_amount():
    amount = float(input("Enter amount to deposit: ₹ "))
    if amount < 0:
        print("Deposit amount cannot be negative.")
    else:   
       return amount

def withdraw_amount(balence):
    amount = float(input("Enter amount to withdraw: ₹ "))

    if amount > balence:
        print("Insufficient balance.")
        return 0
    elif amount < 0: 
        print(f"Amount cannot be negative.")
        return 0
    else:
        return amount 
    
def main():
    balence=0.0
    is_running=True

    while is_running:
        print("Welcome to the Banking Program")
        print("1. Show Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            show_balence(balence)
        elif choice == '2':
            balence+=deposit_amount()
        elif choice == '3':
            balence-=withdraw_amount(balence)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid option. Please try again.")

    print("Thank you for using the Banking Program Have a nice day!!")

if __name__ == "__main__":
    main()