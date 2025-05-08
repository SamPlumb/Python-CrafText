import time
import textwrap
import random

# CrafText -


# Variables -
char_len_of_ctrs = []
qty_added = 0


main_menu = True
display_intro = True

game_running = False
game_start = True

# Box Ascii -

top_bot = "═"
bot = "═"
sides = "║"

top_left = "╔"
top_right = "╗"
bot_left = "╚"
bot_right = "╝"


# Items -

plr_inv = {"Logs": 0,
           "Planks": 0,
           "Stick": 0,
           "Stone": 0,
           "Coal": 3,
           "Iron Ore": 0,
           "Iron Ingot": 0,
           "Gold": 0,
           "Wooden Pickaxe": 0,
           "Stone Pickaxe": 0,
           "Iron Pickaxe": 0,
           "Stone Axe": 1}


ctrs_list = ["Controls / Player Choices",
             " ",
             "[controls] - Open this menu (Controls / Player Choices)",
             "[Chop] - Chop down a tree.",
             "[Mine] - Mine rock with chance to find stone or minerals.",
             "[Craft] - Open crafting menu.",
             "[Smelt] - Open smelting menu.",
             "[Bag] - See what items you have."]

quit_text = "Thank you for playing!"


for ctr in ctrs_list:
    char_len_of_ctrs.append(len(ctr))

width_ctrs = max(char_len_of_ctrs)


# Functions -


def print_c_str(text, padding=100, char_fill=" "):
    text = text.center(padding, char_fill)
    print(text)

# def print_multi_line(text, width=100, )


def ctrs_menu():
    print_c_str(f"{top_left}{top_bot*(width_ctrs+2)}{top_right}")

    for ctrs in ctrs_list:
        print_c_str(f"║ {ctrs:^{width_ctrs}} ║")

    print_c_str(f"{bot_left}{top_bot*(width_ctrs+2)}{bot_right}")


def main_menu_txt():
    print_c_str("Welcome To CrafText")
    print_c_str("Text-based crafting game!")
    print()


def quit_game():

    print_c_str(f"{top_left}{top_bot*(len(quit_text)+2)}{top_right}")
    print_c_str(f"║ {quit_text:^{len(quit_text)}} ║")
    print_c_str(f"{bot_left}{top_bot*(len(quit_text)+2)}{bot_right}")

    time.sleep(5)
    exit()


while main_menu:

    if display_intro == True:
        main_menu_txt()
        ctrs_menu()
        display_intro = False

    print()
    print_c_str("Type [Start] to start a new game, [Quit] to exit: ")
    start = input()

    if start.lower() == "quit":
        quit_game()

    elif start.lower() == "start":
        main_menu = False
        display_intro = True
        game_running = True

    else:
        print_c_str("Action entered is invalid, Try again!")


while game_running:

    if game_start == True:

        print_c_str(f"{top_left}{top_bot*98}{top_right}")

        for line in textwrap.wrap("Ahead of you, a peaceful river meanders through the valley, its clear waters reflecting the soft glow of the sky. The banks are lined with tall, sturdy trees, creating a quiet rhythm with every whisper of wind. In the distance, mountains pierce the sky with snow-capped peaks, while their lower slopes are covered in a blanket of pine trees.", width=96):
            print(f"║ {line.center(96)} ║")

        print_c_str(f"{bot_left}{top_bot*98}{bot_right}")
        print()

        print_c_str(
            "Your pockets feel empty, and you only have the clothes on your back. What do you choose to do?")
        print()

        game_start = False

    player_input = input()


# Quit -
    if player_input.lower() == "quit":
        quit_game()


# Controls -
    elif player_input.lower() == "controls":
        ctrs_menu()

    elif player_input.lower() == "bag":
        for itm, qty in plr_inv.items():
            if qty >= 1:
                print_c_str(f"{itm:15}: {qty}")


# Wood Chop -
    elif player_input.lower() == "chop":
        if plr_inv.get("Stone Axe") >= 1:
            player_input = input(
                "Would you like to use your Stone Axe? (Yes/No): ")
            print()

            if player_input.lower() == "yes":

                qty_added = random.randint(2, 3)
                plr_inv["Logs"] += qty_added

                print_c_str(
                    f"You used your Stone Axe to chop down a tree got {qty_added} Logs. You now have {plr_inv.get('Logs')} Logs.")

            elif player_input.lower() == "no":

                qty_added = random.randint(0, 1)

                print_c_str(
                    "You chose to try to chop a tree without the Axe from your bag... ")
                print()

                if qty_added == 0:

                    print_c_str(
                        f"You punched a tree as hard as you could but nothing broke loose. You still have {plr_inv.get('Logs')} Logs.")
                    print()

                else:

                    # Gain 1 Log
                    plr_inv["Logs"] += qty_added

                    print_c_str(
                        f"You shook the tree as hard as you could and a branch fell off. You now have {plr_inv.get('Logs')} Logs.")
        else:
            qty_added = random.randint(0, 1)

            if qty_added == 0:

                print_c_str(
                    f"You tried to karate chop the tree but, you didn't even make a dent. You still have {plr_inv.get('Logs')} Logs and a bruised hand")

            else:

                # Gain 1 Log
                plr_inv["Logs"] += qty_added

                print_c_str(
                    f"You found a fallen tree and managed to break off a chunk. You now have {plr_inv.get('Logs')} Logs.")


# Mine -
    elif player_input.lower() == "mine":
        pass


# Craft -
    elif player_input.lower() == "craft":
        pass


# Smelt -
    elif player_input.lower() == "smelt":
        pass


# Invalid Action -
    else:
        print_c_str("Action entered is invalid, Try again!")
        print_c_str(
            "Type [controls] if you want to see actions you can perform.")


# Actions
# Hit Tree w fist / pick %50 chance with fist.

# Mine Rock w (pick required) chance to get stone coal, if stone pick, chance to get iron

# If iron pick chance to get gold

# Craft

# Plank 2 -1 log
# Stick 4 -1 log

# Wood pick 10 durability, 2 stick, 3 plank

# 20 durability
# Stone axe, 2 stick, 3 stone
# Stone pickaxe, 2 stick 3 stone
# Iron pick

# Gold star 5 gold win    continue playing or quit.


# Smelting
# Iron, 2iron ore 1 coal

# Charcoal, 4 log

# Only show craft option if inventory has required materials.
