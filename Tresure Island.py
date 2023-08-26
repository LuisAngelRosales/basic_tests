print("Welcome you are about to start an exciting adventure. "
      "\nYou are looking for a treasure which is hidden on an island.")
print("\nWith no mercy, at the beggining there is an archipielago "
      "and you are being pursued by monkeys, you need to choose quickly.")
flag=1
while flag==1:
    first_stage=input("\nSwim to the next island or try to make a boat? (type swim or boat): ")
    first_stage=first_stage.lower()

    if first_stage == "swim":
        print("\nGreat, you swam successfully through and arrived on the island.")
        flag=0
    elif first_stage=="boat":
        print("\nToo bad, you were hit by the monkeys and lose the game.")
        exit()
    else:
        print("\nThat's not a valid option, type swim or boat")
flag=1

print("\nIn front on you there is a maze but you also have "
      "the opportunity of walk around to avoid it.")
second_stage=input("What you would do?\n"
                   "Walk around (type walk) or try solving the maze (type maze): ")
second_stage=second_stage.lower()

while flag==1:
    if second_stage =="walk":
        print("\nPerfect, you took the easier way and avoided "
              "the maze. You passed yo the final section.")
        flag=0
    elif second_stage=="maze":
        print("\nGood heavens! There was no exit for the maze and you got out of your mind. Game over")
        exit()
    else:
        print("\nThat's not a valid option, type walk or maze")
flag=1
print("\nFinally, on the last stage, you need to make a decision, there are three doors, a yellow,"
      " blue and a red one. So basically to get the treasure you need to open the correct door.")

third_stage=input("\nWhat would you choose? (type red, blue or yellow): ")
third_stage=third_stage.lower()
while flag==1:
    if third_stage =="red":
        print("\nWait what? There is a lion waiting for you next the door, you ran away an lose the game.")
        exit()
    elif(third_stage =="blue"):
        print("\nGreat, you got the treasure. Good game!")
        flag=0
    elif(third_stage=='yellow'):
        print('\nBad choice, there is just a goat staring at you on the other side of the door.')
        exit()
    else:
        print("\nThat's not a valid option, type red, blue or yellow")

