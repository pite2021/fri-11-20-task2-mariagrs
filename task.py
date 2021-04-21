import random
from dataclasses import dataclass, field


def get_random_account_number():
    return random.randrange(1000, 2000)


@dataclass()
class Client:
    name: str
    lastname: str
    total_amount_cash: int
    account_number: int = field(init=False, default_factory=get_random_account_number)

    def print_information(self):
        return '\nName : {} \nLastname : {} \nAccount number : {} \nTotal amount in account: {} $' \
            .format(self.name, self.lastname, self.account_number, self.total_amount_cash)

    @property
    def amount_money(self):
        return self.total_amount_cash

    @amount_money.setter
    def amount_money(self, money):
        if money < 0:
            raise ValueError()
        self.total_amount_cash = money

    def change_bank(self, old_bank, new_bank):
        old_bank.delete_client(self)
        new_bank.add_client(self)
        return '{} {} switch from {} to {} bank '.format(self.name, self.lastname, old_bank.name, new_bank.name)


class Bank:
    banks = []

    def __init__(self, name):
        self.name = name
        self.clients = []
        self.banks.append(self)

    @classmethod
    def number_of_banks(cls):
        return len(cls.banks)

    def add_client(self, client):
        self.clients.append(client)

    def display_client(self):
        client_information = '\n--------- {} clients: ---------\n'.format(self.name)
        for i in self.clients:
            client_information += i.name + ' ' + i.lastname + '\n'
        return client_information

    def delete_client(self, client):
        for i in range(len(self.clients)):
            if self.clients[i].account_number == client.account_number:
                return self.clients.pop(i)
        return 'Client not found'

    def withdrawal(self, money, account_number):
        for x in self.clients:
            if x.account_number == account_number:
                if self.is_withdrawal_possible(x.total_amount_cash, money):
                    x.amount_money = x.total_amount_cash - money
                    return "Success! {} {} withdrew {}$, the total money of the account is now {} $" \
                        .format(x.name, x.lastname, money, x.amount_money)
                else:
                    return "Fail! {} {}, no withdrawal possible due to the total amount of money in your account" \
                        .format(x.name, x.lastname)
        return 'No client found'

    @staticmethod
    def is_withdrawal_possible(total_amount_cash, money):
        if total_amount_cash < money:
            return False
        elif total_amount_cash >= money:
            return True

    @staticmethod
    def money_transfer(sender, amount, bank, receiver):
        for x in bank.clients:
            if x.account_number == receiver.account_number:
                x.amount_money = receiver.total_amount_cash + amount
                sender.amount_money = sender.total_amount_cash - amount
                return 'Transfer finish: {} {} send {}$ to {} {}' \
                    .format(sender.name, sender.lastname, amount, receiver.name, receiver.lastname)
        return 'No receiver found'

    def deposit_money(self, client, money_added):
        for x in self.clients:
            if x.account_number == client.account_number:
                x.amount_money = x.total_amount_cash + money_added
                return '{} {} added {} $ to account'.format(x.name, x.lastname, money_added)


if __name__ == '__main__':

    client1 = Client('Maria', 'Graus', 2000)
    client2 = Client('Andre', 'Grs', 1500)
    client3 = Client('Camille', 'Rami', 1700)
    client4 = Client('John', 'Doe', 900)
    client5 = Client('Sophie', 'Deme', 350)
    client6 = Client('Dan', 'Kest', 3000)
    client7 = Client('Zenia', 'Sag', 2040)
    client8 = Client('Coralie', 'Cortez', 1043)
    client9 = Client('Tom', 'Poitier', 999)
    client10 = Client('Ken', 'Mag', 3002)
    client11 = Client('Theo', 'Louv', 700)
    client12 = Client('Luka', 'Ivano', 1860)

    bank1 = Bank('Société Générale')
    bank2 = Bank('BNP')
    bank3 = Bank('CIC')

    bank1.add_client(client1)
    bank1.add_client(client8)
    bank1.add_client(client12)
    bank1.add_client(client4)

    bank2.add_client(client2)
    bank2.add_client(client5)
    bank2.add_client(client10)
    bank2.add_client(client6)

    bank3.add_client(client3)
    bank3.add_client(client7)
    bank3.add_client(client9)
    bank3.add_client(client11)

    print(bank1.display_client())

    print(bank2.display_client())

    print(bank3.display_client())

    print('\n------------------------\n Withdrawal:\n------------------------')
    print(bank1.withdrawal(250, bank1.clients[0].account_number))
    print(bank1.withdrawal(175, bank1.clients[0].account_number))
    print(bank2.withdrawal(450, bank2.clients[1].account_number))
    print(bank2.withdrawal(500, bank2.clients[2].account_number))
    print(bank3.withdrawal(20, bank3.clients[2].account_number))

    print('\n------------------------\n Transfer money:\n------------------------')
    print(bank2.money_transfer(client6, 300, bank1, client4))
    print(bank3.money_transfer(client3, 100, bank2, client2))
    print(bank1.money_transfer(client1, 250, bank3, client11))
    print(bank2.money_transfer(client10, 400, bank1, client12))
    print(bank1.money_transfer(client8, 40, bank2, client2))
    print(bank3.money_transfer(client9, 158, bank3, client7))

    print('\n------------------------\n Deposit money:\n------------------------')
    print(bank2.deposit_money(client5, 400))
    print(bank3.deposit_money(client11, 300))
    print(bank1.deposit_money(client8, 100))
    print(bank1.deposit_money(client12, 500))
    print(bank2.deposit_money(client2, 700))

    print("\n------------------------\n Information about a client:\n------------------------ {}"
          .format(client5.print_information()))

    print("\n------------------------\n Information about a client:\n------------------------ {}"
          .format(client11.print_information()))

    print("\n------------------------\n Information about a client:\n------------------------ {}"
          .format(client1.print_information()))

    print("\n------------------------\n Information about a client:\n------------------------ {}"
          .format(client12.print_information()))

    print('\n------------------------\n Change bank:\n------------------------')
    print(client7.change_bank(bank3, bank2))
    print(client5.change_bank(bank2, bank3))
    print(client8.change_bank(bank1, bank2))
