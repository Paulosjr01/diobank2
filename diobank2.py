from datetime import datetime

class User:
    def __init__(self, name, account_number, initial_balance=0, withdrawal_limit=1000):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance
        self.withdrawal_limit = withdrawal_limit
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            'transaction': 'Deposito',
            'amount': amount,
            'balance': self.balance,
            'datetime': datetime.now()
        })
        print("Deposito efetuado com sucesso. Saldo atualizado: $", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo insuficiente")
        elif amount > self.withdrawal_limit:
            print("Excede o limite de saque")
        else:
            self.balance -= amount
            self.transactions.append({
                'transaction': 'Saque',
                'amount': -amount,
                'balance': self.balance,
                'datetime': datetime.now()
            })
            print("Saque efetuado com sucesso. Saldo: $", self.balance)

    def display_statement(self):
        print("\nExtrato para", self.name)
        print("{:<12} {:<10} {:<10} {:<20}".format('Transacao', 'Valor', 'Saldo', 'Data Hora'))
        for transaction in self.transactions:
            print("{:<12} {:<10} {:<10} {:<20}".format(transaction['transaction'],
                                                        transaction['amount'],
                                                        transaction['balance'],
                                                        transaction['datetime'].strftime('%d/%m/%Y %H:%M')))


class Bank:
    def __init__(self):
        self.users = {}

    def create_user(self, name, account_number, initial_balance=0, withdrawal_limit=1000):
        if account_number in self.users:
            print("Numero de conta ja existe. Escolha um numero de conta diferente.")
        else:
            new_user = User(name, account_number, initial_balance, withdrawal_limit)
            self.users[account_number] = new_user
            print(f"Usuario {name} com numero de conta {account_number} criado com sucesso.")

    def get_user(self, account_number):
        if account_number in self.users:
            return self.users[account_number]
        else:
            print("Usuario nao encontrado. Verifique o numero da conta.")

    def deposit(self, account_number, amount):
        user = self.get_user(account_number)
        if user:
            user.deposit(amount)

    def withdraw(self, account_number, amount):
        user = self.get_user(account_number)
        if user:
            user.withdraw(amount)

    def display_statement(self, account_number):
        user = self.get_user(account_number)
        if user:
            user.display_statement()

    def display_menu(self):
        print("\nMenu do Banco:")
        print("1. Deposito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Criar Usuario")
        print("5. Mostrar Todos os Usuarios")
        print("6. Sair")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nSelecione uma opcao (1-6): ")
            if choice == '1':
                account_number = input("Informe o numero da conta: ")
                amount = float(input("Insira o valor do deposito: "))
                self.deposit(account_number, amount)
            elif choice == '2':
                account_number = input("Informe o numero da conta: ")
                amount = float(input("Informe o valor do saque: "))
                self.withdraw(account_number, amount)
            elif choice == '3':
                account_number = input("Informe o numero da conta: ")
                self.display_statement(account_number)
            elif choice == '4':
                self.create_user_from_input()
            elif choice == '5':
                self.show_all_users()
            elif choice == '6':
                print("Saindo do banco. Obrigado!")
                break
            else:
                print("Escolha invalida. Por favor, informe um numero entre 1 e 6.")

    def create_user_from_input(self):
        name = input("Informe o nome do usuario: ")
        account_number = input("Informe o numero da conta: ")
        initial_balance = float(input("Informe o saldo inicial (opcional, default 0): ") or 0)
        withdrawal_limit = float(input("Informe o limite de saque (opcional, default 1000): ") or 1000)
        self.create_user(name, account_number, initial_balance, withdrawal_limit)

    def show_all_users(self):
        print("\nTodos os Usuarios:")
        print("{:<20} {:<20} {:<15} {:<15}".format('Nome', 'Numero da Conta', 'Saldo', 'Limite de Saque'))
        for user in self.users.values():
            print("{:<20} {:<20} {:<15} {:<15}".format(user.name, user.account_number, user.balance, user.withdrawal_limit))


# Example usage:
if __name__ == "__main__":
    bank = Bank()
    bank.run()