class User:
	def __init__(self, username, email_address):
		self.name = username
		self.email = email_address
		self.account_balance = 0
	def make_deposit(self, amount):
		self.account_balance += amount
		return self
	def make_withdrawal(self, amount):
		self.account_balance -= amount
		return self
	def display_user_balance(self):
		print("User: " + self.name + ", Balance: $" + str(self.account_balance))
		return self
	def transfer_money(self, other_user, amount):
		self.account_balance -= amount
		other_user.account_balance += amount
		return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
mike = User("Mike Van Horn", "hotmail.com")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(10).display_user_balance()
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(50)
# guido.make_withdrawal(10)
# guido.display_user_balance()

monty.make_deposit(50).make_deposit(500).make_withdrawal(40).make_withdrawal(40).display_user_balance()
# monty.make_deposit(500)
# monty.make_withdrawal(40)
# monty.make_withdrawal(40)
# monty.display_user_balance()

mike.make_deposit(100).make_withdrawal(60).make_withdrawal(40).make_withdrawal(20).display_user_balance()
# mike.make_withdrawal(60)
# mike.make_withdrawal(40)
# mike.make_withdrawal(20)
# mike.display_user_balance()

guido.transfer_money(mike, 20).display_user_balance()
# guido.display_user_balance()
mike.display_user_balance()


