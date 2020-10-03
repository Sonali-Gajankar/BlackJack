import random
import cards

suits=['Spades','Hearts','Clubs','Diamonds']
card_set=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']


class Deck:
	def __init__(self):
		self.deck=[]
		for x in suits:
			for c in card_set:
				new_card=cards.Card(x,c)
				self.deck.append(new_card)
		random.shuffle(self.deck)



	
	def show_cards(self,player1,dealer):
		print("Cards of player1:")
		for card in player1:
			print(card)
		print("Cards of dealer:\n")
		for card in dealer:
			print(card)
	
