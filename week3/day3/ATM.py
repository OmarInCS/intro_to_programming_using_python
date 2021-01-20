from week3.day2.account import Account

acc_list = []
for i in range(10):
    acc_list.append(Account(i, 10000))

while True:
    id = eval(input("Enter an account id: "))
    current_acc = acc_list[id]
    while True:
        menu = """
        Main menu
        1: check balance
        2: withdraw
        3: deposit
        4: exit
        """
        print(menu)
        choice = eval(input("Enter a choice: "))

        if choice == 1:
            print("The balance is", current_acc.get_balance())
        elif choice == 2:
            amt = eval(input("Enter an amount to withdraw: "))
            current_acc.withdraw(amt)
        elif choice == 3:
            amt = eval(input("Enter an amount to deposit: "))
            current_acc.deposit(amt)
        else:
            break

