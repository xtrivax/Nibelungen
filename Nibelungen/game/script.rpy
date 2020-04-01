# The script of the game goes in this file.

#Init varialbes
init:
    $ timer_range = 0
    $ timer_jump = 0
    # varialbes to check whether the player has been somewher or not
    $ arena = ""
    $ castle = ""
    $ cave = ""
    $ city = ""

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#define mc = Character("Main Character", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
define mc = Character("Main Character")
define wb = Character("World Builder")
define gm = Character("Guildmaster")


# define the images
image female_gm = "human_female.png"
image knight_gm = "solid_ritter.png"



image goblin = im.Scale("goblin.png", 460, 500)
image cave = im.Scale("new_cave.jpg", 1920, 1080)
image arena  = im.Scale("arena.jpg", 1920, 1080)
image city = im.Scale("city.jpg", 1920, 1080)
image castle = im.Scale("castle.jpg", 1920, 1080)
image school = im.Scale("school.jpg", 1920, 1080)
image map = im.Scale("map.jpg", 1920, 1080)


screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

default timeout = 5.0
default timeout_label = None
default persistent.timed_choices = True


#location system
default Location = "cave"


screen choice(items):
  style_prefix "choice"

  vbox:
    for i in items:
      textbutton i.caption action i.action

    if (timeout_label is not None) and persistent.timed_choices:

      bar:
        xalign 0.5
        ypos 400
        xsize 740
        value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

      timer timeout action Jump(timeout_label)



# The game starts here.

