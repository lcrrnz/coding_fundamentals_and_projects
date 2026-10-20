#Cree una clase de `BankAccount` que:
#Tenga un atributo de `balance`.
#Tenga un método para ingresar dinero.
#Tengo un método para retirar dinero.
#Cree otra clase que herede de esta llamada `SavingsAccount` que:
#Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.

class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f'Transaction successful. Current balance: {self.balance}')
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f'Transaction successful. Current balance: {self.balance}')


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f'Unable to withdraw {amount}: must maintain a minimum balance of {self.min_balance}.')
        else:
            super().withdraw(amount)


account1 = SavingsAccount(min_balance=100)
account1.deposit(200)
account1.withdraw(50)
account1.withdraw(100)