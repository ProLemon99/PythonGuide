# NOTE: TO PLAY THE GAME, SIMPLY RUN python if.py IN THE SHELL.

#---------------------------------------------------

# The while statement

# The while statement allows you to repeatedly execute a block of statements as long as a condition is true. A while statement is an example of what is called a looping statement. A while statement can have an optional else clause.

number = 69
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')

# The True and False are called Boolean types and you can consider them to be equivalent to the value 1 and 0 respectively.