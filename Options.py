class options:
    inventory = []
    endings = []


    def endgame(choice):
        if choice == "porch":
            print("Guess the paper sent out the wrong person for the story, huh?")
            print("GAME OVER: Ending 1")
            options.endings.append("Ending 1: Coward")

    def porch():
        choice = input("Do you dare to enter the house? Y/N: ")

        if choice.lower() == 'y':
            print("You grip the doorknob again and with a shaky breath, open the door...")
            options.entryway()
        elif choice.lower() == 'n':
            print("You turn around and head back to your car, head lowered in shame.")
            options.endgame("porch")
        else:
            print("Sorry that is not a valid option. Please try again.")
            options.porch()

    def entryway():
        print("A dimly lit entryway greets you, sunlight managing to make it in through\n")
        print("the caked-on grime on the large stained glass windows above the front door.\n")
        print("There's an expensive-looking rug running along the floor and a surprising lack\n")
        print("of vandalism, despite the door not being locked. There is a small table on one side\n")
        print("and a painting on the other. There is also one door leading further into the house.\n")
        print("As far as you can tell, there are three options:\n")
        
        print("A. Investigate the table.\n")
        print("B. Investigate the painting.\n")
        print("C. Go through the door.\n")
        choice = input("What would you like to do?: ")

        if choice.lower() == "a":
            print("You investigate the table and notice it has only one drawer. You open it.\n")
            print("Inside, you find a single key with a decorative ellipses on it. You pocket it.\n")
            options.inventory.append("Attic Key")
            
        elif choice.lower() == "b":
            print("You investigate the painting. It is a self-portait of a very stern-looking man with\n")
            print("a large handlebar mustache and piercing brown eyes. There is otherwise nothing interesting\n")
            print("about it.\n")

        print("You go through the door and make your way further inside...\n\n")
        options.foyer()
            


    
    def foyer():
        print("On the other side of the door lies a dimly lit foyer, stairs go up on the right, to the left there is a\n")
        print("swinging door, to the right just before the stairs there is another door, and forward there is a dark hallway.\n")
        print("Which area would you like to explore?")
        print("A. Go through the left door")
        print("B. Go forward into the hallway")
        print("C. Go through the right door")
        print("D. Go up the stairs")
        print("E. Go back through the door.")
        choice = input()


        if choice.lower() == "a":
            print("You have chosen to go through the left door. It creaks open...")
            options.left_door()
        elif choice.lower() == "b":
            print("You have chosen to go forward into the hallway. You step forward...")
            options.hallway()
        elif choice.lower() == "c":
            print("You have chosen to go through the right door. You turn the knob...")
            options.right_door()
        elif choice.lower() == "d":
            print("You have chosen to go up the stairs. You grip the banister and take the first step...")
            options.stairs()
        elif choice.lower() == "e":
            print("You turn around.")
            options.entryway()
        else:
            print("Sorry, that is not a valid choice.")
            options.foyer()


    def left_door():
        print("The left door leads to a living room. Dust coats the antique furniture and the faint smell of old books hangs in the air.\n")
        print("There are several things about this room that intrigue you.")

    def right_door():
        pass
    
    def hallway():
        pass

    def stairs():
        pass
    


    
        