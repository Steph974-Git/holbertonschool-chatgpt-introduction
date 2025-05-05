class Checkbook:
	"""
	A simple checkbook management system that tracks account balance 
	and handles deposits and withdrawals.
	"""
	def __init__(self):
		"""
		Initialize a new checkbook with a zero balance.
		"""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Add the specified amount to the account balance.
		
		Parameters:
			amount (float): The amount to deposit (must be positive)
			
		Returns:
			None
		"""
		if amount <= 0:
			print("Error: Deposit amount must be positive.")
			return
			
		self.balance += amount
		print("Deposited ${:.2f}".format(amount))
		print("Current Balance: ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		"""
		Remove the specified amount from the account balance if sufficient funds exist.
		
		Parameters:
			amount (float): The amount to withdraw (must be positive)
			
		Returns:
			None
		"""
		if amount <= 0:
			print("Error: Withdrawal amount must be positive.")
			return
			
		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print("Withdrew ${:.2f}".format(amount))
			print("Current Balance: ${:.2f}".format(self.balance))

	def get_balance(self):
		"""
		Display the current account balance.
		
		Returns:
			None
		"""
		print("Current Balance: ${:.2f}".format(self.balance))

def main():
	"""
	Main function that runs the checkbook application interface.
	Handles user interaction and input validation.
	"""
	cb = Checkbook()
	print("Welcome to your Checkbook!")
	
	while True:
		action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
		
		if action.lower() == 'exit':
			print("Thank you for using the Checkbook application. Goodbye!")
			break
			
		elif action.lower() == 'deposit':
			try:
				amount = float(input("Enter the amount to deposit: $"))
				cb.deposit(amount)
			except ValueError:
				print("Error: Please enter a valid numeric amount.")
				
		elif action.lower() == 'withdraw':
			try:
				amount = float(input("Enter the amount to withdraw: $"))
				cb.withdraw(amount)
			except ValueError:
				print("Error: Please enter a valid numeric amount.")
				
		elif action.lower() == 'balance':
			cb.get_balance()
			
		else:
			print("Invalid command. Please try again.")

if __name__ == "__main__":
	main()
