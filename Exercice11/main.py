## Écrivez votre code ici !


class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        try:
            if amount <= 0:
                print("Veuillez saisir un montant valide")
            else:
                self.balance += amount
        except TypeError:
            print("Veuillez saisir un nombre.")

    def withdraw(self, amount):
        try:
            if self.balance - amount < 0:
                print(f" Vous essayez de retirer {amount}€, mais votre solde est de {self.balance}€")

            elif self.balance >= amount:
                self.balance -= amount
                print(f"Vous avez retiré {amount}€")
                print(f"votre nouveau solde est de {self.balance}€")

            else:
                print("Veuillez saisir un montant valide")

        except TypeError:
            print("Veuillez saisir un nombre.")

    def display_balance(self):
        print(f"Nom: {self.account_holder}, Solde: {self.balance}€")


bank = BankAccount("Marc", 2000)
bank.display_balance()
print("---")
bank.deposit(200)
bank.display_balance()
print("---")
bank.withdraw(1000)
