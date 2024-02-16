
#piedra, papel o tijera
import random

options = ('piedra', 'papel', 'tijera')


max_rounds = 5;
computer_victories = 0
user_victories = 0
rounds = 0
while True:
    user_choice = input('piedra, papel o tijera => ')
    user_choice.lower()
    if not user_choice in options:
      print('not a valid option')
      continue
    
    computer_choice = random.choice(options)
    print('User option =>', user_choice)
    print('Computer option =>', computer_choice)
    if user_choice == computer_choice:
        print('draw')
    elif user_choice == 'piedra':
        if computer_choice == 'papel':
            print('Computer wins')
            computer_victories += 1
        else:
            print('User wins')
            user_victories += 1
    elif user_choice == 'papel':
        if computer_choice == 'tijera':
            print('Computer wins')
            computer_victories += 1
        else:
            print('User wins')
            user_victories += 1
    elif user_choice == 'tijera':
        if computer_choice == 'piedra':
            print('Computer wins')
            computer_victories += 1
        else:
            print('User wins')
            user_victories += 1
            
    if user_victories == 3:
        print('game won by user')
        break
    if computer_victories == 3:
        print('game won by computer')
        break
    
    rounds += 1
