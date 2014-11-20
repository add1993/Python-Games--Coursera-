# template for "Guess the number" mini-project
import simplegui
import random
import math

guess1 = 7;
range1 = 100;
secret_number = 0;
def new_game():  
    print ""
    global secret_number, guess1;
    if range1 == 100:
        guess1 = 7;
    else:
        guess1 = 10;
    secret_number = random.randrange(0, range1);
    print "New game. Range is from 0 to", range1
    print "Number of remaining guesses is", guess1
    
# define event handlers for control panel
def range100():
    global guess1;
    guess1 = 7;
    global range1;
    range1 = 100;
    new_game();
    
    # button that changes the range to [0,100) and starts a new game 

def range1000():
    global guess1;
    guess1 = 10;
    global range1;
    range1 = 1000;
    new_game();
    # button that changes the range to [0,1000) and starts a new game     
       
def input_guess(guess):
    global guess1;
    global secret_number
    guess = int(guess);
    guess1 -= 1;
    print ""
    print "Guess was ",guess
    print "Number of remaining guesses ", guess1
        
    if guess == secret_number:
        print "Correct!"
        new_game();        
    elif guess1== 0:
        print "You ran out of guesses. The number was ", secret_number
        new_game()
    elif guess < secret_number:
        print "Higher!"
    else:
        print "Lower!"
    
# create frame
frame = simplegui.create_frame("Number Game", 200, 200);
frame.add_button("Range is [0-100)", range100, 200);
frame.add_button("Range is [0-1000)", range1000, 200);
frame.add_input("Enter a guess", input_guess, 200);
# register event handlers for control elements and start frame

# call new_game 
new_game()
