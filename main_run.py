import deck
import player_bet


def game():
	deck1=deck.Deck()
	player_bets=player_bet.Player_Bet(int(input("Kindly provide the total chips you will be playing with: ")))
	bet=player_bets.bet()
	player1=[]
	player1.append(deck1.deck.pop())
	player1.append(deck1.deck.pop())
	dealer=[]
	dealer.append(deck1.deck.pop())
	dealer.append(deck1.deck.pop())
	print("Cards of player1:")
	for card in player1:
		print(card)
	print("Cards of dealer:\n X")
	for card in range(1,len(dealer)):
		print(dealer[card])

	#show_cards(player1,dealer)
	hit='Y'
	sum_player=player1[0].value+player1[1].value
	sum_dealer=dealer[0].value+dealer[1].value

	while hit == 'Y' or hit == 'y' and sum_player<21:
		hit = input("Player1, would you like to hit? y/n")
		if hit=='y' or hit=='Y':
			popped_card=deck1.deck.pop()
			player1.append(popped_card)
			sum_player+=popped_card.value
			deck1.show_cards(player1,dealer)

	if sum_player>21:
		print("Player1 busts! Dealer wins!!")
	else:
		deck1.show_cards(player1,dealer)

		while sum_dealer<sum_player and sum_dealer<21:
			popped_card=deck1.deck.pop()
			dealer.append(popped_card)
			sum_dealer+=popped_card.value
			deck1.show_cards(player1,dealer)
			print("Sum of the dealer: {}".format(sum_dealer))


		if sum_player<sum_dealer and sum_dealer<21:
			player_bets.chips-=bet

			print("Player1 lost!! Total chips: {}".format(player_bets.chips))

		elif sum_player==sum_dealer and sum_player<21:
			print("BlackJack! Its a tie!!")
			player_bets.chips+=bet*2
			print("Player1 Total chips: {}".format(player_bets.chips))
		else:

			player_bets.chips+=bet*2
			print("Player1 won!! Total chips: {}".format(player_bets.chips))
