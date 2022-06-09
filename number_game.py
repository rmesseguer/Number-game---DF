import random



robot_score = 0
player_score = 0


while True:
    num = random.randint(1,10) # this is the random number variable that needs to be guessed

    good_guess = False # sets good guess to False at the begining of the loop

    while not good_guess: # while loop starts with "good_guess" set to False. So "while not good_guess" is True 
        try: # sets exception for data type ValueError handling
            guess = int(input('Guess a number between 1 and 10: '))  # takes "guess" as input from the player  
            
            if guess < 1 or guess > 10: # conditions for error handling and exception
                raise ValueError()

            good_guess = True #good_guess is not False anymore so this while loop breaks here
        except ValueError:
            print("Sorry I didn't understand that. Please try again.")
    
    times = 1

    while times < 3 and guess != num:
        if (guess > num):
            try:
                guess = int(input('Lower. Please guess again: '))
            except ValueError:
                print("Sorry I didn't understand that. Please guess again:")
                    
        else:
            try:
                guess = int(input('Higher. Guess again: '))
            except ValueError:
                print("Sorry I didnt understand that. Please guess again:")

        times = times + 1

        if (times == 3):
            print('Too many tries!')
            
            

    if (guess == num):
        player_score = player_score + 1        
        print('You win!', player_score, 'vs', robot_score, '\,,/(^_^)\,,/')

    else:
        robot_score = robot_score + 1        
        print('You lose! The number was ' + str(num) + '. ',player_score, ' vs ', robot_score, '¯\_(oO)_/¯',sep='')