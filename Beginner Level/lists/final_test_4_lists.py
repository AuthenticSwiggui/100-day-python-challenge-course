import random

user = int(input('''
    Select your hand: 
        0 = rock
        1 = paper
        2 = scissors
'''))

#Playable hands
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''

paper = '''
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

hands = [rock, paper, scissors]



computer_choice = random.randint(0, 2)
    


def play(user, computer):
    results = "Win"
    
    print("="*60)        
    print(hands[user])
    print("="*60)
    print(hands[computer])
    if user == computer:
        results = "Tie"
    if user == 0 and computer == 1:
        results = "Loose"
    elif user == 1 and computer == 2:
        results = "Loose"
    elif user == 2 and computer == 0:
        results = "Loose"
    
    return results
        
print(play(user, computer_choice))
