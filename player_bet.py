class Player_Bet():

	def __init__(self,chips):
		self.chips=chips

	def bet(self):
		bet=int(input("Please enter bet amount: "))
		if bet>self.chips:
			while bet>self.chips:
				if self.chips==0:
					print("Total chips are 0. Cannot place any more bets!!")
					return 0
				else:
					bet=int(input("Bet is more than the total chips. Please enter appropriate bet: "))

		return bet

