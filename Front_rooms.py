# Living room, Entryway, and Foyer
from Options import options
from Items import items
from Office_room import office_room

class front_rooms:
    
    def entryway():
            print("\nA dimly lit entryway greets you, sunlight managing to make it in through the caked-on grime coating the large stained glass windows above the front door.")
            print("There's an expensive-looking rug running along the floor and a surprising lack of vandalism, despite the door not being locked.")
            print("There is a small table on one side, a painting on the other, and a door straight ahead leading further into the house.")
            front_rooms.entryway_2()

    def entryway_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A. Investigate the table")
        print("B. Investigate the painting")
        print("C. Go through the door")
        print("D. Leave the house")
        choice = input("\n> ")
        
        if choice.lower() == "a" and options.taken_attic_key:
            print("\nYou open the drawer on the table.")
            print("It is empty. You close it and turn back to the room.")
            front_rooms.entryway_2()
        
        elif choice.lower() == "a":
            print("\nYou decide to investigate the table and notice it has only one drawer. You open it.")
            print("Inside, you find a single key with a decorative ellipse on it.")
            options.investigated_entryway_key = True
            front_rooms.entryway_key()
            
        elif choice.lower() == "b":
            print("\nYou investigate the painting. It is a self-portait of a very stern-looking man with a large handlebar mustache and piercing blue eyes.")
            print("There is otherwise nothing interesting about it.")
            print("You turn back to the room.")
            front_rooms.entryway_2()

        elif choice.lower() == "c":
            print("\nYou go through the door and make your way further inside.")
            front_rooms.foyer()
        
        elif choice.lower() == "d":
            print("\nYou try the doorknob. Locked. Looks like you're stuck here.")
            print("You turn back around.")
            front_rooms.entryway_2()

        else:
            options.try_again()
            front_rooms.entryway_2()

    def entryway_key():
        choice = input("\nDo you want to take the key? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou put the key in your pocket.")
            options.inventory.append(items.attic_key)
            options.taken_attic_key = True
            print("You turn back to the room.")
            front_rooms.entryway_2()
                
        elif choice.lower() == "n":
            print("\nYou leave the key alone and turn back to the room.")
            front_rooms.entryway_2()
                
        else:
            options.try_again()
            front_rooms.entryway_key()



    def foyer():
        if options.first_foyer:
            print("\nIn front of you lies a dimly lit foyer with stairs running up on the right.")
            print("To the left there is a swinging door that looks like it leads to a living room.")
            print("To the right just before the stairs there is another door that looks like it goes into an office.")
            print("And lastly, there is a dark hallway leading further into the house.")
            options.first_foyer = False
            front_rooms.foyer_2()
        else:
            front_rooms.foyer_2()

    def foyer_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A. Go into the living room")
        print("B. Go into the hallway")
        print("C. Go into the office")
        print("D. Go up the stairs")
        print("E. Go back through the door")
        choice = input("\n> ")

        if choice.lower() == "a":
            print("\nYou have chosen to go through the left door.")
            front_rooms.living_room()
        elif choice.lower() == "b":
            print("\nYou have chosen to go forward into the hallway.")
            options.hallway()
        elif choice.lower() == "c":
            print("\nYou have chosen to go through the right door.")
            office_room.office()
        elif choice.lower() == "d":
            print("\nYou have chosen to go up the stairs.")
            options.stairs("up")
        elif choice.lower() == "e":
            print("\nYou turn around and head back through the door.")
            front_rooms.entryway_2()
        else:
            options.try_again()
            front_rooms.foyer_2()


    
    def living_room():
        print("\nThe left door leads to a living room. Dust coats the antique furniture and the faint smell of old books hangs in the air.")
        print("You look about the room.")
        print("A large bookshelf stands directly across from you, covering most of the wall.")
        print("A large, intricately decorated fireplace lies inset into the wall to the right of the bookshelf.")
        print("On the left side of the room a dirty window encrusted with grime lets in just enough light to see by.")
        print("Just below the window lies a glass display case with a wooden frame.")
        front_rooms.living_room_2()

    def living_room_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A. Investigate the bookshelf")
        print("B. Investigate the fireplace")
        print("C. Investigate the display case")
        print("D. Leave the room")
        choice = input("\n> ")

        if choice.lower() == "a" and options.investigated_bookshelf:
            print("\nYou walk up to the bookshelf and look over the various publications.")
            print("Everything about the bookshelf remains the same.")
            print("You turn back to the room.")
            front_rooms.living_room_2()
        
        elif choice.lower() == "a":
            print("\nYou go to the bookshelf and look over the old tomes.")
            print("Aside from noticing the majority of them are mystery and thrillers, nothing really stands out about them.")
            print("You give some of them an experimental tug, expecting a cliche hidden room to open, but nothing happens.")
            print("You shrug and turn back to the room.")
            options.investigated_bookshelf = True
            front_rooms.living_room_2()
            
        elif choice.lower() == "b":
            front_rooms.fireplace()

        elif choice.lower() == "c":
            if items.silver_dagger in options.inventory and options.investigated_display_case:
                print("\nYou pull out the silver dagger you found in the kitchen and line it up with the impression in the display case.")
                print("Carefully, you set the knife into the case, making sure not to cut the leather strap that holds the knife in place.")
                print("Somewhere in the house, you hear a loud thunk, then silence.")
                options.inventory.remove(items.silver_dagger)
                options.used_silver_dagger = True
                options.bolts += 1
                print("You turn back to the room.")
                front_rooms.living_room_2()
            
            elif items.silver_dagger in options.inventory and options.investigated_display_case == False:
                print("\nYou walk up to the display case. Now standing in front of it, you wipe off the layer of collected dust and peer inside.")
                print("Upon seeing that it is empty, you open the display case, the hinges creaking as you lift the lid.") 
                print("Inside there is an impression of a dagger on the velvet cushion within the case. It strongly resembles the dagger you found in the kitchen.")
                print("You notice there are also leather straps surrounding the impression seemingly intended to hold the dagger in place.")
                print("You take out the dagger and carefully set it into the case, securing the leather straps around it.")
                print("Somewhere in the house, you hear a loud thunk, then silence.")
                options.inventory.remove(items.silver_dagger)
                options.used_silver_dagger = True
                options.bolts += 1
                print("You turn back to the room.")
                front_rooms.living_room_2()

            elif options.used_silver_dagger:
                print("\nYou look into the display case.")
                print("The silver dagger you put there remains, shining brilliantly despite the poor lighting from the window.")
                print("You turn back to the room.")
                front_rooms.living_room_2()

            else:
                print("\nYou walk up to the display case and brush away the dust collected on the glass lid.")
                print("It's empty. Perhaps some looters had stolen whatever was inside before.")
                print("You look closer and notice several leather straps on the velvet cushion of the case. They surround the faint impression of a dagger.")
                print("It appears that the leather straps hold the dagger in place. Interesting.")
                print("You turn back to the room.")
                options.investigated_display_case = True
                front_rooms.living_room_2()
        
        elif choice.lower() == "d":
            print("\nYou decide to leave the living room.")
            front_rooms.foyer_2()
        
        else:
            options.try_again()
            front_rooms.living_room_2()

    def fireplace():
        if options.chosen_fireplace:
                print("\nYou look towards the fireplace and wonder what would have happened if you'd pushed the button.")
                print("You suddenly feel very hot and involuntarily shake your head, as if to deny thinking about it.")
                print("You wipe away a small bead of sweat and turn back to the room.")
                front_rooms.living_room_2()
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
                options.chosen_fireplace = True
                options.retry(front_rooms.living_room_2)
                
            elif push.lower() == "n":
                print("\nYou decide not to push the button.")
                print("Strangely, you let out a breath you didn't realize you were holding.")
                print("You don't know how, but you just know you made the right decision.")
                print("You turn back to the room.")
                options.chosen_fireplace = True
                front_rooms.living_room_2()
                
            else:
                options.try_again()
                front_rooms.fireplace()