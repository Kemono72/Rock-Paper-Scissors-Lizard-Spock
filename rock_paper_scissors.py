import random 

print ('================================')
print ('Rock Paper Scissors Lizard Spock')
print ('================================')
print ('1) ✊ (Rock)'  )
print ('2) ✋ (Paper)'  )
print ('3) ✌️ (Scissors)' )
print ('4) 🦎 (Lizard)' )
print ('5) 🖖 (Spock)' )

player = int(input('Pick a number(1-5): '))
computer = random.randint(1, 5)

# rock beats scissors loses to paper
# scissors beat paper loses to rock
# paper beats rock loses to scissors 
# rock > scissor > paper > rock 
#
if player == 3 and computer == 2:
    print()

