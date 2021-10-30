from ATM_controller.bank_api import *
import time
class Controller:
    def __init__(self):
        self.server = Bank()
        pass
    
    def insert_card(self):
        print("\nWaiting for your card...")
        name = input("Name: ")
        card = input("Card number (15 digit): ")
        month = input("Expiration month (1-2 digit): ")
        year = input("Expiration year (2 digit): ")
        CVV = input("CVV (3 digit): ")
        self.name = name
        self.card_number = card
        self.month = month
        self.year = year
        self.CVV = CVV

    def insert_pin(self):
        pin = input("Your pin number: ")
        query = User(self.name, self.card_number, self.month, self.year, self.CVV, pin)
        return self.server.validate_user(query)
    
    def run(self):
        # loop
        while (1):
            while (1):
                self.insert_card()
                if self.insert_pin():
                    break
                time.sleep(0.5)

            # proceed to withdarw/deposit
            while (1):
                choice = input('''\n1. Withdraw\n2. Deposit\n3. See Balance\n4. Quit\nPlease select your option: ''')
                if choice == "1":
                    amount = int(input("Amount of withdrawal: "))
                    self.server.request_withdrawal(amount)
                elif choice == "2":
                    amount = int(input("Amount of deposit: "))
                    self.server.request_deposit(amount)
                elif choice == "3":
                    self.server.request_balance()
                elif choice == "4":
                    self.server.logout()
                    break
                else:
                    print("Wrong option")

                time.sleep(0.5)
            time.sleep(0.5)


