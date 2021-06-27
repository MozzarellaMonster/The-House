from Items import items

class options:

    inventory = []
    endings = []

    #Decide if you want to make it optional to pick up inventory items.
    def endgame(choice):
        if choice == "porch":
            print("Guess the paper sent out the wrong person for the story, huh?")
            print("GAME OVER: Ending 1: Coward")
            options.endings.append("Ending 1: Coward")



    def porch():
        choice = input("Do you dare to enter the house? Y/N: ")

        if choice.lower() == 'y':
            print("\nYou grip the doorknob again and with a shaky breath, open the door...")
            options.entryway()
        elif choice.lower() == 'n':
            print("\nYou turn around and head back to your car, head lowered in")
            print("shame.")
            options.endgame("porch")
        else:
            options.try_again()
            options.porch()



    def entryway():
        print("A dimly lit entryway greets you, sunlight managing to make it in through")
        print("the caked-on grime on the large stained glass windows above the front door.")
        print("There's an expensive-looking rug running along the floor and a surprising lack")
        print("of vandalism, despite the door not being locked. There is a small table on one side")
        print("and a painting on the other. There is also one door leading further into the house.")
        options.entryway_2()
    


    def entryway_2():
        print("As far as you can tell, there are three options:\n")
        print("A. Investigate the table.")
        print("B. Investigate the painting.")
        print("C. Go through the door.")
        choice = input("\nWhat would you like to do?: ")        
        
        if choice.lower() == "a":
            print("You investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it. You pocket it.")
            options.inventory.append("Attic Key")
            print("You turn back to the room.")
            options.entryway_3("a")
            
        elif choice.lower() == "b":
            print("You investigate the painting. It is a self-portait of a very stern-looking man with")
            print("a large handlebar mustache and piercing brown eyes. There is otherwise nothing interesting")
            print("about it.")
            print("You turn back to the room.")
            options.entryway_3("b")

        elif choice.lower() == "c":
            print("You go through the door and make your way further inside...\n")
            options.foyer()
        
        else:
            options.try_again()
            options.entryway_2()
    


    def entryway_3(used = None):
        done = False
        print("You turn back to the room.")
        if used == "a":
            print("There are now two options left, you can either look at the painting or")
            print("you can go through the door, which would you like to do?")
            print("1. Look at the painting")
            print("2. Go through the door")
            choice_2 = input()
        elif used == "b":
            print("There are now two options left, you can either investigate the table or")
            print("you can go through the door, which would you like to do?")
            print("A. Investigate the table")
            print("B. Go through the door")
            choice_2 = input()
            
        if choice_2 == "1":
            print("You investigate the painting. It is a self-portait of a very stern-looking man with")
            print("a large handlebar mustache and piercing brown eyes. There is otherwise nothing interesting")
            print("about it.")
            done = True
        elif choice_2.lower() == "a":
            print("You investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it. You pocket it.")
            options.inventory.append("Attic Key")
            done = True

        if choice_2 == "2" or choice_2.lower() == "b" or done:
            print("You go through the door and make your way further inside...\n")
            options.foyer()
        else:
            options.try_again()
            options.entryway_3(used)



    def foyer():
        print("In front of you lies a dimly lit foyer, stairs go up on the right, to the left there is a")
        print("swinging door, to the right just before the stairs there is another door, and forward there is a dark hallway.")
        print("\nWhich area would you like to explore?")
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
            print("You try to go back through the door, but it is locked. You turn back around")
            options.foyer()
        else:
            options.try_again()
            options.foyer()


    def left_door():
        print("The left door leads to a living room. Dust coats the antique furniture and the faint smell of old books hangs in the air.")
        print("There are several things about this room that intrigue you.")
        print("One of them is the large bookshelf directly across from you filled with dusty old books.")
        print("Another is the large, intricately decorated fireplace against the wall.")
        print("The last thing of note is the display case underneath the window.")
        print("\nWhich would you like to investigate?")
        print("A. The bookshelf")
        print("B. The fireplace")
        print("C. The display case")
        print("D. Leave the room")
        choice = input()

        if choice.lower() == "a":
            print("You go to the bookshelf and look over the old tomes on the shelf.")
            print("Aside from noticing the majority of them were mystery and thrillers, nothing really stands out about them.")
            print("You turn back to the room.")
            
            
        elif choice.lower() == "b":
            print("You go up to the fireplace and admire the intricate carvings of grapevines on it.")
            print("There seems to be one cluster of grapes that stands out from the rest.")
            print("Specifically, one particular grape. You graze your hand over it and notice that it gently")
            print("gives under the pressure of your finger. It's a button! Push it?")
            push = input("Will you push the button, Y/N?: ")


        elif choice.lower() == "c":
            print("You walk up to the display case and brush away the dust collected on the glass lid.")
            print("It's empty. Figures, maybe some looters took whatever valuable thing may have been inside?")
            print("You look closer and notice the faint impression of a dagger in the velvet cushion of the case.")
            print("Interesting, maybe whoever lived here before liked collecting antiques?")
            print("You turn back to the room.")
        
        else:
            options.try_again()
            options.left_door()


    def right_door():
        print("The right door leads into a small home office. Strangely, the desk lamp is on despite the fact that the house does not have ")
        print("power connected to it. A large globe stand sits next to the desk supported by three legs. It looks like the kind to have a hidden compartment within.")
        choice = input("You could either check out the desk or the globe, which do you choose?\n A: The desk\n B: The globe stand")
        
        if choice.lower() == "a":
            print("The desk itself has several drawers, two of which are empty. The main drawer only has a single pen inside it and the bottom left drawer ")
            print("has a locked box with the emblem of a crane on it.")
            print("What do you want to do?")


        elif choice.lower() == "b":
            print("You were right when you guessed the globe had a hidden compartment within it.")
            print("You opened it up to find a contraption made of several gears tucked tightly inside.")
            print("There appears to be a gear missing. Nothing will move without that gear.")
        
        else:
            options.try_again()
            options.right_door()


    def hallway():
        print("You head down the old dusty hallway and find the entrances to two rooms. One is obviously the kitchen,")
        print("the other appears to be the basement. What would you like to do?")
        print("A. Go into the kitchen")
        print("B. Head down into the basement")
        print("C. Go back into the foyer")
        choice = input()

        if choice.lower() == "a":
            print("You head into the kitchen.")
            options.kitchen()

        elif choice.lower() == "b":
            print("You take the first step down into the basement.")

        elif choice.lower() == "c":
            print("You turn around and head back into the foyer.")

        else:
            options.try_again()
            options.hallway()            


    def kitchen():
        print("It is drab, with the cabinets painted a faded yellow with white tile counters.")
        print("The oven stood open like a gaping maw, the door having fallen off the hinges.")
        print("The refrigerator stood about two feet away from the wall, appearing to have been pulled away from it.")
        print("The floor is a checkered black and white and the small table has been destroyed, it looks like it was hit by a massive impact.")
        print("At first, nothing really stands out to you, but then you notice something glinting inside a broken cabinet with no door.")
        print("There is also the matter of opening the refrigerator, whose door is still intact and closed.")
        print("\nWhat would you like to do?")
        print("A. Investigate the glinting object")
        print("B. Open the refrigerator door")
        print("C. Go back into the hallway")
        choice = input("\n")

        if choice.lower() == "a":
            print("You bend down and look deeper into the broken cabinet.")
            print("It is a silver, decorative dagger.")
            #print("You pick it up.")
            options.kitchen_cabinet()
        elif choice.lower() == "b":
            print("You open the refrigerator door. It's full of mold. Mold is growing around the entirety of the space inside.")
            print("An awful smell hits you and close the door immediately. Don't know what else you expected, honestly.")
            options.kitchen()
        elif choice.lower() == "c":
            print("You turn around and go back into the hallway.")
            options.hallway()
        else:
            options.try_again()
            options.kitchen()
            
                
    def kitchen_cabinet():
        pick_up = input("\nDo you want to pick it up? Y/N: ")
        if pick_up.lower() == "y":
            options.inventory.append(items.silver_dagger)
            return
        elif pick_up.lower() == "n":
            print("You decide to leave the dagger alone and get back up.")
            return
        else:
            options.try_again()
            options.kitchen_cabinet()


    #Finish basement
    def basement():
        if items.flashlight in options.inventory:
            print("Now that you have a light source, you can definitely see better in the dark basement.")
            print("You shine the light around, illuminating the dark, dusty corners of the creepy basement.")
            print("You come to rest the beam on one particuler outcropping of battered concrete on the floor of the basement.")
        else:
            print("The stairs creak as you make your way down into the basement, the aged wood threatening to give out from under you.")
            print("As you reach the bottom of the stairs, complete darkness welcomes you. A faint pitter-patter of water can be heard from somewhere in the basement.")
            print("You reach out blindly, hoping to find a light switch or a pull cord. Finding none, you make your way back up the stairs.")


    def stairs(direction):
        if direction == "up":
            print("You head up the stairs, your hand gliding along the surprisingly smooth polished surface of the banister.")
            print("The old wooden steps creak as you make your way up.")
            print("You notice the pale, unfaded patches of wall where pictures used to hang.")
            print("You reach the top of the stairs.")
            options.upper_hallway()
        else:
            print("You head down the stairs.")
            options.foyer()


    def upper_hallway():
        print("You look around the upstairs hallway and immediately notice three doors.")
        print("One seems to lead to an upstairs bathroom, another leads to a bedroom, and yet another appears to lead to the attic.")
        print("\nWhich room would you like to explore?")
        print("A. Bathroom")
        print("B. Bedroom")
        print("C. Attic")
        print("D. Leave the hallway")
        choice = input("\n")
        
        if choice.lower() == "a":
            options.bathroom()
        
        elif choice.lower() == "b":
            options.bedroom()

        elif choice.lower() == "c":
            options.attic()
            
        elif choice.lower() == "d":
            options.stairs("down")
        else:
            options.try_again()
            options.upper_hallway()
    

    def bathroom():
        print("You choose to explore the bathroom.")
        print("You go inside the bathroom and immediately notice the dirty and stained mirror, cracked with age.")
        print("There is also a broken down toilet and the shower with a missing showerhead.")
        print("The cabinet doors are missing and there is no compartment behind the mirror.")
        print("Seeing nothing of interest in the bathroom, you leave.")
        options.upper_hallway()
    

    def bedroom():
        print("You choose to explore the bedroom.")
        print("You make your way into the bedroom and admire the stunning mahogany four-poster bed the takes up the majority of the space.")
        print("There is also a wardrobe, dresser, and a trunk at the end of the bed.")
        print("Seeing no other furniture, you decide either the dresser, trunk, or wardrobe might be worth investigating.")
        print("\nWhich would you like to choose?")
        print("A. Dresser")
        print("B. Trunk")
        print("C. Wardrobe")
        print("D. Leave the bedroom")
        choice = input("\n")

        if choice.lower() == "a":
            print("You go up to the dresser and open the drawers one by one. You don't really find much, except for some mothballs.")
            print("You leave the dresser, closing all the drawers first.")
            options.bedroom()
        
        elif choice.lower() == "b":
            print("You crouch in front of the trunk and slowly open it. Inside, you find a single flashlight.")
            print("You flick the switch and find that it still works, despite its obvious age.")
            options.inventory.append(items.flashlight)
            print("You decide to take it with you.")
            options.bedroom()
        
        elif choice.lower() == "c":
            print("You walk up to the wardrobe and slowly open it.")
            print("Inside, you find an old jacket. Perhaps it belonged to whoever used to live here?")
            print("You attempt to move the jacket, but immediately falls apart. It's clear you can't move it.")
            print("You close the wardrobe and turn back to the room.")
            options.bedroom()
        
        elif choice.lower() == "d":
            options.upper_hallway()

    
    def attic():
        print("You head up the short staircase and poke your head into the dark gloom of the attic.")
        print("Surprisingly, the attic is quite empty save for an old safe that leaning against one wall of the dusty room.")
        print("Seeing no other option, you head up to the old safe.")
        if items.attic_key in options.inventory:
            print("You notice that unique ellipse shape on the door of the safe from that key you picked up earlier in the foyer.")
            print("Curious, you bring the key out from your pocket and try it in the keyhole of the safe.")
            print("It works.")
            print("You slowly twist the key and hear a satisfying click.")
            print("You creak open the old safe's door. Inside, you find a dusty old gear.")
            print("You add it to your backpack.")
            options.inventory.append(items.old_gear)
            print("You close the old safe and head out of the attic.")
            options.upper_hallway()
        else:
            print("You notice that there's a unique ellipse shape on the door.")
            print("It seems somewhat familiar...")
            print("Unfortunately, you cannot do any more with the safe at this time.")
            print("You make your way back down the short staircase.")
            options.attic()


    def try_again():
        print("Sorry, that is not a valid option. Please try again.\n")