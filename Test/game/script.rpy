# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows starting sprite
    screen timer_test():
    vbox:
         textbutton "Yes." action Jump("yes")
         textbutton "No." action Jump("no")

    timer 3.0 action Jump("too_slow")
    show eileen happy

    # These display lines of dialogue.

    e "Test."

    e "Placeholder!"

    call battle

    # This ends the game.

    return
