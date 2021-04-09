
class Client:
  def __init__(self, name, lastname, age,account_number,bank_name, total_amount_cash):
    self.name = name
    self.lastname = lastname
    self.age = age
    self.account_number = account_number
    self.bank_name = bank_name
    self.total_amount_cash = total_amount_cash
  
  def print_information (self):
    print("\nName :", self.name ,"\nLastname : ", self.lastname, "\nAge : ", self.age, "\nAccount number : ", self.account_number, "\nBank name : ", self.bank_name, "\nTotal amount : ", self.total_amount_cash, "$")

class Bank:

  def __init__(self, name):
    self.name = name



client1 = Client('Maria','Graus','22',1234, 'SG', 3000)
client2 = Client('Andre','Graus','21',1354, 'SG', 3500)

client1.print_information()
client2.print_information()