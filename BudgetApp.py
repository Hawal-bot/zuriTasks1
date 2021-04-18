import os
import sys
class BudgetApp():
    def __init__(self):
        self.deposit = 0
        self.withdrawals = 0
        self.withdrawal_list = []
        self.withdrawal_name = []
        self.deposit_name = []
        self.deposit_list = []

        self.prompt_deposit()
    def deposit_ask(self):
        add_deposit = input('Add a deposit category? [y/n]: ')
        return add_deposit
    def deposit_sum(self):
        self.deposit = sum(self.deposit_list)
    def withdrawal_ask(self):
        add_withdrawal = input('Add withdrawal category? [y/n]: ')
        return add_withdrawal
    def withdrawal_sum(self):
        self.withdrawals = sum(self.withdrawal_list)
    def deposit_check(self):
        if not self.deposit_list:
            print('Please enter atleast one deposit category. ')
            self.prompt_deposit()
        else:
            return
    def withdrawal_check(self):
        if not self.withdrawal_list:
            print('Please enter atleast one withdrawal caegory. ')
            self.prompt_withdrawal()
        else:
            return
    def prompt_deposit(self):
        x = False
        while not x:
            result = self.deposit_ask()
            if result == 'y':
                deposit_input = int(input('Enter amount to deposit. [Numbers Only]: '))
                self.deposit_list.append(deposit_input)
                deposit_name = input('Enter deposit category. [Name Only]: ')
                self.deposit_name.append(deposit_name)
            else:
                self.deposit_check()
                x = True
        self.deposit_sum()
        name = [name for name in self.deposit_name]
        deposit = [deposit for deposit in self.deposit_list]
        depositdict = dict(zip(name, deposit))
        for k in depositdict:
            print(k + ': ', 'NGN' + str(depositdict[k]))
        print('Total user deposit: ', 'NGN' + str(self.deposit))
        self.prompt_withdrawal()
    def prompt_withdrawal(self):
        x = False
        while not x:
            result = self.withdrawal_ask()
            if result == 'y':
                withdrawal_input = int(input('Enter withdrawal amount. [Numbers Only]: '))
                self.withdrawal_list.append(withdrawal_input)
                withdrawal_name = input('Enter withdrawal category. [Name Only]: ')
                self.withdrawal_name.append(withdrawal_name)
            else:
                self.withdrawal_check()
                x = True
        self.withdrawal_sum()
        name = [name for name in self.withdrawal_name]
        withdrawal = [deposit for deposit in self.withdrawal_list]
        withdrawaldict = dict(zip(name, withdrawal))
        for k in withdrawaldict:
            print(k + ': ', 'NGN' + str(withdrawaldict[k]))
        print('Total user withdrawals: ', 'NGN' + str(self.withdrawals))
        self.uservalue()

    def uservalue(self):
        valoutput = self.deposit - self.withdrawals
        if valoutput < 0:
            print('You have spent beyond your budget and have ' + 'NGN' + str(valoutput))
        if valoutput == 0:
            print('You have spent all your budget')
        if valoutput > 0:
            print('You have a balance of, ' + 'NGN' + str(valoutput))
        else:
            self.close_program()

    def close_program(self):
        print('Exiting Program.')
        sys.exit(0)

if __name__ == '__main__':
    BudgetApp()