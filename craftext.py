import time
import textwrap
import random

# TODO - smelting
# TODO - flavour text on using a tool for first time


# CrafText -

# Variables -
char_len_of_ctrs = []
craft_char_len_of_ctrs = []
qty_added = 0
type_added = 0


main_menu = True
display_intro = True

game_running = False
game_start = True

game_chop = False
game_mine = False
game_craft = False
game_smelt = False


# Box Ascii -
top_bot = "═"
bot = "═"
sides = "║"

top_left = "╔"
top_right = "╗"
bot_left = "╚"
bot_right = "╝"


# Items Dict -
plr_inv = {"Logs": 5,
           "Planks": 10,
           "Sticks": 10,
           "Stone": 10,
           "Coal": 30,
           "Iron Ore": 10,
           "Iron Ingot": 10,
           "Gold": 10,
           "Wooden Pickaxe": 1,
           "Stone Pickaxe": 1,
           "Iron Pickaxe": 1,
           "Stone Axe": 1,
           "Wooden Axe": 1,
           "Golden Statue": 1}


# Controls list -
ctrs_list = ["Controls / Player Choices",
             " ",
             "[Quit] - Closes the game",
             "[Controls] - Open this menu (Controls / Player Choices)",
             "[Chop] - Chop down a tree.",
             "[Mine] - Mine rock with chance to find stone or minerals.",
             "[Craft] - Open crafting menu.",
             "[Smelt] - Open smelting menu.",
             "[Bag] - See what items you have."
             ]

craft_ctrs_list = ["Craft Options",
                   "",
                   "[Quit] - Closes the game",
                   "[None] - Closes crafting menu",
                   "[Item Name] - type the name of the item you wish to craft, eg. [Wooden Pickaxe]"
                   ]


# Find length of all the controls in list to create box around them
for ctr in ctrs_list:
    char_len_of_ctrs.append(len(ctr))
ctrs_width_ctrs = max(char_len_of_ctrs)

for ctr in craft_ctrs_list:
    craft_char_len_of_ctrs.append(len(ctr))
craft_ctrs_width_ctrs = max(craft_char_len_of_ctrs)


# Functions -
# Center text - with 100 padding
def print_c_str(text, padding=100, char_fill=" "):
    text = text.center(padding, char_fill)
    print(text)


# Center text - with 100 padding and new line
def print_c_str_nl(text, padding=100, char_fill=" "):
    text = text.center(padding, char_fill)
    print(text)
    print()


# Print line of text in a dynamic box
def print_in_box(text: str):
    str_len = (len(text))

    print_c_str(f"{top_left}{top_bot*(str_len+2)}{top_right}")

    print_c_str(f"║ {text:^{str_len}} ║")

    print_c_str_nl(f"{bot_left}{top_bot*(str_len+2)}{bot_right}")


# Control Menu - with dynamic box around
def ctrs_menu(ctr_list, width):
    print_c_str(f"{top_left}{top_bot*(width+2)}{top_right}")

    for ctrs in ctr_list:
        print_c_str(f"║ {ctrs:^{width}} ║")

    print_c_str_nl(f"{bot_left}{top_bot*(width+2)}{bot_right}")


# Quit Game - Text w box around, 5 second sleep before window closes.
def quit_game():
    print_in_box("Thank you for playing!")
    time.sleep(5)
    exit()


# Open Bag
def open_bag():
    print_c_str(f"{top_left}{top_bot*22}{top_right}")
    for itm, qty in plr_inv.items():
        if qty > 0:
            print_c_str(f"║ {itm:15}: {qty:3} ║")

    print_c_str_nl(f"{bot_left}{top_bot*22}{bot_right}")


# Main Menu Loop -
while main_menu:

    if display_intro == True:
        print_in_box("Welcome To CrafText")
        ctrs_menu(ctrs_list, ctrs_width_ctrs)
        print()
        display_intro = False

    print_c_str_nl("Type [Start] to start a new game, [Quit] to exit: ")
    player_input = input()

    if player_input.lower() == "quit":
        quit_game()

    elif player_input.lower() == "start":
        main_menu = False
        display_intro = True
        game_running = True

    else:
        print_in_box("Answer Invalid, Try again!")

