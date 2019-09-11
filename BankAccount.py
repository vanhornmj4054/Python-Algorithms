class User:
	def __init__(self, username, email_address, account_number):
		self.name = username
		self.email = email_address
		self.account_number = BankAccount(number)
		self.account = BankAccount(int_rate=0.02, balance=0)
	def make_deposit(self, amount, number):
		self.account.deposit(self, amount, number)
		return self
	def make_withdrawal(self, amount):
		self.account.withdraw(self, amount)
		return self
	def display_user_balance(self):
		print("User: " + self.name + ", Balance: $" + str(self.account.display_account_info(self)))
		return self
	def transfer_money(self, other_user, amount):
		self.account_balance -= amount
		other_user.account_balance += amount
		return self

class BankAccount:
	def __init__(self,int_rate=0.00, balance=0.0):
		self.rate = int_rate
		self.account_balance = balance
	def deposit(self, amount):
		self.account_balance += amount
		return self
	def withdraw(self, amount):
		self.account_balance -= amount
		return self
	def display_account_info(self):
		print("Balance: $" + str(self.account_balance))
		return self
	def yield_interest(self):
		if self.account_balance > 0:
			self.account_balance += self.account_balance * self.rate
		else:
			print("Negative Balance")
		return self

guido = BankAccount(int_rate=.12, balance=100)
monty = BankAccount(int_rate=.10, balance=400)

guido.deposit(100).deposit(200).deposit(50).withdraw(60).yield_interest().display_account_info()
monty.deposit(200).deposit(150).withdraw(60).withdraw(60).withdraw(20).withdraw(20).yield_interest().display_account_info()


