import random

names = { 'R':'Rock', 'P': 'paper', 'S':'scissors'}
done = False

wins,losses,ties = 0,0,0

while not done:
    user_choice = input("Enter your choice ( R , P , S) - Q to Quit ").upper()
    computer_choice = random.choice(['R', 'P', 'S'])

    if user_choice == computer_choice:
        print(f"it's a tie, you both chose {names[computer_choice]}")
        ties += 1


    elif user_choice == 'R':
        if computer_choice == 'P':
            print(f"Computer wins, you chose {names[user_choice]}, computer choose {names[computer_choice]}")
            losses += 1
        else:
            print(f"You win, you chose {names[user_choice]}, computer choose {names[computer_choice]}")
            wins += 1


    elif user_choice == 'P':
        if computer_choice == 'S':
            print(f"Computer wins, you chose {names[user_choice]}, computer choose {names[computer_choice]}")
            losses += 1
        else:
            print(f"You win, you chose {names[user_choice]}, computer choose {names[computer_choice]}")
            wins += 1
    elif user_choice == 'S':
        if computer_choice == 'R':
            print(f"Computer win, you chose {names[user_choice]}, computer choose {names[computer_choice]}")
            losses += 1
        else:
            print(f"You win, you chose {names[user_choice]}, computer choose {names[computer_choice]}")
            wins += 1

    elif user_choice == 'Q':
        done = True
    else:
        print("Invalid choice")




print(f"Wins: {wins} \nLosses: {losses}  \nTies: {ties}  ")