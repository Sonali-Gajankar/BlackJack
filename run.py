import main_run

def run_game():
	main_run.game()

	play_again='y'
	while play_again=='y' or play_again=='Y':
		play_again=input("Would you like to play again? ")
		if play_again=='y' or play_again=='Y':
			main_run.game()
		else:
			print("Thank You!!")
run_game()