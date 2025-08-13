from datetime import datetime

cust_file = "cust_data.txt"
txn_file = "txn_data.txt"

def record_txn(acc_no, typ, amt, bal):
    try:
        with open(txn_file, "a") as f:
            f.write(f"{datetime.now()},{acc_no},{typ},{amt},{bal}\n")
    except:
        print("Error saving transaction.")

def read_customers():
    data = {}
    try:
        with open(cust_file, "r") as f:
            for line in f:
                nm, acc, bal = line.strip().split(",")
                data[acc] = [nm, float(bal)]
    except FileNotFoundError:
        pass
    return data

def write_customers(data):
    try:
        with open(cust_file, "w") as f:
            for acc, (nm, bal) in data.items():
                f.write(f"{nm},{acc},{bal}\n")
    except:
        print("Error saving customers.")

def new_customer():
    data = read_customers()
    nm = input("Name: ").strip()
    acc = input("Account No: ").strip()
    if acc in data:
        print("Account exists.")
        return
    data[acc] = [nm, 0.0]
    write_customers(data)
    print("Customer added.")

def add_money():
    data = read_customers()
    acc = input("Account No: ").strip()
    if acc not in data:
        print("Account not found.")
        return
    amt = float(input("Amount to deposit: "))
    data[acc][1] += amt
    write_customers(data)
    record_txn(acc, "Deposit", amt, data[acc][1])
    print("Deposit done.")

def take_money():
    data = read_customers()
    acc = input("Account No: ").strip()
    if acc not in data:
        print("Account not found.")
        return
    amt = float(input("Amount to withdraw: "))
    if amt > data[acc][1]:
        print("Not enough balance.")
        return
    data[acc][1] -= amt
    write_customers(data)
    record_txn(acc, "Withdraw", amt, data[acc][1])
    print("Withdrawal done.")

def show_all():
    data = read_customers()
    if not data:
        print("No data.")
        return
    print("\n-- Customers --")
    for acc, (nm, bal) in data.items():
        print(f"{nm} | {acc} | {bal}")

def main():
    while True:
        print("\n-- Menu --")
        print("1. New Customer")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Customers")
        print("5. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            new_customer()
        elif ch == "2":
            add_money()
        elif ch == "3":
            take_money()
        elif ch == "4":
            show_all()
        elif ch == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
