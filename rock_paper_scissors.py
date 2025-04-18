import random 

rock     = '✊'
paper    = '✋'
scissors = '✌️'
lizard   = '🦎'
spock    = '🖖'

choices = { 
    1: 'rock ✊',
    2: 'paper ✋',
    3: 'scissors ✌️',
    4: 'lizard 🦎',
    5: 'spock 🖖'

}

#Scissors beats Paper and Paper beats Rock and Rock beats Scissors.
#Lizard beats Spock and Spock beats Scissors and Scissors beats Lizard.
#Rock beats Lizard and Lizard beats Paper and Paper beats Spock and Spock beats Rock

winning_combos = {
    (1, 3),  # Rock beats Scissors
    (1, 4),  # Rock beats Lizard
    (2, 1),  # Paper beats Rock
    (2, 5),  # Paper beats Spock
    (3, 2),  # Scissors beats Paper
    (3, 4),  # Scissors beats Lizard
    (4, 2),  # Lizard beats Paper
    (4, 5),  # Lizard beats Spock
    (5, 1),  # Spock beats Rock
    (5, 3)   # Spock beats Scissors
}

print ('=' * 32)
print ('Rock Paper Scissors Lizard Spock')
print ('=' * 32)
print ('1) ✊ (Rock)'  )
print ('2) ✋ (Paper)'  )
print ('3) ✌️ (Scissors)' )
print ('4) 🦎 (Lizard)' )
print ('5) 🖖 (Spock)' )

player = int(input('Pick a number(1-5): '))
if player == 1:
 print ('You Chose: ' + rock)
elif player == 2:
   print ('You Chose: ' + paper)
elif player == 3:
   print ('You Chose: ' + scissors)
elif player == 4:
   print ('You Chose: ' + lizard)
elif player == 5:
   print ('You Chose: ' + spock)
else:
   print ('Invalid Pick Again!')

computer = random.randint(1, 5)
if computer == 1:
 print ('Computer Chose: ' + rock)
elif computer == 2:
   print ('Computer Chose: ' + paper)
elif computer == 3:
   print ('Computer Chose: ' + scissors)
elif computer == 4:
   print ('Computer Chose: ' + lizard)
else:
   print ('Computer Chose: ' + spock)


    
