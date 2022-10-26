# Upper hallway, Bathroom, Bedroom, Attic
from Options import options
from Items import items
from Back_rooms import back_rooms

class upper_rooms:

    def upper_hallway():
        print("\nYou look around the dusty upstairs hallway, which is lit by the feeble amount of light being let in through two of the three doors connected to it.")
        print("One seems to lead to an bathroom, another leads to a bedroom, and the last, much darker, doorway opens into a short staircase that leads further upward into an attic.")
        upper_rooms.upper_hallway_2()

    def upper_hallway_2():
        options.line()
        options.show_inventory()
        
        print("\nWhat would you like to do?")
        print("A. Go into the bathroom")
        print("B. Go into the bedroom")
        print("C. Go into the attic")
        print("D. Leave the hallway")
        choice = input("\n> ")
        
        if choice.lower() == "a":
            upper_rooms.bathroom()
        
        elif choice.lower() == "b":
            upper_rooms.bedroom()

        elif choice.lower() == "c":
            upper_rooms.attic()
            
        elif choice.lower() == "d":
            back_rooms.stairs("down")
        else:
            options.try_again()
            upper_rooms.upper_hallway_2()
    


    def bathroom():
        options.line()
        if options.bathroom_done:
            print("\nThere is no reason to go back into the bathroom.")
            upper_rooms.upper_hallway_2()
        
        elif options.investigated_bathroom:
            print("\nThe bathroom looks the same, yet your gaze is drawn to the mirror.")
            upper_rooms.bathroom_mirror()
        
        else:
            print("\nYou choose to explore the bathroom.")
            print("There is a dirty toilet connected to the left wall with a broken commode and no lid. Thankfully, it is dry and... unused.")
            print("Against the furthest wall there is a shower with a missing showerhead. A few shower curtain rings hang from a broken rod. A shower curtain is nowhere to be found.")
            print("You notice a dirty and stained mirror hanging on the wall over a dirty sink.")
            print("The mirror is shattered, cracks radiating out from the lower righthand corner.")
            print("Several shards of glass rest in the sink basin.")
            print("Out of the corner of your eye, you notice something move in the mirror.")
            print("You quickly look back at the mirror, but don't see anything out of the ordinary.")
            print("Still, something's telling you to look closer...")
            options.investigated_bathroom = True
            upper_rooms.bathroom_mirror()
    
    def bathroom_mirror():
        if options.chosen_mirror:
            print("\nYou resist the urge to look closer and turn away from the mirror, closing your eyes.")
            print("Your heartbeat quickens momentarily and you brush your fingers against your neck, a small itch running across it.")
            print("The itch turns into a slight pain and the image of your maniacal visage flashes in your mind.")
            print("But as swiftly as it appears, it disappears. The slight pain vanishing completely.")
            print("You involuntarily shudder and leave the bathroom.")
            options.bathroom_done = True
            upper_rooms.upper_hallway_2()

        else:
            choice = input("\nLook closer at the mirror? Y/N: ")
        
            if choice.lower() == "y":
                print("\nYou look at the mirror and examine it closely, staring into your reflection's eyes.")
                print("Your body suddenly freezes and you realize you can't move. You're paralyzed.")
                print("Absolute terror sets in when you realize your reflection is moving on its own.")
                print("It smiles wickedly as it grabs one of the reflected shards of glass in the basin.")
                print("Suddenly, your body follows your reflection's movements, grabbing the counterpart shard in the basin.")
                print("The smile on your reflection grows wider as it raises the shard to its throat, your hand following in sync.")
                print("You struggle, trying to shake your head, beg, fling the shard away, anything to stop and regain control of your body.")
                print("It's hopeless. Your reflection stares back at you with triumph when it sees the palpable fear in your eyes.")
                print("Slowly, it digs the shard of glass into its throat.")
                print("You do the same and blood oozes from your neck.")
                print("Ever so slowly, it draws the shard across its neck.")
                print("You cough and sputter as you mimic the movement and slice open your throat.")
                print("Only after making sure its evil deed is done does it relinquish control of your body.")
                print("You immediately grab your neck, hot sticky blood quickly coats the entirety of both of your hands.")
                print("You try desperately to stop the bleeding as your reflection laughs maniacally.")
                print("Darkness encroaches on the edges of your vision as you give one final gasp, your reflection's wicked laughter echoing off the walls.")
                print("The world fades away as you drop to the floor.")
                print("GAME OVER: Ending 4: Slit")
                options.chosen_mirror = True
                options.retry(upper_rooms.bathroom)
        
            elif choice.lower() == "n":
                print("\nYou shudder a bit at the creepy sensation, but decide not to look closer at the mirror.")
                print("You turn and leave the bathroom.")
                options.chosen_mirror = True
                upper_rooms.upper_hallway_2()

            else:
                options.try_again()
                upper_rooms.bathroom_mirror()



    def bedroom():
        print("\nYou choose to explore the bedroom.")
        print("You make your way into the bedroom and admire the stunning mahogany four-poster bed against the left wall that takes up the majority of the space.")
        print("There is also a wardrobe against the far wall, a dresser against the right wall, and a trunk at the end of the bed.")
        upper_rooms.bedroom_2()

    def bedroom_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A. Look in the dresser")
        print("B. Look in the trunk")
        print("C. Look in the wardrobe")
        print("D. Look under the bed")
        print("E. Leave the bedroom")
        choice = input("\n> ")

        if choice.lower() == "a":
            print("\nYou go up to the dresser and open the drawers one by one. You don't really find much, except for some mothballs.")
            print("You leave the dresser, closing all the drawers first.")
            upper_rooms.bedroom_2()
        
        elif choice.lower() == "b" and options.taken_flashlight:
            print("\nYou peer inside the open trunk, its lid laying against the footboard of the bed.")
            print("It's empty.")
            print("You turn back to the room.")
            upper_rooms.bedroom_2()
        
        elif choice.lower() == "b":
            print("\nYou crouch in front of the trunk and struggle to lift the heavy lid. Once you get it open, you find a single flashlight inside.")
            print("You flip the switch and find that it still works, despite its obvious age.")
            print("You decide to take it with you.")
            options.inventory.append(items.flashlight)
            options.taken_flashlight = True
            print("You turn back to the room.")
            upper_rooms.bedroom_2()
        
        elif choice.lower() == "c" and options.used_wardrobe_switch:
            print("\nYou look into the wardrobe, but there's nothing new here.")
            print("The switch is still flipped, at least.")
            print("You turn back to the room.")
            upper_rooms.bedroom_2()
        
        elif choice.lower() == "c":
            print("\nYou walk up to the wardrobe and slowly open it.")
            print("At first, you don't see anything of interest.")
            print("Looking closer, you see a small switch in the back of the wardrobe.")
            upper_rooms.wardrobe()
        
        elif choice.lower() == "d" and options.investigated_bed:
            print("\nYou look underneath the bed again.")
            print("There is still nothing underneath.")
            print("You turn back to the room.")
            upper_rooms.bedroom_2()

        elif choice.lower() == "d":
            print("\nYou get down on your hands and knees next to the bed and look underneath.")
            print("Several dust bunnies scurry away as you breathe out, but there is otherwise nothing under the bed.")
            print("You run your hand underneath regardless, but only manage to collect dust on your appendage.")
            print("You get back up and dust yourself off, then turn back to the room.")
            options.investigated_bed = True
            upper_rooms.bedroom_2()


        elif choice.lower() == "e":
            print("\nYou decide to leave the bedroom.")
            upper_rooms.upper_hallway_2()
        
        else:
            options.try_again()
            upper_rooms.bedroom_2()
        
    def wardrobe():
        choice = input("\nDo you want to flip the switch? Y/N: ")
        
        if choice.lower() == "y":
            print("\nYou flip the switch and almost immediately hear a loud thunk somewhere in the house.")
            options.used_wardrobe_switch = True
            options.bolts += 1
            print("You turn back to the room.")
            upper_rooms.bedroom_2()
        
        elif choice.lower() == "n":
            print("\nYou decide to leave the switch alone and turn back to the room.")
            upper_rooms.bedroom_2()
        
        else:
            options.try_again()
            upper_rooms.wardrobe()


 
    def attic():
        print("\nYou head up the short staircase and poke your head into the dusty gloom of the attic.")

        if options.investigated_attic:
            print("You head to the safe leaning against the wall.")

        else:
            print("Surprisingly, the attic is quite empty save for an old safe that is leaning against one wall of the room.")
            print("Seeing no other option, you head up to the old safe.")
            options.investigated_attic = True
        
        upper_rooms.attic_2()

    def attic_2():
        options.line()
        options.show_inventory()
        
        if options.taken_old_gear:
            print("\nYou look into the empty safe, then around the attic.")
            print("There is nothing new, so you head back down the stairs.")
            upper_rooms.upper_hallway_2()
        
        elif options.used_attic_key and options.taken_old_gear == False:
            print("\nInside the open safe lies the old brass gear.")
            upper_rooms.gear()

        elif items.attic_key in options.inventory and options.used_attic_key == False:
            print("\nYou notice a familiar ellipse shape on the door of the safe. It strongly resembles the design from that key you picked up earlier in the entryway.")
            print("You bring out the key and compare the two designs. They match perfectly.")

            choice = input("Would you like to use the key on the safe? Y/N: ")
            
            if choice.lower() == "y":
                print("\nIt fits. You twist the key and hear a satisfying click.")
                options.used_attic_key = True
                options.inventory.remove(items.attic_key)
                print("You creak open the old safe's door. Inside, you find an old brass gear.")
                upper_rooms.gear()

            elif choice.lower() == "n":
                print("\nYou decide against trying the key on the safe.")
                print("You turn around and leave the room.")
                upper_rooms.upper_hallway_2()

            else:
                options.try_again()
                upper_rooms.attic_2()

        else:
            print("\nYou notice that there's a unique ellipse shape on the door.")
            print("Unfortunately, you cannot do anything with the safe at this time.")
            print("You make your way back down the short staircase.")
            upper_rooms.upper_hallway_2()

    def gear():
        options.investigated_safe = True
        choice = input("\nDo you want to take the gear? Y/N: ")

        if choice.lower() == "y":
            print("\nYou pick up the old gear and stash it away.")
            options.inventory.append(items.old_gear)
            options.taken_old_gear = True
            print("You close the old safe and head out of the attic.")
            upper_rooms.upper_hallway_2()
        
        elif choice.lower() == "n":
            print("\nYou decide to leave the old gear alone and leave the room.")
            upper_rooms.upper_hallway_2()