# Main Game Loop -
while game_running:

    # Game Intro -
    if game_start == True:

        print_c_str(f"{top_left}{top_bot*98}{top_right}")

        for line in textwrap.wrap("Ahead of you, a peaceful river meanders through the valley, its clear waters reflecting the soft glow of the sky. The banks are lined with tall, sturdy trees, creating a quiet rhythm with every whisper of wind. In the distance, mountains pierce the sky with snow-capped peaks, while their lower slopes are covered in a blanket of pine trees.", width=96):
            print(f"║ {line.center(96)} ║")

        print_c_str_nl(f"{bot_left}{top_bot*98}{bot_right}")

        print_c_str_nl(
            "Your pockets feel empty, and you only have the clothes on your back. What do you choose to do?")

        player_input = input()
        game_start = False

# Quit Game -
    if player_input.lower() == "quit":
        quit_game()

# Open Controls Menu -
    elif player_input.lower() == "controls":
        ctrs_menu(ctrs_list, ctrs_width_ctrs)

# Open Bag -
    elif player_input.lower() == "bag":
        open_bag()

# Wood Chop -
    elif player_input.lower() == "chop":
        game_chop = True

    # Chop w Stone Axe
        if game_chop:
            while plr_inv.get("Stone Axe") >= 1:

                print_c_str_nl(
                    "Would you like to use your Stone Axe? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

                elif player_input.lower() == "yes":

                    game_chop = False
                    qty_added = random.randint(2, 3)
                    plr_inv["Logs"] += qty_added

                    print_in_box(
                        f"You used your Stone Axe to chop down a tree got {qty_added} Logs.")
                    print_in_box(f"You now have {plr_inv.get('Logs')} Logs.")

                    break

                elif player_input.lower() == "no":
                    break

                else:
                    print_in_box("Answer MUST be either Yes or No, Try Again!")

    # Chop w Wooden Axe
        if game_chop:
            while plr_inv.get("Wooden Axe") >= 1:

                print_c_str_nl(
                    "Would you like to use your Wooden Axe? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

                elif player_input.lower() == "yes":

                    game_chop = False
                    qty_added = random.randint(1, 2)
                    plr_inv["Logs"] += qty_added

                    print_in_box(
                        f"You used your Wooden Axe to chop down a small tree and gained {qty_added} Logs.")
                    print_in_box(f"You now have {plr_inv.get('Logs')} Logs.")

                    break

                elif player_input.lower() == "no":

                    game_chop = False
                    qty_added = random.randint(0, 1)

                    print_in_box(
                        "You chose to try to chop a tree without the Axe from your bag... ")

                # Failed to get Log w Fist (Have Stone Axe)
                    if qty_added == 0:

                        print_in_box(
                            f"You punched a tree as hard as you could but nothing broke loose.")
                        print_in_box(
                            f"You still have {plr_inv.get('Logs')} Logs.")

                # Gain Log w Fist (Have Stone Axe)
                    else:

                        plr_inv["Logs"] += qty_added

                        print_in_box(
                            f"You shook the tree as hard as you could and a branch fell off.")
                        print_in_box(
                            f"You now have {plr_inv.get('Logs')} Logs.")

                    break

                else:
                    print_in_box("Answer MUST be either Yes or No, Try Again!")

    # If player doesn't have an Axe
        if game_chop:

            game_chop = False
            qty_added = random.randint(0, 1)

            if qty_added == 0:

                print_in_box(
                    f"You tried to karate chop the tree but, you didn't even make a dent.")
                print_in_box(
                    f"You still have {plr_inv.get('Logs')} Logs and bruised your hand")

            else:

                plr_inv["Logs"] += qty_added

                print_in_box(
                    f"You found a fallen tree and managed to break off a chunk.")
                print_in_box(f"You now have {plr_inv.get('Logs')} Logs.")

# Mine -
    elif player_input.lower() == "mine":
        game_mine = True

    # Mine w Iron Pickaxe -
        if game_mine:
            while plr_inv.get("Iron Pickaxe") >= 1:

                print_c_str_nl(
                    "Would you like to use your Iron Pickaxe to mine? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

                elif player_input.lower() == "yes":

                    game_mine = False
                    type_added = random.randint(1, 10)

            # TODO - First craft flavour text (implement with crafting)
                    print_in_box(
                        "Your Pickaxe carves though rock like butter enabling you to dig deeper and deeper")

        # Gain Stone w Iron Pickaxe
                    if 1 <= type_added <= 2:
                        qty_added = random.randint(3, 4)
                        plr_inv["Stone"] += qty_added

                        print_in_box(
                            f"You knocked a chunk of rock loose with your Iron Pickaxe. It was just {qty_added} Stone.")
                        print_in_box(
                            f"You now have {plr_inv.get('Stone')} Stone.")

        # Gain Coal w Iron Pickaxe
                    elif 3 <= type_added <= 5:

                        qty_added = random.randint(2, 3)
                        plr_inv["Coal"] += qty_added

                        print_in_box(
                            f"You swung the Iron pickaxe against the rock, breaking it into chunks Coal. You found {qty_added} Coal.")
                        print_in_box(
                            f"You now have {plr_inv.get('Coal')} Coal.")

        # Gain Iron Ore w Iron Pickaxe
                    elif 6 <= type_added <= 8:

                        qty_added = random.randint(1, 2)
                        plr_inv["Iron Ore"] += qty_added

                        print_in_box(
                            f"You hurled your pickaxe at the rock and split a large rock in half revealing {qty_added} Iron Ore.")
                        print_in_box(
                            f"You now have {plr_inv.get('Iron Ore')} Iron Ore.")

        # Gain Gold w Iron Pickaxe
                    else:

                        qty_added = 1
                        plr_inv["Gold"] += qty_added

                        print_in_box(
                            f"After hours down in the mine, you see a sparkle of gold in the corner of your eye. You gained {qty_added} Gold")
                        print_in_box(
                            f"You now have {plr_inv.get('Gold')} Gold.")

                    break

                elif player_input.lower() == "no":
                    break

                else:
                    print_in_box("Answer MUST be either Yes or No, Try Again!")

    # Mine w Stone Pickaxe
        if game_mine:
            while plr_inv.get("Stone Pickaxe") >= 1:

                print_c_str_nl(
                    "Would you like to use your Stone Pickaxe to mine? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

                elif player_input.lower() == "yes":

                    game_mine = False
                    type_added = random.randint(1, 10)

            # TODO first craft flavour text (fix when implemented crafting)
                    print_in_box(
                        "Your Stone Pickaxe cuts though the rock easier enabling you to dig deeper into the earth.")
                    print_in_box("You may potentially find better minerals.")

        # Gain Stone w Stone Pickaxe
                    if 1 <= type_added <= 3:
                        qty_added = random.randint(1, 3)
                        plr_inv["Stone"] += qty_added

                        print_in_box(
                            f"You hit every rock in sight and found nothing but rock. You gained {qty_added} Stone.")
                        print_in_box(
                            f"You now have {plr_inv.get('Stone')} Stone.")

        # Gain Coal w Stone Pickaxe
                    elif 4 <= type_added <= 7:

                        qty_added = random.randint(1, 2)
                        plr_inv["Coal"] += qty_added

                        print_in_box(
                            f"You found a black rock while mining, It seemed different to other rocks so held onto it for safe keeping.")
                        print_in_box(
                            f"You found {qty_added} Coal. You now have {plr_inv.get('Coal')} Coal.")

        # Gain Iron Ore w Stone Pickaxe
                    else:
                        qty_added = 1
                        plr_inv["Iron Ore"] += qty_added

                        print_in_box(
                            f"After hours of no luck, a small redish silver rock broke off the wall. You gained {qty_added} Iron Ore.")
                        print_in_box(
                            f"You now have {plr_inv.get('Iron Ore')} Iron Ore.")

                    break

                elif player_input.lower() == "no":
                    break

                else:
                    print_in_box("Answer MUST be either Yes or No, Try Again!")

    # Mine w Wooden Pickaxe
        if game_mine:
            while plr_inv.get("Wooden Pickaxe") >= 1:

                print_c_str_nl(
                    "Would you like to use your Wooden Pickaxe to mine? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

                elif player_input.lower() == "yes":
                    # TODO - Add flavour text on first craft
                    game_mine = False
                    type_added = random.randint(1, 10)

        # Gain Stone w Wooden Pickaxe
                    if 1 <= type_added <= 5:
                        qty_added = 1
                        plr_inv["Stone"] += qty_added

                        print_in_box(
                            f"You hit the same piece of rock over and over again, finally a chunk split off")
                        print_in_box(
                            f"You gained {qty_added} Stone, You now have {plr_inv.get('Stone')} Stone.")

        # Gain Coal w Wooden Pickaxe
                    elif type_added == 6:

                        qty_added = 1
                        plr_inv["Coal"] += qty_added

                        print_in_box(
                            "You found a black rock while mining, It seemed different to other rocks so held onto it for safe keeping.")
                        print_in_box(
                            f"You found {qty_added} Coal. You now have {plr_inv.get('Coal')} Coal.")

        # Fail w Wooden Pickaxe
                    else:
                        print_in_box(
                            "You swung your Wooden Pickaxe and it bounced back, the rock seemed unfazed.")
                        print_in_box(
                            "You found nothing. Better Luck next time.")

                    break

                elif player_input.lower() == "no":
                    break

                else:
                    print_in_box("Answer MUST be either Yes or No, Try Again!")

    # If player does not have/select a Pickaxe
        if game_mine:

            print_in_box("You require a Pickaxe to mine rocks")
            game_mine = False

# Craft -
    elif player_input.lower() == "craft":
        game_craft = True

        print_c_str(f"{top_left}{top_bot*56}{top_right}")

        if plr_inv.get("Logs") >= 1:
            print_c_str(f"║{' ':56}║")
            print_c_str(f"║ {'1 Log':^25} -> {'2 Planks':^25} ║")
            print_c_str(f"║ {'1 Log':^25} -> {'4 Sticks':^25} ║")

        if plr_inv.get("Planks") >= 3 and plr_inv.get("Sticks") >= 2:
            print_c_str(f"║{' ':56}║")
            print_c_str(
                f"║ {'2x Sticks, 3x Planks':^25} -> {'1 Wooden Pickaxe':^25} ║")
            print_c_str(
                f"║ {'2x Sticks, 3x Planks':^25} -> {'1 Wooden Axe':^25} ║")

        if plr_inv.get("Stone") >= 3 and plr_inv.get("Sticks") >= 2:
            print_c_str(f"║{' ':56}║")
            print_c_str(
                f"║ {'2x Sticks, 3x Stone':^25} -> {'1 Stone Pickaxe':^25} ║")
            print_c_str(
                f"║ {'2x Sticks, 3x Stone':^25} -> {'1 Stone Axe':^25} ║")

        if plr_inv.get("Iron Ingot") >= 3 and plr_inv.get("Sticks") >= 2:
            print_c_str(f"║{' ':56}║")
            print_c_str(
                f"║ {'2x Sticks, 3x Iron Ingots':^25} -> {'1 Iron Pickaxe':^25} ║")

        print_c_str(f"║{' ':56}║")
        print_c_str_nl(f"{bot_left}{top_bot*56}{bot_right}")

        while game_craft:
            print_c_str_nl("What would you like to craft?: ")
            player_input = input()

            if player_input.lower() == "quit":
                quit_game()

            elif player_input.lower() == "none":
                game_craft = False
                break

            elif player_input.lower() == "craft controls":
                ctrs_menu(craft_ctrs_list, craft_ctrs_width_ctrs)

            elif player_input.lower() == "planks":

                max_craft = plr_inv.get('Logs')

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Logs':^30} : {plr_inv.get('Logs'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Planks Recipe:':^40}║")
                print_c_str(f"║{'1x Log -> 2x Planks':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many logs would you like to use (1 - {max_craft}?): ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Logs"] -= int(player_input)
                        plr_inv["Planks"] += (int(player_input*2))

                        print_in_box(
                            f"You crafted {int(player_input)*2} Planks.")
                        print_in_box(f"You have {plr_inv['Logs']} Logs left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            elif player_input.lower() == "sticks":

                max_craft = plr_inv.get('Logs')

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Logs':^30} : {plr_inv.get('Logs'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Sticks Recipe:':^40}║")
                print_c_str(f"║{'1x Log -> 4x Sticks':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many logs would you like to use (1 - {max_craft}?): ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Logs"] -= int(player_input)
                        plr_inv["Sticks"] += (int(player_input)*4)

                        print_in_box(
                            f"You crafted {int(player_input)*4} Sticks.")
                        print_in_box(f"You have {plr_inv['Logs']} Logs left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            elif player_input.lower() == "wooden pickaxe":

                max_craft = min((int(plr_inv.get('Planks')/3)),
                                (int(plr_inv.get('Sticks')/2)))

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Planks':^30} : {plr_inv.get('Planks'):^5} ║")
                print_c_str(
                    f"║ {'Total Sticks':^30} : {plr_inv.get('Sticks'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Wooden Pickaxe Recipe:':^40}║")
                print_c_str(
                    f"║{'2x Sticks, 3x Planks -> Wooden Pickaxe':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many Wooden Pickaxe would you like to craft (1 - {max_craft})?: ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Planks"] -= (int(player_input)*3)
                        plr_inv["Sticks"] -= (int(player_input)*2)
                        plr_inv["Wooden Pickaxe"] += (int(player_input))

                        print_in_box(
                            f"You crafted {int(player_input)} Wooden Pickaxe.")
                        print_in_box(
                            f"You have {plr_inv['Planks']} Planks and {plr_inv['Sticks']} Sticks left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            elif player_input.lower() == "wooden axe":
                
                max_craft = min((int(plr_inv.get('Planks')/3)),
                                (int(plr_inv.get('Sticks')/2)))

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Planks':^30} : {plr_inv.get('Planks'):^5} ║")
                print_c_str(
                    f"║ {'Total Sticks':^30} : {plr_inv.get('Sticks'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Wooden Axe Recipe:':^40}║")
                print_c_str(
                    f"║{'2x Sticks, 3x Planks -> Wooden Axe':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many Wooden Axe would you like to craft (1 - {max_craft})?: ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Planks"] -= (int(player_input)*3)
                        plr_inv["Sticks"] -= (int(player_input)*2)
                        plr_inv["Wooden Axe"] += (int(player_input))

                        print_in_box(
                            f"You crafted {int(player_input)} Wooden Axe.")
                        print_in_box(
                            f"You have {plr_inv['Planks']} Planks and {plr_inv['Sticks']} Sticks left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            elif player_input.lower() == "stone pickaxe":

                max_craft = min((int(plr_inv.get('Stone')/3)),
                                (int(plr_inv.get('Sticks')/2)))

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Stone':^30} : {plr_inv.get('Stone'):^5} ║")
                print_c_str(
                    f"║ {'Total Sticks':^30} : {plr_inv.get('Sticks'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Stone Pickaxe Recipe:':^40}║")
                print_c_str(
                    f"║{'2x Sticks, 3x Stone -> Stone Pickaxe':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many Stone Pickaxe would you like to craft (1 - {max_craft})?: ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Stone"] -= (int(player_input)*3)
                        plr_inv["Sticks"] -= (int(player_input)*2)
                        plr_inv["Stone Pickaxe"] += (int(player_input))

                        print_in_box(
                            f"You crafted {int(player_input)} Stone Pickaxe.")
                        print_in_box(
                            f"You have {plr_inv['Stone']} Stone and {plr_inv['Sticks']} Sticks left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            elif player_input.lower() == "stone axe":
                
                max_craft = min((int(plr_inv.get('Stone')/3)),
                                (int(plr_inv.get('Sticks')/2)))

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Stone':^30} : {plr_inv.get('Stone'):^5} ║")
                print_c_str(
                    f"║ {'Total Sticks':^30} : {plr_inv.get('Sticks'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Stone Axe Recipe:':^40}║")
                print_c_str(
                    f"║{'2x Sticks, 3x Stone -> Stone Axe':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many Stone Axe would you like to craft (1 - {max_craft})?: ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Stone"] -= (int(player_input)*3)
                        plr_inv["Sticks"] -= (int(player_input)*2)
                        plr_inv["Stone Axe"] += (int(player_input))

                        print_in_box(
                            f"You crafted {int(player_input)} Stone Axe.")
                        print_in_box(
                            f"You have {plr_inv['Stone']} Stone and {plr_inv['Sticks']} Sticks left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            elif player_input.lower() == "iron pickaxe":
                
                max_craft = min((int(plr_inv.get('Iron Ingot')/3)),
                                (int(plr_inv.get('Sticks')/2)))

                print_c_str(f"{top_left}{top_bot*40}{top_right}")
                print_c_str(
                    f"║ {'Total Iron Ingots':^30} : {plr_inv.get('Iron Ingot'):^5} ║")
                print_c_str(
                    f"║ {'Total Sticks':^30} : {plr_inv.get('Sticks'):^5} ║")
                print_c_str(f"║{' ':^40}║")
                print_c_str(f"║{'Iron Pickaxe Recipe:':^40}║")
                print_c_str(
                    f"║{'2x Sticks, 3x Iron Ingot -> Iron Pickaxe':^40}║")
                print_c_str_nl(f"{bot_left}{top_bot*40}{bot_right}")

                while game_craft:

                    print_c_str_nl(
                        f"How many Pickaxe would you like to craft (1 - {max_craft})?: ")
                    player_input = input()

                    if not player_input.isdigit():
                        print_in_box(
                            f"{player_input} is not a number, please enter a number between 1 and {max_craft}.")

                    elif 1 <= int(player_input) <= max_craft:
                        plr_inv["Iron Ingot"] -= (int(player_input)*3)
                        plr_inv["Sticks"] -= (int(player_input)*2)
                        plr_inv["Iron Pickaxe"] += (int(player_input))

                        print_in_box(
                            f"You crafted {int(player_input)} Iron Pickaxe.")
                        print_in_box(
                            f"You have {plr_inv['Iron Ingot']} Iron Ingots and {plr_inv['Sticks']} Sticks left.")

                        game_craft = False
                        break

                    else:
                        print_in_box(
                            f"{player_input} is not an valid number between 1 and {max_craft}, Try again!")

            # elif player_input.lower == "iron axe":
            #     pass

            else:
                print_in_box(f"{player_input} is not an action, Try again!")
                print_in_box(
                    "Type [Craft Controls] if you want to see actions you can perform.")

        # print_c_str(f"║ {'Total logs':^12}:  {logs:^12} ║")
        # print_c_str(f"║ {'-'*27:^24} ║")
        # print_c_str(f"║ {'1 Log -> 2 Planks':20}: {math.floor(logs / 2):3} ║")

# Smelt -
    elif player_input.lower() == "smelt":
        pass

# Invalid Action -
    else:

        print_in_box(f"{player_input} is not an action, Try again!")
        print_in_box(
            "Type [Controls] if you want to see actions you can perform.")

# Next Action -
    if game_start == False:
        print_c_str_nl("What would you like to do next?: ")
        player_input = input()


# Planning -


# Wood pick 10 durability, 2 stick, 3 plank
# Gold star 5 gold win    continue playing, new game, quit.

# 20 durability
# Stone axe, 2 stick, 3 stone
# Stone pickaxe, 2 stick 3 stone

# 30 durability
# Iron pick

# Smelting
# Iron, 2iron ore 1 coal
# Charcoal, 4 log


# small chunk of silver and redish looking rock broke off.