label start:


    # checks if this mission has already been done
    if  cave == "done":
        scene cave
        wb "You've already cleared this cave of enemys, I'll take you back to the map"
        jump map




    stop music fadeout 1
    $ renpy.pause(2.0)


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "audio/cave.mp3"
    $ renpy.pause(4.0)


    scene cave
    with Dissolve(7.0)


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
    stop music
    play music "audio/battle.mp3"
    wb "Now the creature is close enough that you notice its green skin and sharp teeth."
    wb "The creature draws out a sword and jumps towards you."
    wb "In the very last moment you manage to dodge."
    wb "The creature falls on the ground"
    wb "Now as you directly look  into the eyes of the creature, you see there is no doubt, it must be a Goblin."
    wb "The Goblin yells and gets up immediately"
    wb "He spreads his sword towards you."
    wb "There is no other option, he wants to stab you to death"
    show goblin at right
    $ picture = "gimar"
    image MC = "[picture].png"
    label attack:

      #set the label that is jumped to if the player doesn't make a decision
      $ timeout_label = "dead"

    menu:
      "Rush towards him and disarm the Goblin":
        $ picture = "Main_Ritter"
        jump knight

      "Conjure a Spell":
        $ picture = "gimar"
        jump mage




    label knight:

      show MC at left
      $ player_warrior = Char("Player:", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
      $ mc = player_warrior
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
      hide goblin
      jump choosen

    label mage:
      show MC at left
      $ player_mage = Char("Player:", 5, 416, 535, 359, 535, 239, 379, [fireball, flamethrower], [], 0, 0)
      $ mc = player_mage
      wb"You instinctively try to cast a spell."
      wb"slowly you see that a ball that looks to be made of fire forms in your hand."
      wb"you can feel the heat that comes from the ball in your hand, it feels like its burning your skin."
      wb"as the goblin run towards you, you fling the fireball at him."
      wb"the impact of the fireball knocks the goblin back."
      wb"he screams in pain as he burns to a crisp."
      hide goblin
      jump choosen

    label dead:
      hide screen countdown
      wb"you died"

      return




    # First Real Battle
    wb "You step over the dead body and step into the tunnels in front of you."
    wb "You follow the tunnel a while before you hear some steps"
    wb "You sneak close in case of another Goblin"
    wb "You walk around the corner when you see it."
    wb "The Goblin notices you and you prepare for battle."
    label choosen:
      $ timeout_label = None
      $ party_list = [mc]
      python:
        enemies_list = []
        testenemy1 = Char("Goblin", 5, 274, 1, 185, 80, 152, 80, [], [], 0, 5)
        #testenemy2 = Char("Hobgoblin", 5, 354, 1, 284, 149, 209, 152, [], [], 0, 10)
        #testenemy3 = Char("Slime", 5, 304, 1, 80, 125, 180, 200, [], [], 0, 5)
        enemies=[testenemy1]
        for i in enemies:
            enemies_list.append (i)


      call battle



    # after you've won the cave fight

    label cave_finish:
        hide screen battle_screen
        scene cave
        wb"Congratulations, you have proven yourself a brave warrior."
        wb"But this was only the beginning."
        wb"In the menu you will find your inventory."
        wb"You can now also use the map and change your localisation by clicking the text."
        wb"Go and explore the wide world of Nibelungen!"
        play music "audio/background_music.mp3" fadein 1.5
        $ cave = "done"

        jump map


    label map:
        scene Map

        $ GameRunning = True
        while GameRunning:
            $ Location_img = Location.lower()
            if renpy.has_image(Location_img, exact=True):
                show expression Location_img

            menu:


                "Current Location: [Location]"

                #Checks if a Laction has been selected if yes, takes you there.
                # Locations are defined in scripts/evenets.rpy file
                "Open Map":
                    window hide
                    $ Location = renpy.call_screen("MapScreen", _layer="screens")
                    if Location == "Castle":
                        jump Castle
                    elif Location == "Arena":
                        jump Arena
                    elif Location == "Cave":
                        jump start
                    elif Location == "City":
                        jump City


                    window show


    label Castle:
        scene castle

        #if castle == "done":
            #wb "You've already been here, I'll take you back to the map"
            #jump map
        wb "This is the castle of Nibelungen"

        wb "It is the safest place of whole Nibelungen"
        wb "If the castle falls all Nibelungen falls"
        hide screen castle
        $ castle = "done"
        jump map

    label Arena:
        scene arena
        #if arena == "done":
            #wb "You've already been here, I'll take you back to the map"
            #jump map
        wb "You are in the great arena"
        wb "Here you can train with other Heros or fight monsters"

        label arena_chose_fight:

          wb "Strømper"
          menu:
              "Chose what you want to do"

              "Fight Monsters":
                  menu:
                    "Which monster do you want to fight?"

                    "Fight Wolf":
                        $ party_list = [mc]
                        python:
                          enemies_list = []
                          wolf = Char("Wolf", 5, 354, 1, 284, 149, 209, 152, [], [], 0, 10)
                          enemies_list = [wolf]
                        call battle

                    "Fight Slime":
                        $ party_list = [mc]
                        python:
                          enemies_list = []
                          slime = Char("Slime", 5, 304, 1, 80, 125, 180, 200, [], [], 0, 5)
                          enemies_list = [slime]
                        call battle

              "Fight other Adventurers":
                  if mc.level > 10:
                    wb "You will fihgt a young adventurer that uses the Sword"
                    $ adventurer = Char("Kevin:", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
                    $ enemies_list = [adventurer]
                    call battle
                  else:
                    wb "You are not experienced enough for this"
                    jump arena_chose_fight

              "Return":
                  return




        hide screen arena
        $ arena = "done"
        jump map


    label City:
        scene city
        #if city == "done":
            #wb "You've already been here, I'll take you back to the map"
            #jump map
        wb "You are in the City"
        wb "Here you can meet other players and bet"
        wb "Don't lose all your coins, you will need them"
        wb "Here also you can trade by selling or buying items. You also accept mercenary services"
        wb "For each completed mission you earn goldcoins and special items"
        show female_gm at left
        show knight_gm at right
        menu:
            "Chose the person you want to talk to"

            "Talk to him":
                hide female_gm
                gm "What do you want?"
                hide knight_gm
                show MC at left
                "I'm offering to do mercany services for you"
                hide MC
                show knight_gm at right
                gm "When I have a job where I need some additional manpower I will come back to your offer"
                gm "Maybe next time."
                hide knight_gm
                jump leave

            "Talk to her":
                hide knight_gm
                gm "I've heard of your great victory against a Goblin!"
                hide female_gm
                show MC at right
                "I hope I can offer you some mercenary services"
                "I would love to accpet one right now"
                hide MC
                show female_gm at left
                gm "I'm afraid I have no Jobs for you right now, but for sure later on"
                gm "Come back another day."
                hide female_gm
                jump leave



    label leave:
        wb "semms like you need to speak to the other Guildermaster next time."
        wb "Let us return and check for mercenay services later on."
        hide screen city
        $ city = "done"
        jump map
