from Items import items

class options:

    inventory = []
    first_stairs = True
    
    def try_again():
        print("\nSorry, that is not a valid option. Please try again.\n")

    def vault(key = None):
        rod = [0,0,0,0]
        if key == items.old_gear["Item name"]:
            rod[0] = 1
        elif key == items.silver_dagger["Item name"]:
            rod[1] = 1
        elif key == "Wardrobe switch":
            rod[2] = 1
        elif key == "Crane":
            rod[3] = 1
        if rod == [1,1,1,1]:
            return 1
        
            

    def porch():
        choice = input("Do you dare to enter the house? Y/N: ")

        if choice.lower() == 'y':
            print("\nYou grip the doorknob again and with a shaky breath, you open the door...")
            options.entryway()
        elif choice.lower() == 'n':
            print("\nYou turn around and head back to your car, head lowered in shame.")
            print("Guess the paper sent out the wrong person for the story, huh?")
            print("GAME OVER: Ending 1: Coward")
        else:
            options.try_again()
            options.porch()



    def entryway():
        print("\nA dimly lit entryway greets you, sunlight managing to make it in through")
        print("the caked-on grime on the large stained glass windows above the front door.")
        print("There's an expensive-looking rug running along the floor and a surprising lack")
        print("of vandalism, despite the door not being locked. There is a small table on one side")
        print("and a painting on the other. There is also one door leading further into the house.")
        options.entryway_2()

    def entryway_2():
        print("\nAs far as you can tell, there are three options:\n")
        print("A. Investigate the table.")
        print("B. Investigate the painting.")
        print("C. Go through the door.")
        choice = input("\nWhat would you like to do?: ")        
        
        if choice.lower() == "a":
            print("\nYou investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it. You pocket it.")
            options.inventory.append(items.attic_key)
            options.entryway_3("a")
            
        elif choice.lower() == "b":
            print("\nYou investigate the painting. It is a self-portait of a very stern-looking man with")
            print("a large handlebar mustache and piercing blue eyes. There is otherwise nothing interesting")
            print("about it.")
            options.entryway_3("b")

        elif choice.lower() == "c":
            print("\nYou go through the door and make your way further inside...\n")
            options.foyer()
        
        else:
            options.try_again()
            options.entryway_2()

    def entryway_3(used = None):
        done = False
        print("You turn back to the room.")
        if used == "a":
            print("\nThere are now two options left, you can either look at the painting or")
            print("you can go through the door, which would you like to do?")
            print("1. Look at the painting")
            print("2. Go through the door")
            choice_2 = input()
        elif used == "b":
            print("\nThere are now two options left, you can either investigate the table or")
            print("you can go through the door, which would you like to do?")
            print("A. Investigate the table")
            print("B. Go through the door")
            choice_2 = input()
            
        if choice_2 == "1":
            print("\nYou investigate the painting. It is a self-portait of a very stern-looking man with")
            print("a large handlebar mustache and piercing blue eyes. There is otherwise nothing interesting")
            print("about it.\n")
            done = True
        elif choice_2.lower() == "a":
            print("\nYou investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it. You pocket it.\n")
            options.inventory.append("Attic Key")
            done = True

        if choice_2 == "2" or choice_2.lower() == "b" or done:
            print("\nYou go through the door and make your way further inside...\n")
            options.foyer()
        else:
            options.try_again()
            options.entryway_3(used)



    def foyer():
        print("\nIn front of you lies a dimly lit foyer, stairs go up on the right, to the left there is a")
        print("swinging door, to the right just before the stairs there is another door, and forward there is a dark hallway.")
        print("\nWhich area would you like to explore?")
        print("A. Go through the left door")
        print("B. Go forward into the hallway")
        print("C. Go through the right door")
        print("D. Go up the stairs")
        print("E. Go back through the door.")
        choice = input()

        if choice.lower() == "a":
            print("\nYou have chosen to go through the left door. It creaks open...")
            options.left_door()
        elif choice.lower() == "b":
            print("\nYou have chosen to go forward into the hallway. You step forward...")
            options.hallway()
        elif choice.lower() == "c":
            print("\nYou have chosen to go through the right door. You turn the knob...")
            options.right_door()
        elif choice.lower() == "d":
            print("\nYou have chosen to go up the stairs. You grip the banister and take the first step...")
            options.stairs("up")
        elif choice.lower() == "e":
            print("\nYou try to go back through the door, but it is locked. You turn back around")
            options.foyer()
        else:
            options.try_again()
            options.foyer()



    def left_door():
        print("\nThe left door leads to a living room. Dust coats the antique furniture and the faint smell of old books hangs in the air.")
        print("There are several things about this room that intrigue you.")
        print("One of them is the large bookshelf directly across from you filled with dusty old books.")
        print("Another is the large, intricately decorated fireplace against the wall.")
        print("The last thing of note is the display case underneath the window.")
        options.left_door_2()

    def left_door_2():
        print("\nWhich would you like to investigate?")
        print("A. The bookshelf")
        print("B. The fireplace")
        print("C. The display case")
        print("D. Leave the room")
        choice = input()

        if choice.lower() == "a":
            print("\nYou go to the bookshelf and look over the old tomes on the shelf.")
            print("Aside from noticing the majority of them were mystery and thrillers, nothing really stands out about them.")
            print("You turn back to the room.")
            options.left_door_2()
            
        elif choice.lower() == "b":
            print("\nYou go up to the fireplace and admire the intricate carvings of grapevines on it.")
            print("There seems to be one cluster of grapes that stands out from the rest.")
            print("Specifically, one particular grape. You graze your hand over it and notice that it gently")
            print("gives under the pressure of your finger. It's a button! Push it?")
            push = input("\nWill you push the button, Y/N?: ")

            if push.lower() == "y":
                print("\nYou push the button. Suddenly, a cast iron claws grabs your hand, its grip like a vice.")
                print("You struggle, helplessly trying to pry the claw off your nearly broken hand.")
                print("You then feel a pulling sensation. And you realize the claw is dragging you into the fireplace.")
                print("You pull even harder and try your hardest to relieve yourself of the iron claw.")
                print("You fail and soon hear the gas being pumped in.")
                print("You only have a moment to realize what's happening before the world around you is engulfed in flames.")
                print("No one can hear your screams over the roar of the fire.")
                print("\nGAME OVER: Ending 2: Burn, baby, BURN.")
                
            elif push.lower() == "n":
                print("\nYou decide not to push the button.")
                print("Strangely, you let out a breath you didn't realize you were holding.")
                print("You don't know how, but you just know you made the right decision.")
                print("You turn back to the room.")
                options.left_door_2()


        elif choice.lower() == "c":
            if items.silver_dagger in options.inventory:
                print("\nYou pull out the silver dagger you found in the kitchen and line it up with the impression")
                print("in the display case. Carefully, you set the knife into the case, making sure not to cut the")
                print("leather strap that holds the knife in place.")
                print("Somewhere in the house, you hear a large thunk, then silence.")
                options.vault(items.silver_dagger["Item name"])
                print("You turn back to the room.")
                options.left_door_2()

            else:
                print("\nYou walk up to the display case and brush away the dust collected on the glass lid.")
                print("It's empty. Figures, maybe some looters took whatever valuable thing may have been inside?")
                print("You look closer and notice the faint impression of a dagger in the velvet cushion of the case.")
                print("Interesting, maybe whoever lived here before liked collecting antiques?")
                print("You turn back to the room.")
                options.left_door_2()
        
        elif choice.lower() == "d":
            print("\nYou decide to leave the living room.")
            options.foyer()
        
        else:
            options.try_again()
            options.left_door()
        


    def right_door():
        print("\nThe right door leads into a small home office. Strangely, the desk lamp is on despite the fact that the house does not have ")
        print("power connected to it. A large globe stand sits next to the desk supported by three legs. It looks like the kind to have a hidden compartment within.")
        options.right_door_2()

    def right_door_2():
        print("\nWhat would you like to do?")
        print("A: Investigate the desk")
        print("B: Investigate the globe stand")
        print("C: Leave the room")
        choice = input()
        
        if choice.lower() == "a":
            print("\nThe desk itself has several drawers, two of which are empty. The main drawer only has a single pen inside it and the bottom left drawer ")
            print("has a locked box with the emblem of a crane on it.")
            options.desk()

        elif choice.lower() == "b":
            if items.old_gear in options.inventory:
                print("\nYou fish the old gear out of your pocket and place it firmly in the hidden compartment of the globe.")
                print("Without any futher action on your part, the gears inexplicably move on their own.")
                print("As you watch the gears seamlessly move together, you hear a loud thunk as something large slides into place.")
                options.vault(items.old_gear["Item name"])
                print("You turn back to the room.")
                options.right_door_2()
            else:
                print("\nYou were right when you guessed the globe had a hidden compartment within it.")
                print("You opened it up to find a contraption made of several gears tucked tightly inside.")
                print("There appears to be a gear missing. Nothing will move without that gear.")
                print("You turn back to the room.")
                options.right_door_2()

        elif choice.lower() == "c":
            print("\nYou decide to leave the room.")
            options.foyer()

        else:
            options.try_again()
            options.right_door()

    def desk():
        print("What do you want to do?")
        print("A. Look at the pen")
        print("B. Look at the box")
        choice = input()

        if choice.lower() == "a":
            print("You look at the pen. It is made of an expensive mahogany with gold trim. You notice an intricate carving of a fancy feather on it.")
            print("You twist the pen and the teeth of a skeleton key pokes out where the ballpoint should be.")
            print("You glance at the box with the carving of a crane on it.")

            print("\nDo you want to use the key on the box? Y/N: ")
            choice_2 = input()
            
            if choice_2.lower() == "y":
                print("\nYou insert the pen key into the key hole on the crane box and give it a twist.")
                print("The lid of the box pops open. Inside, there is only a single red button. You push it.")
                print("Somewhere in the house, you hear a loud thud, then silence.")
                options.vault(items.pen["Item name"])
                print("You turn back to the room.")
                options.right_door_2()
            
            elif choice_2.lower() == "n":
                print("\nYou put the key in your pocket.")
                options.inventory.append(items.pen)
                options.desk()

            else:
                options.try_again()
                options.desk()
                
        elif choice.lower() == "b":
            if items.pen in options.inventory:
                print("\nYou insert the pen key into the key hole on the crane box and give it a twist.")
                print("The lid of the box pops open. Inside, there is only a single red button. You push it.")
                print("Somewhere in the house, you hear a loud thud, then silence.")
                print("You turn back to the room.")
                options.right_door_2()
            else:
                print("You examine the box closely. It appears to have a keyhole in the front and is lined with gold trim around the lid of the box.")
                print("The box is currently locked and cannot be opened.")
                print("You turn back to the room.")
                options.right_door_2()
        
        else:
            options.try_again()
            options.desk()



    def hallway():
        print("\nYou head down the old dusty hallway and find the entrances to two rooms. One is obviously the kitchen,")
        print("the other appears to be the basement.")
        print("\nWhat would you like to do?")
        print("A. Go into the kitchen")
        print("B. Head down into the basement")
        print("C. Go back into the foyer")
        choice = input()

        if choice.lower() == "a":
            print("You head into the kitchen.")
            options.kitchen()

        elif choice.lower() == "b":
            print("You take the first step down into the basement.")
            options.basement()

        elif choice.lower() == "c":
            print("You turn around and head back into the foyer.")
            options.foyer()

        else:
            options.try_again()
            options.hallway()            



    def kitchen():
        print("\nIt is drab, with the cabinets painted a faded yellow with white tile counters.")
        print("The oven stood open like a gaping maw, the door having fallen off the hinges.")
        print("The refrigerator stood about two feet away from the wall, appearing to have been pulled away from it.")
        print("The floor is a checkered black and white and the small table has been destroyed, it looks like it was hit by a massive impact.")
        print("At first, nothing really stands out to you, but then you notice something glinting inside a broken cabinet with no door.")
        print("There is also the matter of opening the refrigerator, whose door is still intact and closed.")
        options.kitchen_2()

    def kitchen_2():
        print("\nWhat would you like to do?")
        print("A. Investigate the glinting object")
        print("B. Open the refrigerator door")
        print("C. Go back into the hallway")
        choice = input("\n")

        if choice.lower() == "a":
            print("\nYou bend down and look deeper into the broken cabinet.")
            print("It is a silver, decorative dagger.")
            options.kitchen_cabinet()
        elif choice.lower() == "b":
            print("\nYou open the refrigerator door. It's full of mold. Mold is growing around the entirety of the space inside.")
            print("An awful smell hits you and close the door immediately.")
            print("You immediately start to itch all over your body. You look down and scream.")
            print("Small, moldy growths are appearing all over your body. You scratch and scratch, but the itch won't go away.")
            print("Mold soon covers your entire body and you find it hard to breathe as spores fill your lungs.")
            print("You collapse as your final breath leaves you.")
            print("GAME OVER: Ending 3: Itchy end")
        elif choice.lower() == "c":
            print("\nYou turn around and go back into the hallway.")
            options.hallway()
        else:
            options.try_again()
            options.kitchen()
            
    def kitchen_cabinet():
        pick_up = input("\nDo you want to pick it up? Y/N: ")
        if pick_up.lower() == "y":
            print("\n\nYou pick up the dagger. The cold heavy knife weighs on your hand and fills you with a small sense of dread.")
            print("You quickly put the item away and turn back to the kitchen.")
            options.inventory.append(items.silver_dagger)
            options.kitchen_2()
        elif pick_up.lower() == "n":
            print("\nYou decide to leave the dagger alone and get back up.")
            options.kitchen_2()
        else:
            options.try_again()
            options.kitchen_cabinet()



    def basement():
        if items.flashlight in options.inventory and options.vault() != 1:
            print("\nNow that you have a light source, you can definitely see better in the dark basement.")
            print("You shine the light around, illuminating the dark, dusty corners of the creepy basement.")
            print("You come to rest the beam on one particuler outcropping of battered concrete on the floor of the basement.")
            print("You slowly approach the slab and note its resemblance to a large vault door.")
            print("You examine it closely and notice there are four large metal bolts keeping the slab in place.")
            print("With nothing else of interest in the basement, you decide to leave.")
            options.hallway()

        elif items.flashlight in options.inventory and options.vault() == 1:
            print("\nHaving put different items back in their proper places or simply flicking a switch, you have unknowingly opened the basement vault.")
            print("The large slab of concrete is no longer held back by the large metal bolts. You lift the concrete slab away, straining with the effort.")
            print("Underneath you spy something strange. It looks like some type of machine, though not one you've ever seen before.")
            print("There is a large stone ring with strange glyphs carved into it. Oddly, the glyphs appear to be glowing rather faintly.")
            print("The ring is held in place by large brackets on the machine. Several glowing buttons appear in a grid to the right of the stone ring.")
            print("Each of the buttons are numbered, 1 - 9, with a small screen directly above the grid of buttons.")
            print("You stare at the machine in confusion, not daring to touch anything for fear of what might happen.")
            print("You hastily get up, intent on leaving the machine be. This might be a good chance to get something for the newspaper, however.")
            print("You fish your phone out of your pocket, intent on taking a picture of the machine. Howvever, your car keys come along with it.")
            print("The keys fall out of reach and hit several buttons on the machine. The stone ring glows brighter and a strange, opaque liquid shimmer appears in the center of the ring.")
            print("You quickly grab the keys and turn to leave, but are soon stopped by a blinding flash of light directly behind you.")
            print("You take a few moments to gather your senses, and soon your eyes adjust to see that you are now standing in front of several trees.")
            print("You spin around, looking around for the familiar concrete walls of the basement, but find nothing but more trees.")
            print("You look up into the pale blue sky, several clouds drifting lazily about, unaware of your current predicament.")
            print("You take out your phone, intent on calling for help, but find you have no signal. You look about helplessly.")
            print("The trees look like those found in some jungle, and now that you're paying more attention, you hear several bizarre animal calls.")
            print("You look back down at the phone and pull up your compass app. It spins around uselessly. You put it back in your pocket.")
            print("You take a hesitant step forward, not knowing where you're going or what you're going to do. You travel further into the jungle...")
            print("GAME OVER: Ending 5: Lost")
            
        else:
            print("\nThe stairs creak as you make your way down into the basement, the aged wood threatening to give out from under you.")
            print("As you reach the bottom of the stairs, complete darkness welcomes you. A faint pitter-patter of water can be heard from somewhere in the basement.")
            print("You reach out blindly, hoping to find a light switch or a pull cord. Finding none, you make your way back up the stairs.")
            options.hallway()



    def stairs(direction):
        if direction == "up" and options.first_stairs:
            print("\nYou head up the stairs, your hand gliding along the surprisingly smooth polished surface of the banister.")
            print("The old wooden steps creak as you make your way up.")
            print("You notice the pale, unfaded patches of wall where pictures used to hang.")
            print("You reach the top of the stairs.")
            options.first_stairs = False
            options.upper_hallway()
        elif direction == "up":
            print("You head up the stairs.")
            options.upper_hallway()
        else:
            print("You head down the stairs.")
            options.foyer()



    def upper_hallway():
        print("\nYou look around the upstairs hallway and immediately notice three doors.")
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
        print("\nYou choose to explore the bathroom.")
        print("You go inside the bathroom and immediately notice the dirty and stained mirror, shattered in the lower right corner.")
        print("There is also a broken down toilet and the shower with a missing showerhead.")
        print("The cabinet doors are missing and there are shards of glass resting in the sink basin.")
        print("Out of the corner of your eye, you notice something move in the mirror.")
        print("You look back to the mirror and examine it closely, staring into your reflection's eyes.")
        print("Your body suddenly freezes and you realize you can't move. You're paralyzed.")
        print("Your fear only grows stronger when you realize your reflection is moving on its own.")
        print("It smiles wickedly as it grabs one of the shards of glass in the basin.")
        print("Suddenly, your body follows your reflection's movements, grabbing an identical shard in the basin.")
        print("The smile on your reflection grows wider as it raises the shard to its throat, your hand following in sync.")
        print("You struggle, trying to shake your head, beg, fling the shard away, anything to stop and regain control of your body.")
        print("It's hopeless. Your reflections stares back at you with triumph when it sees the palpable fear in your eyes.")
        print("Slowly, it digs the shard of glass into its throat.")
        print("You do the same and blood oozes from your neck.")
        print("Ever so slowly, it draws the shard across your neck.")
        print("You cough and sputter, finally regaining control of your body.")
        print("You try desperately to stop the bleeding as a wicked laugh fills the air.")
        print("The world soon fades away as you drop to the floor.")
        print("GAME OVER: Ending 4: Choke")
    


    def bedroom():
        print("\nYou choose to explore the bedroom.")
        print("You make your way into the bedroom and admire the stunning mahogany four-poster bed the takes up the majority of the space.")
        print("There is also a wardrobe, dresser, and a trunk at the end of the bed.")
        print("Seeing no other furniture, you decide either the dresser, trunk, or wardrobe might be worth investigating.")
        options.bedroom_2()

    def bedroom_2():
        print("\nWhich would you like to choose?")
        print("A. Dresser")
        print("B. Trunk")
        print("C. Wardrobe")
        print("D. Leave the bedroom")
        choice = input("\n")

        if choice.lower() == "a":
            print("\nYou go up to the dresser and open the drawers one by one. You don't really find much, except for some mothballs.")
            print("You leave the dresser, closing all the drawers first.")
            options.bedroom_2()
        
        elif choice.lower() == "b":
            print("\nYou crouch in front of the trunk and slowly open it. Inside, you find a single flashlight.")
            print("You flip the switch and find that it still works, despite its obvious age.")
            options.inventory.append(items.flashlight)
            print("You decide to take it with you.")
            options.bedroom_2()
        
        elif choice.lower() == "c":
            print("\nYou walk up to the wardrobe and slowly open it.")
            print("At first, you don't see anything of interest. Looking closer, you see a small switch in the back of")
            print("the wardrobe.")
            options.wardrobe()
        
        elif choice.lower() == "d":
            print("\nYou decide to leave the bedroom.")
            options.upper_hallway()
        
    def wardrobe():
        choice = input("Do you want to flip the switch? Y/N: ")
        if choice.lower() == "y":
            print("\nYou flip the switch and almost immediately hear a loud thunk somewhere in the house.")
            options.vault("Wardrobe switch")
            print("You turn back to the room.")
            options.bedroom_2()
        elif choice.lower() == "n":
            print("\nYou decide to leave the switch alone and turn back to the room.")
            options.bedroom_2()

    
    def attic():
        print("\nYou head up the short staircase and poke your head into the dark gloom of the attic.")
        print("Surprisingly, the attic is quite empty save for an old safe that leaning against one wall of the dusty room.")
        print("Seeing no other option, you head up to the old safe.")
        if items.attic_key in options.inventory:
            print("\nYou notice that unique ellipse shape on the door of the safe from that key you picked up earlier in the foyer.")
            print("Curious, you bring the key out from your pocket and try it in the keyhole of the safe.")
            print("It works.")
            print("You slowly twist the key and hear a satisfying click.")
            print("You creak open the old safe's door. Inside, you find a dusty old gear.")
            print("You add it to your backpack.")
            options.inventory.append(items.old_gear)
            print("You close the old safe and head out of the attic.")
            options.upper_hallway()
        else:
            print("\nYou notice that there's a unique ellipse shape on the door.")
            print("It seems somewhat familiar...")
            print("Unfortunately, you cannot do any more with the safe at this time.")
            print("You make your way back down the short staircase.")
            options.attic()
