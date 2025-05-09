import time
import textwrap
import random

# TODO - put box on invalid action
# TODO - finish mining
# TODO - update chop to be written like mining
# TODO - do crafting, smelting


# CrafText -

# Variables -
char_len_of_ctrs = []
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
plr_inv = {"Logs": 0,
           "Planks": 0,
           "Stick": 0,
           "Stone": 0,
           "Coal": 30,
           "Iron Ore": 0,
           "Iron Ingot": 0,
           "Gold": 0,
           "Wooden Pickaxe": 1,
           "Stone Pickaxe": 1,
           "Iron Pickaxe": 1,
           "Stone Axe": 1}

# Controls list -
ctrs_list = ["Controls / Player Choices",
             " ",
             "[controls] - Open this menu (Controls / Player Choices)",
             "[Chop] - Chop down a tree.",
             "[Mine] - Mine rock with chance to find stone or minerals.",
             "[Craft] - Open crafting menu.",
             "[Smelt] - Open smelting menu.",
             "[Bag] - See what items you have."]


# Find length of all the controls in list to create box around them
for ctr in ctrs_list:
    char_len_of_ctrs.append(len(ctr))

width_ctrs = max(char_len_of_ctrs)


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


# Control Menu - with dynamic box around
def ctrs_menu():
    print_c_str(f"{top_left}{top_bot*(width_ctrs+2)}{top_right}")

    for ctrs in ctrs_list:
        print_c_str(f"║ {ctrs:^{width_ctrs}} ║")

    print_c_str(f"{bot_left}{top_bot*(width_ctrs+2)}{bot_right}")
    print()


# Main Menu Text -
def main_menu_txt():
    print_c_str_nl("Welcome To CrafText")
    print_c_str_nl("Text-based crafting game!")
    print()


# Quit Game - Text w box around, 5 second sleep before window closes.
def quit_game():

    quit_text = "Thank you for playing!"

    print_c_str(f"{top_left}{top_bot*(len(quit_text)+2)}{top_right}")
    print_c_str(f"║ {quit_text:^{len(quit_text)}} ║")
    print_c_str(f"{bot_left}{top_bot*(len(quit_text)+2)}{bot_right}")

    time.sleep(5)
    exit()


# Incorrect Answer (Yes/No) -
def incorrect_answer():

    incorrect_text = ("Answer MUST be either Yes or No: ")

    print_c_str(f"{top_left}{top_bot*(len(incorrect_text)+2)}{top_right}")
    print_c_str(f"║ {incorrect_text:^{len(incorrect_text)}} ║")
    print_c_str(f"{bot_left}{top_bot*(len(incorrect_text)+2)}{bot_right}")
    print()


# Open Bag
def open_bag():

    for itm, qty in plr_inv.items():
        if qty > 0:
            print_c_str(f"{itm:15}: {qty:3}")


# Game Loop -
    # Main Menu screen -
while main_menu:

    if display_intro == True:
        main_menu_txt()
        ctrs_menu()
        display_intro = False

    print()
    print_c_str_nl("Type [Start] to start a new game, [Quit] to exit: ")
    start = input()

    if start.lower() == "quit":
        quit_game()

    elif start.lower() == "start":
        main_menu = False
        display_intro = True
        game_running = True

    else:
        print_c_str_nl("Action entered is invalid, Try again!")

    # Main Game Loop -
while game_running:

    # Game Intro -
    if game_start == True:

        print_c_str(f"{top_left}{top_bot*98}{top_right}")

        for line in textwrap.wrap("Ahead of you, a peaceful river meanders through the valley, its clear waters reflecting the soft glow of the sky. The banks are lined with tall, sturdy trees, creating a quiet rhythm with every whisper of wind. In the distance, mountains pierce the sky with snow-capped peaks, while their lower slopes are covered in a blanket of pine trees.", width=96):
            print(f"║ {line.center(96)} ║")

        print_c_str(f"{bot_left}{top_bot*98}{bot_right}")
        print()

        print_c_str_nl(
            "Your pockets feel empty, and you only have the clothes on your back. What do you choose to do?")

        game_start = False

    if game_start == False:
        print_c_str_nl("What would you like to do next?: ")
    player_input = input()


# Quit Game -
    if player_input.lower() == "quit":
        quit_game()


# Open Controls Menu -
    elif player_input.lower() == "controls":
        ctrs_menu()


# Open Bag -
    elif player_input.lower() == "bag":
        open_bag()


