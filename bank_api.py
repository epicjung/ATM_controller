import pandas as pd
import csv

class User(object):
    def __init__(self, name, card_num, month, year, CVV, pin):
        self.name = name
        self.card_num = card_num
        self.month = month
        self.year = year
        self.CVV = CVV
        self.pin = pin
        self.balance = 0
        self.index = -1

    def __eq__(self, other):
        return self.name == other.name and self.card_num == other.card_num and \
                self.month == other.month and self.year == other.year and self.CVV == other.CVV 

    def __str__(self):
        return 'Name: {}\nCard Number: {}\nMonth/Year: {}\nCVV: {}\nBalance: {}\n'.format(self.name, self.card_num, self.month+'/'+self.year, self.CVV, self.balance)

class Bank(object):
    def __init__(self, database='private/database.csv'):
        self.users = []
        self.current_user = None
        self.database = database

        # Get information from database
        df = pd.read_csv(database)
        for i in range(df.shape[0]):
            user = User(str(df.iloc[i, 0]), str(df.iloc[i, 1]), str(df.iloc[i, 2]), str(df.iloc[i, 3]), str(df.iloc[i, 4]), str(df.iloc[i, 5]))
            user.balance = df.iloc[i, 6]
            user.index = i
            self.users.append(user)
        self.df = df

    def validate_user(self, query):
        found = False
        success = False
        for user in self.users:
            if user == query:
                found = True
                if query.pin == user.pin:
                    self.current_user = user
                    success = True

        if found:
            if success:
                print("\n***Validation success***")
            else:
                print("\n***Wrong PIN***")
        else:
            print("\n***Wrong credit card info***")

        return success

    def request_withdrawal(self, amount):
        if self.current_user:
            if amount > self.current_user.balance:
                print("Denied. Your current balance: ${}".format(self.current_user.balance))
            else:
                self.current_user.balance -= amount
                self.update_status()
                print("Complete. Your current balance: ${}".format(self.current_user.balance))
        else:
            print("System Danger. Shutting down...")

    def request_deposit(self, amount):
        if self.current_user:
            self.current_user.balance += amount
            self.update_status()
            print("Complete. Your current balance: ${}".format(self.current_user.balance))
        else:
            print("System Danger. Shutting down...")

    def request_balance(self):
        if self.current_user:
            print("Your current balance: ${}".format(self.current_user.balance))

    def update_status(self):
        # update changes (only balance)
        if self.current_user:
            self.df.iloc[self.current_user.index, -1] = self.current_user.balance
            self.df.to_csv(self.database, index=False)

    def logout(self):
        self.current_user = None
        # update balance


