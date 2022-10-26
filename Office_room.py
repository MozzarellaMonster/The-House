# Office_room
from Options import options
from Items import items
from Front_rooms import front_rooms

class office_room:
    
    def office():
        print("\nThe right door leads into a small home office. Strangely, the desk lamp is on despite the fact that the house does not have power connected to it.")
        print("The desk lamp is also the only source of light in the office, since the room does not have any windows at all.")
        print("A large globe stand sits next to the desk supported by three legs. It looks like the kind to have a hidden compartment within.")
        office_room.office_2()

    def office_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A: Investigate the desk")
        print("B: Investigate the globe stand")
        print("C: Investigate the desk lamp")
        print("D: Leave the room")
        choice = input("\n> ")
        
        if choice.lower() == "a" and options.used_pen:
            print("\nYou look back at the desk and see only the unlocked box with the key sticking out of it.")
            print("The desk is otherwise unchanged.")
            print("You turn back to the room.")
            office_room.office_2()

        elif choice.lower() == "a" and options.taken_pen:
            print("\nYou look at the desk and notice that now only the locked box remains in the bottom left drawer.")
            print("The rest of the drawers remain empty. The pen prods at your leg, almost as if urging you to use it.")
            office_room.desk()
        
        elif choice.lower() == "a":
            print("\nThe desk is made of polished mahogany with carvings of jungle scenes decorating its walls. The desk itself has several drawers, many of which are empty.")
            print("The main drawer only has a single pen inside it and the bottom left drawer has a locked box with an etching of a crane on it.")
            print("The others appear to have been hurriedly emptied, with several stray papers lying about the room.")
            office_room.desk()

        elif choice.lower() == "b":
            if options.used_old_gear:
                print("\nYou look into the globe, observing the gears that continue to turn without any action on your part.")
                print("Shrugging, you turn back to the room.")
                office_room.office_2()
            
            elif items.old_gear in options.inventory and options.investigated_globe:
                print("\nYou fish the old gear out of your pocket and place it firmly in the hidden compartment of the globe.")
                print("Without any futher action on your part, the gears inexplicably move on their own.")
                print("As you watch the gears seamlessly move together, you hear a loud thunk as something large slides into place.")
                options.inventory.remove(items.old_gear)
                options.used_old_gear = True
                options.bolts += 1
                print("You turn back to the room.")
                office_room.office_2()

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
                office_room.office_2()

            else:
                print("\nYou were right when you guessed the globe had a hidden compartment within it.")
                print("You open it up to find a contraption made of several gears tucked tightly inside.")
                print("You give the contraption an experimental tug, but it is firmly attached to the walls of the globe.")
                print("You look closer and notice that there appears to be a gear missing. Nothing will move without that gear.")
                print("You turn back to the room.")
                options.investigated_globe = True
                office_room.office_2()
        
        elif choice.lower() == "c" and options.investigated_lamp:
            print("\nYou look at the lamp on the desk, face contorted in mild annoyance.")
            print("You decide it would be better to just leave it alone. It's not like you can take it anywhere anyways.")
            print("Giving a small shake of your head, you turn back to the room.")
            office_room.office_2()
        
        elif choice.lower() == "c":
            print("\nYou walk up to the desk and take a look at the lamp, wondering exactly how it manages to stay on despite the lack of power to the house.")
            print("The lamp closely resembles your typical bankers lamp and is made of shiny brass with a glossy emerald-colored lampshade.")
            print("You try to lift it up off the desk but it is stuck fast to the mahogany surface despite the obvious contrast in build materials.")
            print("You give a few more tugs, but it doesn't move at all. Curious, you follow the power cord to the nearest outlet.")
            print("There, lying in front of the outlet is the plug, disconnected from the house entirely.")
            print("Now even more curious, you plug the lamp into the outlet and are immediately enveloped in total darkness as the lamp immediately turns off.")
            print("Surprised, you unplug the lamp and the room is once more bathed in warm light.")
            print("Now absolutely baffled, you plug and unplug the lamp several times, resulting in the same effect.")
            print("After a while, you decide to leave well enough alone, having gained no answers at all. You drop the cord as you turn back to the room.")
            options.investigated_lamp = True
            office_room.office_2()

        elif choice.lower() == "d":
            print("\nYou decide to leave the room.")
            front_rooms.foyer_2()

        else:
            options.try_again()
            office_room.office_2()

    def desk():
        if options.used_pen:
            print("\nYou look at the box with the key sticking out of it.")
            print("There's really nothing else you can do about it.")
            print("You turn back to the room.")
            office_room.office_2()

        else:
            print("\nWhat would you like to do?")
            print("A. Look at the pen")
            print("B. Look at the box")
            choice = input("\n> ")

            if choice.lower() == "a" and options.taken_pen:
                print("\nYou fish the pen out of your pocket and look at it.")
                print("Feeling silly, you put the pen back and turn your attention back to the desk.")
                office_room.desk()
            
            elif choice.lower() == "a":
                print("\nYou look at the pen. It is made of an expensive mahogany with gold trim. You notice an intricate carving of a feather on it.")
                print("You twist the pen and the teeth of a skeleton key poke out where the ballpoint should be.")
                office_room.pen()
                
            elif choice.lower() == "b":
                if options.taken_pen and items.pen in options.inventory:
                    office_room.box()

                else:
                    print("\nYou examine the box closely. It appears to have a keyhole in the front and is lined with gold trim around the lid of the box.")
                    print("The lid of the box bears the etched picture of a beautiful Sandhill crane on it.")
                    print("The box is currently locked and cannot be opened.")
                    print("You turn back to the room.")
                    options.investigated_box = True
                    office_room.office_2()
        
            else:
                options.try_again()
                office_room.desk()

    def pen():
        choice = input ("\nDo you want to take the pen? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou close the pen and put it in your pocket.")
            options.inventory.append(items.pen)
            options.taken_pen = True
            print("You turn back to the room.")
            office_room.office_2()

        elif choice.lower() == "n":
            print("\nYou close the pen and put it back in the drawer.")
            print("You turn back to the room.")
            office_room.office_2()

        else:
            options.try_again()
            office_room.pen()
            
    def box():
        if options.investigated_box:
            print("\nThe box with the gold trim remains locked.")
            choice = input("\nDo you want to use the pen key on the box? Y/N: ")
            
            if choice.lower() == "y":
                print("\nYou insert the pen key into the keyhole on the crane box and give it a twist.")
                print("The lid of the box pops open. Inside, there is only a single red button. You push it.")
                print("Somewhere in the house, you hear a loud thud, then silence.")
                options.inventory.remove(items.pen)
                options.used_pen = True
                options.bolts += 1
                print("You turn back to the room.")
                office_room.office_2()
           
            elif choice.lower() == "n":
                print("\nYou leave the box alone and turn back to the room.")
                office_room.office_2()

            else:
                options.try_again()
                office_room.box()
        else:
            print("\nYou hold the box up in your hands. Gold trim lines the border of the lid and there is a keyhole in front.")
            print("On the lid of the box there is an etching of a Sandhill crane.")
            print("The box is currently locked, but it looks like the pen key might fit in there.")
            options.investigated_box = True
            office_room.box()