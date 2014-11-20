# Rock-paper-scissors-lizard-Spock
import random

def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    
    
def rpsls(player_choice): 
    print('')
    print "Player chooses "+player_choice
    num = name_to_number(player_choice)
    comp = random.randrange(0, 5)
    print "Computer chooses "+number_to_name(comp)
    diff = (comp - num)%5
    
    if diff <= 2 and diff > 0:
        print "Computer wins!"
    elif diff >=3 and diff <=4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




