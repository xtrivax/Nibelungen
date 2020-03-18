# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Main Character")
define wb = Character("World Builder")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    wb "It's dark around you and you feel slightly cold as you wake up."
    wb "You try to pull up your blanket and Sleep another round. "
    wb "But you grab in to thr air. There is no blanket you realise."
    wb "You feel the ground around yourself. The ground is cold and Hard."
    wb "Dimm light come from cracks in the ceiling."
    wb "Your eyes adjust slowly to the Darkness."
    wb "It seems like you are in some sort of a cave."
    wb "You see a small Tunnel that seems to lead out of the cave."
    wb "A small silhouette comes from the tunnel towards you."
    mc " Hello is someone here?"
    wb "The movement stops shortly, then the silhouette turns to you"
    mc "what are you"
    wb "The silhouette is to small to be human"
    wb "The small creatur screeches and comes towards you."
    mc "Dont come any closer."
    wb "The creature doesn't seem to responde you."
    wb "It gets close and closer to you by every second"
    wb "Now the creature is close enough that you notice its green skin and sharp teeth."
    wb "The creature draws out a sword and jumps towards you."
    wb "In the very last moment you manage to dodge."
    wb "The creature falls on the ground"
    wb "Now as you directly look  into the eyes of the creature, you see there is no doubt, it must be a Goblin."
    wb "The Goblin yells and gets up immediately"
    wb "He spreads his sword towards you."
    wb "There is no other option, he wants to stab you to death"

    menu:
     "what do you do?"

     "Rush towards him and disarm the Goblin":
        image Knight MC = "Main_Ritter.png"
        show Knight MC at left
        wb"You rush towards the Goblin. "
        wb"The surprised Goblin swings his Sword after you. "
        
        wb"But you react fast and evade it. "
        wb"You hit the Sword out of his Hand and then kick him in the chest. "
        wb"He Stumbles. Which gives you enough Time to get his Sword from the Ground."
        
        wb"You attack him immediately and stab into his chest. "
        wb"He cries in Agony while you press him to the ground. "
        wb"It becomes quiet. You apply some more pressure just to be sure and then pull the               
        sword out "
        wb"Blood flows down the sword and you shortly clean it on the Goblins leather clothes. "
        wb"You look at the Sword, its not exactly new but still in good Condition." 
        wb"There is no scabbard but it should do just fine."

     "Conjure a Spell":
        image Mage MC = "gimar.png"
        show Mage MC at left
        wb"You instinctively try to cast a spell."
        wb"slowly you see that a ball that looks to be made of fire forms in your hand."
        wb"you can feel the heat that comes from the ball in your hand, it feels like its burning your skin."
        wb"as the goblin run towards you, you fling the fireball at him."
        wb"the impact of the fireball knocks the goblin back."
        wb"he screams in pain as he burns to a crisp."

    # First Real Battle

    call battle

    return
