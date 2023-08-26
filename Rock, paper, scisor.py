import random

selection=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n" ))
if selection >2:
    print("Invalid selection, you lose")
else:
    computer_selection=random.randint(0,2)

    computer_list=["rock","paper","scissor"]

    print("Computer choose "+computer_list[computer_selection])


    if selection == computer_selection:
        print("It's a tie")
    elif selection == 0 and computer_selection== 1:
        print("You lose")
    elif selection == 0 and computer_selection == 2:
        print("You win")
    elif selection==1 and computer_selection==0:
        print ('You win')
    elif selection==1 and computer_selection==2:
        print('You lose')
    elif selection==2 and computer_selection==0:
        print("You lose")
    elif selection==2 and computer_selection==1:
        print("You win")