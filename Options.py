from turtle import back
from Back_rooms import back_rooms
from Items import items
from Office_room import office_room
from Front_rooms import front_rooms

class options:

    inventory = []
    first_stairs = True
    first_foyer = True

    investigated_display_case = False
    investigated_box = False
    investigated_globe = False
    investigated_safe = False
    investigated_entryway_key = False
    investigated_bathroom = False
    investigated_lamp = False
    investigated_attic = False
    investigated_bed = False
    investigated_bookshelf = False

    bathroom_done = False

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

    def show_inventory():
        inv = ", ".join(item["Item name"] for item in options.inventory)
        print("\n[Inventory: " + inv + "]\n")

    def line():
        print("==========================")
        
    def retry(func = None):
        if func is None:
            print("\nWould you like to play again? Y/N: ")
            choice = input("\n> ")

            if choice.lower() == "y":
                options.start()
            elif choice.lower() == "n":
                exit()
            else:
                options.try_again()
                options.retry()
        else:
            print("\nRetry from the last area? Y/N: ")
            choice = input("\n> ")

            if choice.lower() == 'y':
                func()
            elif choice.lower() == 'n':
                options.retry()
            else:
                options.try_again()
                options.retry(func)



    def start(self):
        options.inventory.clear()
        
        options.first_stairs = True
        options.first_foyer = True

        options.investigated_display_case = False
        options.investigated_box = False
        options.investigated_globe = False
        options.investigated_safe = False
        options.investigated_entryway_key = False
        options.investigated_bathroom = False
        options.investigated_lamp = False
        options.investigated_attic = False
        options.investigated_bed = False
        options.investigated_bookshelf = False

        options.bathroom_done = False

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
        print("You grip the doorknob and are surprised to find it ice cold despite the warm, sunny summer afternoon. You pull your hand back and shudder.")

        options.porch()

    def porch():
        choice = input("Do you dare to enter the house? Y/N: ")

        if choice.lower() == 'y':
            print("\nYou grip the doorknob again and with a shaky breath, you open the door.")
            front_rooms.entryway()

        elif choice.lower() == 'n':
            print("\nYou turn around and head back to your car, head lowered in shame.")
            print("Guess the paper sent out the wrong person for the story, huh?")
            print("GAME OVER: Ending 1: Coward")
            options.retry(options.porch)

        else:
            options.try_again()
            options.porch()


    def hallway():
        print("\nYou head down the old dusty hallway and find the entrances to two rooms.")
        print("One is obviously the kitchen, the other appears to be the basement.")
        options.hallway_2()
    
    def hallway_2():
        options.line()
        options.show_inventory()

        print("\nWhat would you like to do?")
        print("A. Go into the kitchen")
        print("B. Head down into the basement")
        print("C. Go back into the foyer")
        choice = input("\n> ")

        if choice.lower() == "a":
            print("\nYou head into the kitchen.")
            back_rooms.kitchen()

        elif choice.lower() == "b":
            print("\nYou take the first step down into the basement.")
            back_rooms.basement()

        elif choice.lower() == "c":
            print("\nYou head back into the foyer.")
            front_rooms.foyer_2()

        else:
            options.try_again()
            options.hallway_2()
