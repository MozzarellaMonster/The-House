# Kitchen, Basement, Stairs
from Options import options
from Items import items
from Front_rooms import front_rooms

class back_rooms:
    
    def kitchen():
        print("\nIt is drab, the cabinets are painted a faded yellow and the white tiles of the countertops are either cracked or missing.")
        print("The oven stands open like a gaping maw, the door having fallen off its hinges.")
        print("The refrigerator stands about two feet away from the left wall, appearing to have been pulled away from it.")
        print("There is a small table off to the right that has been destroyed. It looks like it was hit by a massive impact.")
        print("The floor is a checkered black and white, dirty and stained with some small plants growing through the cracks.")
        print("At first, nothing really stands out to you, but then you notice something glinting inside a broken cabinet with no door.")
        print("There is also the matter of opening the refrigerator, the door of which is still intact and closed.")
        back_rooms.kitchen_2()

    def kitchen_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A. Look into the cabinet")
        print("B. Investigate the refrigerator")
        print("C. Go back into the hallway")
        choice = input("\n> ")

        if choice.lower() == "a" and options.taken_silver_dagger:
            print("\nYou bend down and look into the broken cabinet.")
            print("It's empty, you stand back up and turn back to the room.")
            back_rooms.kitchen_2()

        elif choice.lower() == "a":
            print("\nYou bend down and look deeper into the broken cabinet.")
            print("It is a silver, decorative dagger.")
            back_rooms.kitchen_cabinet()

        elif choice.lower() == "b" and options.chosen_fridge:
            print("\nYou glance towards the fridge but quickly avert your gaze and look back towards the rest of the room.")
            back_rooms.kitchen_2()

        elif choice.lower() == "b":
            print("\nYou walk over to the fridge and look it over.")
            print("There are several unidentifiable stains on the outside of the fridge.")
            print("Patches of mold line the edges of the door.")
            back_rooms.fridge()

        elif choice.lower() == "c":
            print("\nYou turn around and go back into the hallway.")
            options.hallway_2()
        else:
            options.try_again()
            back_rooms.kitchen()
            
    def kitchen_cabinet():
        pick_up = input("\nDo you want to pick it up? Y/N: ")
        
        if pick_up.lower() == "y":
            print("\nYou pick up the dagger. The cold heavy knife weighs on your hand and fills you with a small sense of dread.")
            print("You quickly put the item away and turn back to the kitchen.")
            options.inventory.append(items.silver_dagger)
            options.taken_silver_dagger = True
            back_rooms.kitchen_2()
        
        elif pick_up.lower() == "n":
            print("\nYou decide to leave the dagger alone and get back up.")
            back_rooms.kitchen_2()
        
        else:
            options.try_again()
            back_rooms.kitchen_cabinet()

    def fridge():
        choice = input("Do you want to open the fridge door? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou open the refrigerator door. It's full of mold, mold that is growing around the entirety of the space inside.")
            print("Suddenly, spores are violently expelled toward you.")
            print("You splutter and fall backward, desperately trying to rub away the spores in your eyes.")
            print("You immediately start to itch all over your body. You look down with teary eyes and scream.")
            print("Small, moldy growths are appearing all over your body. You scratch and scratch, but the itch won't go away.")
            print("You scratch so hard that you draw blood, allowing the mold to spread even faster.")
            print("Mold soon covers your entire body and you find it hard to breathe as the spores fill your lungs.")
            print("You slowly lose sensation in your body as a cold numbness replaces the itch and the world fades to black.")
            print("GAME OVER: Ending 3: Rot")
            options.chosen_fridge = True
            options.retry(back_rooms.kitchen_2)
        
        elif choice.lower() == "n":
            print("\nYou turn away from the door, but are quickly overcome with a strong dizzy spell.")
            print("Your body suddenly feels incredibly itchy. But as soon as you make a move to scratch, the sensation disappears.")
            print("The dizzy spell also quickly passes and you're left confused.")
            print("You look back at the fridge, but the sight of the mold lining the edges of the door gives you a full-body shudder.")
            print("You quickly back away from the fridge and look to the rest of the room.")
            options.chosen_fridge = True
            back_rooms.kitchen_2()
        
        else:
            options.try_again()
            back_rooms.fridge()

    def basement():
        options.line()
        options.show_inventory()

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
            print("GAME OVER: Ending 5: Lost - TRUE ENDING")
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
            front_rooms.foyer_2()