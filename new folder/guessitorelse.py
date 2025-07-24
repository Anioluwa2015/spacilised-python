import random
num = random.randint(1,100)

def intro():
    global name
    name=input("enter the name")
    print(name, "Let's play the number from 1 to 100!")

    if num %2==0:
        x='even'
    else:
        x='odd'
    print("The number is ", x)
    print("go ahead please guess the number")
def pick():
	guessesTaken = 0

	#if the number of guesses is less than 6
	while guessesTaken < 6:
		#inserts the place to enter guess
		enter=input("Guess: ") 

		#check if a number was entered
		try: 

			#stores the guess as an integer instead of a string 
			guess = int(enter)    

			if guess<=100 and guess>=1: #if they are in range
				guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong
				if guessesTaken<6:
					if guess<num:
						print("The guess of the number that you have entered is too low")
					if guess>num:
						print("The guess of the number that you have entered is too high")
					if guess != num:

						print("Try Again!")
				
				#if the guess is right, then we are going to jump out of the while block
					if guess==num:
						break 

			
			if guess>100 or guess<1: 
				print("Silly Goose! That number isn't in the range!")

				print("Please enter a number between 1 and 100")

		except: #if a number wasn't entered
			print("I don't think that "+enter+" is a number. Sorry")
			
	if guess == num:
		guessesTaken = str(guessesTaken)
		print('Good job, {}! You guessed my number in {} guesses!'.format(name, guessesTaken))

	if guess != num:
		print('Nope. The number I was thinking of was ' + str(num))

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	pick()
	print("Do you want to play again?")
	playagain=input()




