class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

users = {}

try:
    with open("bank.txt", "r") as file:
        for line in file:
            name, balance = line.strip().split(",")
            users[name] = int(balance)
except FileNotFoundError:
    pass


while True:
    print("\n--- Banking System ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")

        if name in users:
            print("User already exists")
        else:
            balance = int(input("Enter initial amount: "))
            users[name] = balance
            print("Account created")

    elif choice == "2":
        name = input("Enter your name: ").lower()

        if name not in users:
            print("User not found")
            continue

        acc = Bank(name, users[name])

        while True:
            print(f"\nWelcome {name}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")

            ch = input("Enter choice: ")

            if ch == "1":
                amt = int(input("Enter amount: "))
                acc.deposit(amt)

            elif ch == "2":
                amt = int(input("Enter amount: "))
                acc.withdraw(amt)

            elif ch == "3":
                acc.show_balance()

            elif ch == "4":
                break

            else:
                print("Invalid choice")

            users[name] = acc.balance

    elif choice == "3":
        with open("bank.txt", "w") as file:
            for name, balance in users.items():
                file.write(f"{name},{balance}\n")

        print("Data saved. Bye ")
        break

    else:
        print("Invalid choice")
