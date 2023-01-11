name = input("What is your name? ")
print("Wellcome", name, "to this adventure ")

answer = input("You are on the road, it has come to an end and you can go left or right, which way would like to go? ").lower()

if answer == 'left':
    answer = input("You have come to a lake. You can walk around or swim across, what do you choose? ").lower()
    if answer == 'swim across' :
        print("You swim across and were eaten by crocodile.")
    elif answer == 'walk around':
        print("You survived, there is a bar on the other side of the lake!")
   
        if answer == "right":
            print("You got hit by a truck and died")
else:
    print("Not a valid option. You died. ")
