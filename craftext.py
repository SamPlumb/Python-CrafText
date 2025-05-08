import time

# CrafText -


# Variables -
char_len_of_ctrs = []

main_menu = True
display_intro = True

game_running = False


# Items -
log = 0
plank = 0
stick = 0
stone = 0
iron = 0
gold = 0
pick_dur = 0
axe_dur = 0

# Box Ascii -

top_bot = "═"
bot = "═"
sides = "║"

top_left = "╔"
top_right = "╗"
bot_left = "╚"
bot_right = "╝"


ctrs_list = ["Controls",
             " ",
             "[Chop] - Chop down a tree",
             "[Mine] - Mine rock with chance to find stone or minerals.",
             "[Craft] - Open Crafting Menu",
             "[Smelt] - Open Smelting Menu"]

quit_text = "Thank you for playing!"


for ctr in ctrs_list:
    char_len_of_ctrs.append(len(ctr))

width_ctrs = max(char_len_of_ctrs)


# Functions -


def print_c_str(text, padding=100, char_fill=" "):
    text = text.center(padding, char_fill)
    print(text)


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
        print_c_str("Data entered is invalid, Try again")


while game_running:

    print_c_str("Welcome to the CrafText Wilderness")

    if input().lower() == "quit":
        quit_game()


# While running true loop

# Inventory table before each action


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