# Wood Chop -
    elif player_input.lower() == "chop":

        game_chop = True

        while game_chop:

            # If player has stone axe
            if plr_inv.get("Stone Axe") > 0:

                print_c_str_nl(
                    "Would you like to use your Stone Axe? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

    # Player uses Stone Axe
                elif player_input.lower() == "yes":

                    game_chop = False

                    qty_added = random.randint(2, 3)
                    plr_inv["Logs"] += qty_added

                    print_c_str_nl(
                        f"You used your Stone Axe to chop down a tree got {qty_added} Logs. You now have {plr_inv.get('Logs')} Logs.")

    # Player doesn't use Stone Axe
                elif player_input.lower() == "no":

                    game_chop = False
                    qty_added = random.randint(0, 1)

                    print_c_str_nl(
                        "You chose to try to chop a tree without the Axe from your bag... ")

    # Failed to get Log w Fist (Have Stone Axe)
                    if qty_added == 0:

                        print_c_str_nl(
                            f"You punched a tree as hard as you could but nothing broke loose. You still have {plr_inv.get('Logs')} Logs.")

    # Gain Log w Fist (Have Stone Axe)
                    else:

                        plr_inv["Logs"] += qty_added

                        print_c_str_nl(
                            f"You shook the tree as hard as you could and a branch fell off. You now have {plr_inv.get('Logs')} Logs.")

     # If player entered incorrect answer
                else:

                    incorrect_answer()

    # If player doesn't have an Axe
            elif plr_inv.get("Stone Axe") == 0:

                game_chop = False
                qty_added = random.randint(0, 1)

    # Failed to get Log w Fist
                if qty_added == 0:

                    print_c_str_nl(
                        f"You tried to karate chop the tree but, you didn't even make a dent. You still have {plr_inv.get('Logs')} Logs and a bruised hand")

    # Gain Log w fist
                else:

                    plr_inv["Logs"] += qty_added

                    print_c_str_nl(
                        f"You found a fallen tree and managed to break off a chunk. You now have {plr_inv.get('Logs')} Logs.")


# Mine -
    elif player_input.lower() == "mine":

        game_mine = True

        while plr_inv.get("Iron Pickaxe") >= 1:

            print_c_str_nl(
                "Would you like to use your Iron Pickaxe to mine? (Yes/No): ")
            player_input = input()

    # Mine w Iron Pickaxe -
            if player_input.lower() == "quit":
                quit_game()

            elif player_input.lower() == "yes":

                game_mine = False
                type_added = random.randint(1, 10)

    # Gain Stone w Iron Pickaxe
                if 1 <= type_added <= 2:
                    qty_added = random.randint(3, 4)
                    plr_inv["Stone"] += qty_added

                    print_c_str_nl(
                        f"You knocked a chunk of rock loose with your Iron Pickaxe. It was just {qty_added} Stone. You now have {plr_inv.get('Stone')} Stone.")

    # Gain Coal w Iron Pickaxe
                elif 3 <= type_added <= 5:

                    qty_added = random.randint(2, 3)
                    plr_inv["Coal"] += qty_added

                    print_c_str_nl(
                        f"You swung the Iron pickaxe against the rock, breaking it into chunks Coal. You found {qty_added} Coal. You now have {plr_inv.get('Coal')} Coal.")

    # Gain Iron Ore w Iron Pickaxe
                elif 6 <= type_added <= 8:

                    qty_added = random.randint(1, 2)
                    plr_inv["Iron Ore"] += qty_added

                    print_c_str_nl(
                        f"You hurled your pickaxe at the rock and split a large rock in half revealing {qty_added} Iron. You now have {plr_inv.get('Iron Ore')} Iron Ore.")

    # Gain Gold w Iron Pickaxe
                else:

                    qty_added = 1
                    plr_inv["Gold"] += qty_added

                    print_c_str_nl(
                        f"After hours down in the mine, sweat dripping form your face, you see a sparkle of gold in the corner of your eye. You gained {qty_added} Gold")

                break

            elif player_input.lower() == "no":
                break

            else:
                incorrect_answer()
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
                    print(1)
                    break

                elif player_input.lower() == "no":
                    break

                else:
                    incorrect_answer()

        if game_mine:
            while plr_inv.get("Wooden Pickaxe") >= 1:

                print_c_str_nl(
                    "Would you like to use your Wooden Pickaxe to mine? (Yes/No): ")
                player_input = input()

                if player_input.lower() == "quit":
                    quit_game()

                elif player_input.lower() == "yes":

                    game_mine = False
                    print(1)
                    break

                elif player_input.lower() == "no":
                    break

                else:
                    incorrect_answer()

        if game_mine:
            print_c_str_nl("You require a Pickaxe to mine rocks")
            game_mine = False


# Craft -
    elif player_input.lower() == "craft":
        pass


# Smelt -
    elif player_input.lower() == "smelt":
        pass


# Invalid Action -
    else:
        print_c_str_nl("Action entered is invalid, Try again!")
        print_c_str_nl(
            "Type [Controls] if you want to see actions you can perform.")


# TODO - Planning -


# Mine Rock w (pick required) chance to get stone coal, if stone pick, chance to get iron
# If iron pick chance to get gold

# Crafting - Only show craft option if inventory has required materials.
# Plank 2 -1 log
# Stick 4 -1 log

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
