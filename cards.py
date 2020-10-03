value={'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
suits=['Spades','Hearts','Clubs','Diamonds']
card_set=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']

class Card():

	def __init__(self,suits,cards):
		self.cards=cards
		self.suits=suits
		self.value=value[cards]
		
	def __str__(self):
		return '{} of {}'.format(self.cards,self.suits)

	

	
	