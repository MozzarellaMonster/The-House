from Items import items

class options:

    inventory = []
    first_stairs = True
    first_foyer = True

    investigated_display_case = False
    investigated_box = False
    investigated_globe = False
    investigated_safe = False
    investigated_entryway_key = False

    chosen_fireplace = False
    chosen_fridge = False
    chosen_mirror = False

    taken_attic_key = False
    used_attic_key = False

    taken_silver_dagger = False
    used_silver_dagger = False

    taken_old_gear = False
    used_old_gear = False

    taken_pen = False
    used_pen = False

    taken_flashlight = False
    used_wardrobe_switch = False
        
    bolts = 0

    def calc_used_bolts():
        return (4 - options.bolts)

    def try_again():
        print("\nSorry, that is not a valid option. Please try again.\n")

    def vault():
        return options.used_old_gear and options.used_pen and options.used_silver_dagger and options.used_wardrobe_switch

    def retry():
        print("\nWould you like to play again? Y/N: ")
        choice = input()

        if choice.lower() == "y":
            options.start()
        elif choice.lower() == "n":
            exit()
        else:
            options.try_again()
            options.retry()

    def start():
        options.inventory.clear()
        
        options.first_stairs = True
        options.first_foyer = True

        options.investigated_display_case = False
        options.investigated_box = False
        options.investigated_globe = False
        options.investigated_safe = False
        options.investigated_entryway_key = False

        options.chosen_fireplace = False
        options.chosen_fridge = False
        options.chosen_mirror = False

        options.taken_attic_key = False
        options.used_attic_key = False

        options.taken_silver_dagger = False
        options.used_silver_dagger = False

        options.taken_old_gear = False
        options.used_old_gear = False

        options.taken_pen = False
        options.used_pen = False

        options.taken_flashlight = False
        options.used_wardrobe_switch = False
        
        options.bolts = 0
        
        print("_________          _______             _______           _______  _______ ")
        print("\__   __/|\     /|(  ____ \  |\     /|(  ___  )|\     /|(  ____ \(  ____ \"")
        print("   ) (   | )   ( || (    \/  | )   ( || (   ) || )   ( || (    \/| (    \/")
        print("   | |   | (___) || (__      | (___) || |   | || |   | || (_____ | (__    ")
        print("   | |   |  ___  ||  __)     |  ___  || |   | || |   | |(_____  )|  __)   ")
        print("   | |   | (   ) || (        | (   ) || |   | || |   | |      ) || (      ")
        print("   | |   | )   ( || (____/\  | )   ( || (___) || (___) |/\____) || (____/\"")
        print("   )_(   |/     \|(_______/  |/     \|(_______)(_______)\_______)(_______/")
        print("                                                                          ")
    
        print("\nHello! Welcome to The House!")
        print("A mystery awaits you in this accursed abode.")
        print("Will you make it out alive or will The House claim another life?")

        print("\nYou are a journalist investigating the house at the end of the street on Willow Road.")
        print("Throughout your time staying in this town, this house has been the focal point of many stories.")
        print("Stories that give the impression there is more going on than meets the eye.")

        print("\nYou find yourself standing on the porch of the old house. You wonder how this house hasn't been demolished yet.")
        print("You grip the ice-cold doorknob despite it being a warm, sunny summer afternoon. You pull your hand back, surprised.")

        options.porch()

    def porch():
        choice = input("Do you dare to enter the house? Y/N: ")

        if choice.lower() == 'y':
            print("\nYou grip the doorknob again and with a shaky breath, you open the door.")
            options.entryway()

        elif choice.lower() == 'n':
            print("\nYou turn around and head back to your car, head lowered in shame.")
            print("Guess the paper sent out the wrong person for the story, huh?")
            print("GAME OVER: Ending 1: Coward")
            options.retry()

        else:
            options.try_again()
            options.porch()



    def entryway():
        print("\nA dimly lit entryway greets you, sunlight managing to make it in through the caked-on grime coating the large stained glass windows above the front door.")
        print("There's an expensive-looking rug running along the floor and a surprising lack of vandalism, despite the door not being locked.")
        print("There is a small table on one side, a painting on the other, and a door straight ahead leading further into the house.")
        options.entryway_2()

    def entryway_2():
        print("\nWhat would you like to do?")
        print("A. Investigate the table")
        print("B. Investigate the painting")
        print("C. Go through the door")
        print("D. Leave the house")
        choice = input()
        
        if choice.lower() == "a" and options.taken_attic_key:
            print("\nYou open the drawer on the table.")
            print("It is empty. You close it and turn back to the room.")
            options.entryway_2()
        
        elif choice.lower() == "a":
            print("\nYou decide to investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it.")
            options.investigated_entryway_key = True
            options.entryway_key()
            
        elif choice.lower() == "b":
            print("\nYou investigate the painting. It is a self-portait of a very stern-looking man with a large handlebar mustache and piercing blue eyes.")
            print("There is otherwise nothing interesting about it.")
            print("You turn back to the room.")
            options.entryway_2()

        elif choice.lower() == "c":
            print("\nYou go through the door and make your way further inside.")
            options.foyer()
        
        elif choice.lower() == "d":
            print("\nYou try the doorknob. Locked. Looks like you're stuck here.")
            print("You turn back around.")
            options.entryway_2()

        else:
            options.try_again()
            options.entryway_2()

    def entryway_key():
        choice = input("\nDo you want to take the key? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou put the key in your pocket.")
            options.inventory.append(items.attic_key)
            options.taken_attic_key = True
            print("You turn back to the room.")
            options.entryway_2()
                
        elif choice.lower() == "n":
            print("\nYou leave the key alone and turn back to the room.")
            options.entryway_2()
                
        else:
            options.try_again()
            options.entryway_key()



    def foyer():
        if options.first_foyer:
            print("\nIn front of you lies a dimly lit foyer with stairs running up on the right.")
            print("To the left there is a swinging door that looks like it leads to a living room.")
            print("To the right just before the stairs there is another door that looks like it goes into an office.")
            print("And lastly, there is a dark hallway leading further into the house.")
            options.first_foyer = False
            options.foyer_2()
        else:
            options.foyer_2()

    def foyer_2():
        print("\nWhat would you like to do?")
        print("A. Go into the living room")
        print("B. Go into the hallway")
        print("C. Go into the office")
        print("D. Go up the stairs")
        print("E. Go back through the door")
        choice = input()

        if choice.lower() == "a":
            print("\nYou have chosen to go through the left door.")
            options.living_room()
        elif choice.lower() == "b":
            print("\nYou have chosen to go forward into the hallway.")
            options.hallway()
        elif choice.lower() == "c":
            print("\nYou have chosen to go through the right door.")
            options.office()
        elif choice.lower() == "d":
            print("\nYou have chosen to go up the stairs.")
            options.stairs("up")
        elif choice.lower() == "e":
            print("\nYou turn around and head back through the door.")
            options.entryway_2()
        else:
            options.try_again()
            options.foyer_2()


    
    def living_room():
        print("\nThe left door leads to a living room. Dust coats the antique furniture and the faint smell of old books hangs in the air.")
        print("You look about the room.")
        print("A large bookshelf stands directly across from you, covering most of the wall.")
        print("A large, intricately decorated fireplace lies inset into the wall to the right of the bookshelf.")
        print("On the left side of the room a dirty window encrusted with grime lets in just enough light to see by.")
        print("Just below the window lies a glass display case with a wooden frame.")
        options.living_room_2()

    def living_room_2():
        print("\nWhat would you like to do?")
        print("A. Investigate the bookshelf")
        print("B. Investigate the fireplace")
        print("C. Investigate the display case")
        print("D. Leave the room")
        choice = input()

        if choice.lower() == "a":
            print("\nYou go to the bookshelf and look over the old tomes.")
            print("Aside from noticing the majority of them are mystery and thrillers, nothing really stands out about them.")
            print("You give some of them an experimental tug, expecting a cliche hidden room to open, but nothing happens.")
            print("You shrug and turn back to the room.")
            options.living_room_2()
            
        elif choice.lower() == "b":
            options.fireplace()

        elif choice.lower() == "c":
            if items.silver_dagger in options.inventory and options.investigated_display_case:
                print("\nYou pull out the silver dagger you found in the kitchen and line it up with the impression in the display case.")
                print("Carefully, you set the knife into the case, making sure not to cut the leather strap that holds the knife in place.")
                print("Somewhere in the house, you hear a loud thunk, then silence.")
                options.inventory.remove(items.silver_dagger)
                options.used_silver_dagger = True
                options.bolts += 1
                print("You turn back to the room.")
                options.living_room_2()
            
            elif items.silver_dagger in options.inventory and options.investigated_display_case == False:
                print("\nYou walk up to the display case, wiping dust off the glass lid. You open the display case, the hinges creaking as you lift the lid.") 
                print("Inside there is an impression of the dagger you found in the kitchen in the velvet cushion within the case.")
                print("You notice there are also leather straps intended to hold the dagger in place.")
                print("You take out the dagger and carefully set it into the case, securing the leather straps around it.")
                print("Somewhere in the house, you hear a loud thunk, then silence.")
                options.inventory.remove(items.silver_dagger)
                options.used_silver_dagger = True
                options.bolts += 1
                print("You turn back to the room.")
                options.living_room_2()

            elif options.used_silver_dagger:
                print("\nYou look into the display case.")
                print("The silver dagger you put there remains, silver shining brilliantly despite the lighting.")
                print("You turn back to the room.")
                options.living_room_2()

            else:
                print("\nYou walk up to the display case and brush away the dust collected on the glass lid.")
                print("It's empty. Perhaps some looters had stolen whatever was inside before.")
                print("You look closer and notice several leather straps and the faint impression of a dagger in the velvet cushion of the case.")
                print("It appears that the leather straps hold the dagger in place. Interesting.")
                print("You turn back to the room.")
                options.investigated_display_case = True
                options.living_room_2()
        
        elif choice.lower() == "d":
            print("\nYou decide to leave the living room.")
            options.foyer_2()
        
        else:
            options.try_again()
            options.living_room_2()

    def fireplace():
        if options.chosen_fireplace:
                print("You look towards the fireplace and wonder what would have happened if you'd pushed the button.")
                print("You suddenly feel very hot and involuntarily shake your head, as if to deny thinking about it.")
                print("You wipe away a small bead of sweat and turn back to the room.")
                options.living_room_2()
        else:
            print("\nYou go up to the fireplace and admire the intricate carvings of grapevines on it.")
            print("There seems to be one cluster of grapes that stands out from the rest.")
            print("Specifically, one particular grape.")
            print("You graze your hand over it and notice that it gently gives under the pressure of your finger.")
            print("It's a button!")
            push = input("\nWill you push the button, Y/N?: ")

            if push.lower() == "y":
                print("\nYou push the button. Suddenly, a cast iron claw grabs your hand, its grip like a vice.")
                print("You struggle, helplessly trying to pry the claw off your nearly broken hand.")
                print("Despite your efforts, the claw drags you into the fireplace.")
                print("Suddenly, a cast iron gate pops up and barricades you inside the hearth.")
                print("You continue to struggle against the grip of the iron claw when you hear gas being pumped in.")
                print("Your life flashes before your eyes as the world around you is engulfed in flames.")
                print("No one can hear your screams over the roar of the fire.")
                print("\nGAME OVER: Ending 2: Cremation")
                options.retry()
                
            elif push.lower() == "n":
                print("\nYou decide not to push the button.")
                print("Strangely, you let out a breath you didn't realize you were holding.")
                print("You don't know how, but you just know you made the right decision.")
                print("You turn back to the room.")
                options.chosen_fireplace = True
                options.living_room_2()
                
            else:
                options.try_again()
                options.fireplace()
        

    
    def office():
        print("\nThe right door leads into a small home office. Strangely, the desk lamp is on despite the fact that the house does not have power connected to it.")
        print("A large globe stand sits next to the desk supported by three legs. It looks like the kind to have a hidden compartment within.")
        options.office_2()

    def office_2():
        print("\nWhat would you like to do?")
        print("A: Investigate the desk")
        print("B: Investigate the globe stand")
        print("C: Leave the room")
        choice = input()
        
        if choice.lower() == "a" and options.used_pen:
            print("\nYou look back at the desk and spy the unlocked box with the key sticking out of it.")
            print("The desk and its contents are otherwise unchanged.")
            print("You turn back to the room.")
            options.office_2()
        
        elif choice.lower() == "a":
            print("\nThe desk itself has several drawers, two of which are empty.")
            print("The main drawer only has a single pen inside it and the bottom left drawer has a locked box with the emblem of a crane on it.")
            options.desk()

        elif choice.lower() == "b":
            if options.used_old_gear:
                print("\nYou look into the globe, noticing that the gears are still turning without any action on your part.")
                print("Shrugging, you turn back to the room.")
                options.office_2()
            
            elif items.old_gear in options.inventory and options.investigated_globe:
                print("\nYou fish the old gear out of your pocket and place it firmly in the hidden compartment of the globe.")
                print("Without any futher action on your part, the gears inexplicably move on their own.")
                print("As you watch the gears seamlessly move together, you hear a loud thunk as something large slides into place.")
                options.inventory.remove(items.old_gear)
                options.used_old_gear = True
                options.bolts += 1
                print("You turn back to the room.")
                options.office_2()

            elif items.old_gear in options.inventory and options.investigated_globe == False:
                print("\nYou open the globe, having correctly assumed there was a hidden compartment within.")
                print("Inside, there is an intricate assortment of gears arranged into a strange contraption within the globe.")
                print("You notice a missing gear, however. You take out the gear you found in the attic and compare it to the empty space.")
                print("It fits like a glove. You firmly attach it to the mass of gears and immediately, the contraption begins to move.")
                print("Somewhere in the house, you hear a loud thunk that sounds like something large sliding into place.")
                options.inventory.remove(items.old_gear)
                options.used_old_gear = True
                options.bolts += 1
                print("You turn back to the room.")
                options.office_2()

            else:
                print("\nYou were right when you guessed the globe had a hidden compartment within it.")
                print("You opened it up to find a contraption made of several gears tucked tightly inside.")
                print("You give the contraption an experimental tug, but it is firmly attached to the walls of the globe.")
                print("You look closer and notice that there appears to be a gear missing. Nothing will move without that gear.")
                print("You turn back to the room.")
                options.investigated_globe = True
                options.office_2()

        elif choice.lower() == "c":
            print("\nYou decide to leave the room.")
            options.foyer_2()

        else:
            options.try_again()
            options.office_2()

    

    def desk():
        if options.used_pen:
            print("\nYou look at the box with the key sticking out of it.")
            print("There's really nothing else you can do about it.")
            print("You turn back to the room.")
            options.office_2()

        else:
            print("\nWhat would you like to do?")
            print("A. Look at the pen")
            print("B. Look at the box")
            choice = input()

            if choice.lower() == "a" and options.taken_pen:
                print("\nYou take the pen out of your pocket and look at it.")
                print("Feeling silly, you put the pen back and turn your attention back to the desk.")
                options.desk()
            
            elif choice.lower() == "a":
                print("\nYou look at the pen. It is made of an expensive mahogany with gold trim. You notice an intricate carving of a feather on it.")
                print("You twist the pen and the teeth of a skeleton key poke out where the ballpoint should be.")
                options.pen()
                
            elif choice.lower() == "b":
                if options.taken_pen and items.pen in options.inventory:
                    options.box()

                else:
                    print("\nYou examine the box closely. It appears to have a keyhole in the front and is lined with gold trim around the lid of the box.")
                    print("The box is currently locked and cannot be opened.")
                    print("You turn back to the room.")
                    options.investigated_box = True
                    options.office_2()
        
            else:
                options.try_again()
                options.desk()

    def pen():
        choice = input ("\nDo you want to take the pen? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou close the pen and put it in your pocket.")
            options.inventory.append(items.pen)
            options.taken_pen = True
            print("You turn back to the room.")
            options.office_2()

        elif choice.lower() == "n":
            print("You leave the pen alone and turn back to the room.")
            options.office_2()

        else:
            options.try_again()
            options.pen()
            
    def box():
        if options.investigated_box:
            choice = input("\nDo you want to use the pen key on the box? Y/N: ")
            
            if choice.lower() == "y":
                print("\nYou insert the pen key into the keyhole on the crane box and give it a twist.")
                print("The lid of the box pops open. Inside, there is only a single red button. You push it.")
                print("Somewhere in the house, you hear a loud thud, then silence.")
                options.inventory.remove(items.pen)
                options.used_pen = True
                options.bolts += 1
                print("You turn back to the room.")
                options.office_2()
           
            elif choice.lower() == "n":
                print("\nYou leave the box alone and turn back to the room.")
                options.office_2()

            else:
                options.try_again()
                options.box()
        else:
            print("\nYou hold the box up in your hands. Gold trim lines the border of the lid and there is a keyhole in front.")
            print("The box is currently locked, but it looks like the pen key might fit in there.")
            options.investigated_box = True
            options.box()



    def hallway():
        print("\nYou head down the old dusty hallway and find the entrances to two rooms.")
        print("One is obviously the kitchen, the other appears to be the basement.")
        options.hallway_2()
    
    def hallway_2():
        print("\nWhat would you like to do?")
        print("A. Go into the kitchen")
        print("B. Head down into the basement")
        print("C. Go back into the foyer")
        choice = input()

        if choice.lower() == "a":
            print("\nYou head into the kitchen.")
            options.kitchen()

        elif choice.lower() == "b":
            print("\nYou take the first step down into the basement.")
            options.basement()

        elif choice.lower() == "c":
            print("\nYou head back into the foyer.")
            options.foyer_2()

        else:
            options.try_again()
            options.hallway_2()            



    def kitchen():
        print("\nIt is drab, with the cabinets painted a faded yellow with white tile counters.")
        print("The oven stands open like a gaping maw, the door having fallen off the hinges.")
        print("The refrigerator stands about two feet away from the wall, appearing to have been pulled away from it.")
        print("There is a small table off to the left that has been destroyed, it looks like it was hit by a massive impact.")
        print("The floor is a checkered black and white, dirty and stained with some small plants growing through the cracks.")
        print("At first, nothing really stands out to you, but then you notice something glinting inside a broken cabinet with no door.")
        print("There is also the matter of opening the refrigerator, whose door is still intact and closed.")
        options.kitchen_2()

    def kitchen_2():
        print("\nWhat would you like to do?")
        print("A. Look into the cabinet")
        print("B. Open the refrigerator door")
        print("C. Go back into the hallway")
        choice = input()

        if choice.lower() == "a" and options.taken_silver_dagger:
            print("\nYou bend down and look into the broken cabinet.")
            print("It's empty, you stand back up and turn back to the room.")
            options.kitchen_2()

        elif choice.lower() == "a":
            print("\nYou bend down and look deeper into the broken cabinet.")
            print("It is a silver, decorative dagger.")
            options.kitchen_cabinet()

        elif choice.lower() == "b":
            print("\nYou open the refrigerator door. It's full of mold, mold that is growing around the entirety of the space inside.")
            print("Suddenly, spores are violently expelled toward you.")
            print("You splutter and fall backward, desperately trying to rub away the spores in your eyes.")
            print("You immediately start to itch all over your body. You look down with teary eyes and scream.")
            print("Small, moldy growths are appearing all over your body. You scratch and scratch, but the itch won't go away.")
            print("You scratch so hard that you draw blood, allowing the mold to spread even faster.")
            print("Mold soon covers your entire body and you find it hard to breathe as the spores fill your lungs.")
            print("You slowly lose sensation in your body as a cold numbness replaces the itch and the world fades to black.")
            print("GAME OVER: Ending 3: Rot")
            options.retry()

        elif choice.lower() == "c":
            print("\nYou turn around and go back into the hallway.")
            options.hallway_2()
        else:
            options.try_again()
            options.kitchen()
            
    def kitchen_cabinet():
        pick_up = input("\nDo you want to pick it up? Y/N: ")
        if pick_up.lower() == "y":
            print("\nYou pick up the dagger. The cold heavy knife weighs on your hand and fills you with a small sense of dread.")
            print("You quickly put the item away and turn back to the kitchen.")
            options.inventory.append(items.silver_dagger)
            options.taken_silver_dagger = True
            options.kitchen_2()
        elif pick_up.lower() == "n":
            print("\nYou decide to leave the dagger alone and get back up.")
            options.kitchen_2()
        else:
            options.try_again()
            options.kitchen_cabinet()



    def basement():
        if items.flashlight in options.inventory and options.vault():
            print("\nHaving put different items back in their proper places or simply flicking a switch, you have unknowingly opened the basement vault.")
            print("The large slab of concrete is no longer held back by the large metal bolts. You lift the concrete slab away, straining with the effort.")
            print("Underneath you spy something strange. It looks like some type of machine, though not a type you've ever seen before.")
            print("There is a large stone ring with strange glyphs carved into it. Oddly, the glyphs appear to be glowing faintly.")
            print("The ring is held in place by large brackets on the machine. Several glowing buttons appear in a grid to the right of the stone ring.")
            print("Each of the buttons are numbered, 1 - 9, with a small screen directly above the grid of buttons.")
            print("You stare at the machine in confusion, not daring to touch anything for fear of what might happen.")
            print("You hastily get up, intent on leaving the machine be. This might be a good chance to get something for the newspaper, however.")
            print("You fish your phone out of your pocket, intent on taking a picture of the machine. Howvever, your car keys come along with it.")
            print("The keys fall out of reach and hit several buttons on the machine. The stone ring glows brighter and a strange, opaque liquid shimmer appears in the center of the ring.")
            print("You quickly grab the keys and turn to leave, but are soon stunned by a blinding flash of light as an energy pulse erupts directly behind you.")
            print("You topple over as the world swirls around you. You can't tell if it's just your perception or if the world is actually swirling.")
            print("You take a few moments to gather your senses, and soon your eyes adjust to see that you are now standing in a clearing surrounded by trees.")
            print("You spin around, looking around for the familiar concrete walls of the basement, but find nothing but more trees.")
            print("You look up into the pale blue sky, but only see several clouds drifting lazily about, unaware of your current predicament.")
            print("You take out your phone, intent on calling for help, but find you have no signal. You look about helplessly.")
            print("The trees look like those found in some jungle, and now that you're paying more attention, you hear several bizarre animal calls.")
            print("You look back down at the phone and pull up your compass app. It spins around uselessly. You put it back in your pocket.")
            print("You take a hesitant step forward, not knowing where you're going or what you're going to do. You travel further into the jungle...")
            print("GAME OVER: Ending 5: Lost")
            options.retry()
            
        
        elif items.flashlight in options.inventory:
            print("\nNow that you have a light source, you can definitely see better in the dark basement.")
            print("You shine the light around, illuminating the dark, dusty corners of the creepy basement.")
            print("You come to rest the beam on one particuler outcropping of battered concrete on the floor of the basement.")
            print("You slowly approach the slab and note its resemblance to a large vault door.")
            if options.calc_used_bolts() <= 1:
                print("You examine it closely and notice there is " + str(options.calc_used_bolts()) + " large metal bolt keeping the slab in place.")
            else:
                print("You examine it closely and notice there are " + str(options.calc_used_bolts()) + " large metal bolts keeping the slab in place.")
            print("With nothing else of interest in the basement, you decide to leave.")
            options.hallway_2()
            
        else:
            print("\nThe stairs creak as you make your way down into the basement, the aged wood threatening to give out from under you.")
            print("As you reach the bottom of the stairs, complete darkness welcomes you. A faint pitter-patter of water can be heard from somewhere in the basement.")
            print("You reach out blindly, hoping to find a light switch or a pull cord. Finding none, you make your way back up the stairs.")
            options.hallway_2()



    def stairs(direction):
        if direction == "up" and options.first_stairs:
            print("\nYou head up the stairs, your hand gliding along the surprisingly smooth polished surface of the banister.")
            print("The old wooden steps creak as you make your way up.")
            print("You notice pale, unfaded patches of wall where pictures used to hang.")
            print("You reach the top of the stairs.")
            options.first_stairs = False
            options.upper_hallway()

        elif direction == "up":
            print("\nYou head up the stairs.")
            options.upper_hallway_2()
        else:
            print("\nYou head down the stairs.")
            options.foyer_2()


    
    def upper_hallway():
        print("\nYou look around the dusty upstairs hallway, lit only by the light let in through two of the three doors connected to it.")
        print("One seems to lead to an upstairs bathroom, another leads to a bedroom, and yet another opens into a short staircase that could only lead to an attic.")
        options.upper_hallway_2()

    def upper_hallway_2():
        print("\nWhat would you like to do?")
        print("A. Go into the bathroom")
        print("B. Go into the bedroom")
        print("C. Go into the attic")
        print("D. Leave the hallway")
        choice = input()
        
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
            options.upper_hallway_2()
    


    def bathroom():
        print("\nYou choose to explore the bathroom.")
        print("There is also a dirty toilet with a broken commode and no lid. Thankfully, it is dry and... unused.")
        print("There is also a shower with a missing showerhead. A few shower curtain rings hang from a crooked shower rod. The shower curtain is nowhere to be found.")
        print("Afterward, you notice the dirty and stained mirror. It is shattered in the lower righthand corner.")
        print("Several shards of glass rest in the sink basin.")
        print("Out of the corner of your eye, you notice something move in the mirror.")
        print("You quickly look back at the mirror, but don't see anything out of the ordinary.")
        print("Still, something's telling you to look closer...")
        options.bathroom_mirror()
    
    def bathroom_mirror():
        choice = input("\nLook closer at the mirror? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou look at the mirror and examine it closely, staring into your reflection's eyes.")
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
            print("GAME OVER: Ending 4: Slit")
            options.retry()
        
        elif choice.lower() == "n":
            print("\nYou shudder a bit at the creepy sensation, but decide not to look closer at the mirror.")
            print("You turn and leave the bathroom.")
            options.upper_hallway_2()

        else:
            options.try_again()
            options.bathroom_mirror()



    def bedroom():
        print("\nYou choose to explore the bedroom.")
        print("You make your way into the bedroom and admire the stunning mahogany four-poster bed that takes up the majority of the space.")
        print("There is also a wardrobe, dresser, and a trunk at the end of the bed.")
        print("Seeing no other furniture, you decide either the dresser, trunk, or wardrobe might be worth investigating.")
        options.bedroom_2()

    def bedroom_2():
        print("\nWhat would you like to do?")
        print("A. Investigate the dresser")
        print("B. Investigate the trunk")
        print("C. Investigate the wardrobe")
        print("D. Leave the bedroom")
        choice = input()

        if choice.lower() == "a":
            print("\nYou go up to the dresser and open the drawers one by one. You don't really find much, except for some mothballs.")
            print("You leave the dresser, closing all the drawers first.")
            options.bedroom_2()
        
        elif choice.lower() == "b" and options.taken_flashlight:
            print("\nYou look inside the trunk.")
            print("It's empty.")
            print("You turn back to the room.")
            options.bedroom_2()
        
        elif choice.lower() == "b":
            print("\nYou crouch in front of the trunk and slowly lift the rather weighty lid. Inside, you find a single flashlight.")
            print("You flip the switch and find that it still works, despite its obvious age.")
            print("You decide to take it with you.")
            options.inventory.append(items.flashlight)
            options.taken_flashlight = True
            print("You turn back to the room.")
            options.bedroom_2()
        
        elif choice.lower() == "c":
            print("\nYou walk up to the wardrobe and slowly open it.")
            print("At first, you don't see anything of interest.")
            print("Looking closer, you see a small switch in the back of the wardrobe.")
            options.wardrobe()
        
        elif choice.lower() == "d":
            print("\nYou decide to leave the bedroom.")
            options.upper_hallway_2()
        
        else:
            options.try_again()
            options.bedroom_2()
        
    def wardrobe():
        if options.used_wardrobe_switch:
            print("\nYou look into the wardrobe, but there's nothing new here.")
            print("The switch is still flipped, at least.")
            print("You turn back to the room.")
            options.bedroom_2()

        else:
            choice = input("\nDo you want to flip the switch? Y/N: ")
            if choice.lower() == "y":
                print("\nYou flip the switch and almost immediately hear a loud thunk somewhere in the house.")
                options.used_wardrobe_switch = True
                options.bolts += 1
                print("You turn back to the room.")
                options.bedroom_2()
            elif choice.lower() == "n":
                print("\nYou decide to leave the switch alone and turn back to the room.")
                options.bedroom_2()
            else:
                options.try_again()
                options.wardrobe()


 
    def attic():
        print("\nYou head up the short staircase and poke your head into the gloom of the attic.")
        print("Surprisingly, the attic is quite empty save for an old safe that's leaning against one wall of the dusty room.")
        print("Seeing no other option, you head up to the old safe.")
        options.attic_2()

    def attic_2():
        if options.taken_old_gear:
            print("\nYou look into the empty safe, then around the attic.")
            print("There is nothing new, so you head back down the stairs.")
            options.upper_hallway_2()
        
        elif options.used_attic_key and options.taken_old_gear == False:
            print("\nInside the open safe lies the old brass gear.")
            options.gear()

        elif items.attic_key in options.inventory and options.used_attic_key == False:
            print("\nYou notice that unique ellipse shape on the door of the safe from that key you picked up earlier in the foyer.")
            print("You bring out the key and compare the two designs. They match.")

            choice = input("Would you like to use the key on the safe? Y/N: ")
            
            if choice.lower() == "y":
                print("It works. You twist the key and hear a satisfying click.")
                options.used_attic_key = True
                options.inventory.remove(items.attic_key)
                print("You creak open the old safe's door. Inside, you find an old brass gear.")
                options.gear()

            elif choice.lower() == "n":
                print("\nYou decide against trying the key on the safe.")
                print("You turn around and leave the room.")
                options.upper_hallway_2()

            else:
                options.try_again()
                options.attic_2()

        else:
            print("\nYou notice that there's a unique ellipse shape on the door.")
            print("Unfortunately, you cannot do any more with the safe at this time.")
            print("You make your way back down the short staircase.")
            options.upper_hallway_2()

    def gear():
        options.investigated_safe = True
        choice = input("\nDo you want to take the gear? Y/N: ")

        if choice.lower() == "y":
            print("\nYou pick up the old gear and stash it away.")
            options.inventory.append(items.old_gear)
            options.taken_old_gear = True
            print("You close the old safe and head out of the attic.")
            options.upper_hallway_2()
        
        elif choice.lower() == "n":
            print("\nYou decide to leave the old gear alone and leave the room.")
            options.upper_hallway_2()

