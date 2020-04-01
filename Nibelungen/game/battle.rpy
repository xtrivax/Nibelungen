define battle_narrator = Character(None, interact=False)
hide screen cave
screen battle_screen:
    vbox:
        xalign 0.01 yalign 0.05
        spacing 5

        for each_party_member in party_list:
            frame:
                size_group "party"
                xminimum 250 xmaximum 250
                yminimum 75
                vbox:
                    text "[each_party_member.name]" size 22 xalign 0.5
                    null height 2.5
                    hbox:
                        bar:
                            xmaximum 130
                            value each_party_member.hp
                            range each_party_member.maxhp
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None

                        null width 5

                        text "[each_party_member.hp] / [each_party_member.maxhp]" size 16

                    hbox:
                        bar:
                            xmaximum 130
                            value each_party_member.mp
                            range each_party_member.maxmp
                            left_gutter 0
                            right_gutter 0
                            thumb None
                            thumb_shadow None

                        null width 5

                        text "[each_party_member.mp] / [each_party_member.maxmp]" size 16
        hbox:
            if players_turn and each_enemy_member.hp > 0:
                textbutton "Attack ->" action Return("attack") yminimum 75
            else:
                textbutton "Attack ->" action None yminimum 75

            if players_turn and each_enemy_member.hp > 0:
                textbutton "Spell ->" action Return("spell") yminimum 75
            else:
                textbutton "Spell ->" action None yminimum 75

            frame:
                size_group "party"
                yminimum 40
                text "Potions left - [potions_left]" yalign 0.5
            if players_turn and potions_left > 0:
                textbutton "<- Use" action Return("heal") yminimum 40
            else:
                textbutton "<- Use" action None yminimum 40


    vbox:
        xalign 0.99 yalign 0.05
        spacing 5

        if enemies_list != []:
            for i, each_enemy_member in enumerate(enemies_list):
                hbox:

                    frame:
                        size_group "enemies"
                        xminimum 250 xmaximum 250
                        yminimum 75
                        vbox:
                            text "[each_enemy_member.name]" size 22 xalign 0.5
                            null height 2.5
                            hbox:
                                bar:
                                    xmaximum 130
                                    value each_enemy_member.hp
                                    range each_enemy_member.maxhp
                                    left_gutter 0
                                    right_gutter 0
                                    thumb None
                                    thumb_shadow None

                                null width 5

                                text "[each_enemy_member.hp] / [each_enemy_member.maxhp]" size 16


init python:
    def check_party(x):
        #### This function will check
        # if at least one of X party members is alive.
        #
        for member in x:
            if member.hp > 0:
                return "ok"

        return "lost"



label battle:
    #### Some variables that describes the game state.
    #
    # The "party_list" is a list of all allies each one of that
    # it is normally defined outside battle but for testpuposes can be defined here
    #
    # testmc = Char("Main Character", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
    # party_list =[testmc]
    $ potions_left = 0
    $ players_turn = False

    #### Enemies list will have the description for enemies.
    #this list is defined outside of battle for testpurpose it can be defined here
    #testenemy1 = Char("Goblin", 5, 274, 1, 185, 80, 152, 80, [], [], 0, 5)
    #$ enemies_list = [testenemy1]

    #calculate enemy xp worth
    $ battlexp = enemyxpworth(enemies_list)

    scene black

    #### Let's show the game screen.
    #
    show screen battle_screen



    "Let the battle begins!"

    #### Main battle loop.
    #
    label battle_2_loop:

        #### At first let's check if player's party is ok.
        #
        if check_party(party_list) == "lost":
            jump battle_2_lose


        #### All the party members will do their actions one after another.
        #
        $ party_index = 0

        while party_index < len(party_list):

            $ current_player = party_list[party_index]

            #### Current player will act only if he still alive.
            #
            if current_player.hp > 0:

                #### Let's check if enemies party is still ok.
                #
                if check_party(enemies_list) == "lost":
                    jump battle_2_win

                #### Let the player make his turn.
                #
                label action_choice:
                    #just a jump beacon


                $ players_turn = True

                battle_narrator"[current_player.name], it's your turn now."

                #### Store the result of player's interaction.
                #

                $ res = ui.interact()

                #### Now disallow player's interact with the game.
                #
                $ players_turn = False

                if res == "heal":
                    $ current_player.hp = min( current_player.hp +5, current_player.maxhp )
                    $ potions_left -= 1
                    "*Drink* 5hp restored"

                #choose_enemy
                elif res == "attack":
                    python:
                        enemy_menu = [(enemy.name, enemy) for enemy in enemies_list]
                        choice = menu(enemy_menu)
                        choosen_enemy = choice
                        player_damage = current_player.generate_damage()
                        dmg = choosen_enemy.take_damage(player_damage)
                    "Take this! you dealt [dmg] damage"
                elif res == "spell":
                    python:
                        spell_menu = [(spell.name, spell) for spell in current_player.magic]
                        spell_menu.append(("Return", "return"))
                        choice = menu(spell_menu)
                    if choice == "return":
                        jump action_choice
                    python:
                        spell = choice
                        enemy_menu = [(enemy.name, enemy) for enemy in enemies_list]
                        choice = menu(enemy_menu)
                        choosen_enemy = choice
                        player_damage = current_player.generate_skilldamage(spell)
                        current_mp = current_player.get_mp()

                        if spell.cost > current_mp:
                            print("Not enough MP")
                            renpy.jump(action_choice)

                        current_player.reduce_mp(spell.cost)
                        dmg = choosen_enemy.take_skilldamage(player_damage, spell)
                    "Take this! you dealt [dmg] damage"




            #### And the turn goes to the next party member.
            #
            $ party_index += 1



        ##### And now it's enemies party turn.
        #
        # At first let's check if enemy's party is ok.
        #
        if check_party(enemies_list) == "lost":
            jump battle_2_win



        #### All the party members will do their actions one after another.
        #
        $ enemy_index = 0

        while enemy_index < len(enemies_list):
            $ current_enemy = enemies_list[enemy_index]

            #### Current enemy will act only if he is still alive.
            #
            if current_enemy.hp > 0:

                #### Let's check if player's party is still ok.
                #
                if check_party(party_list) == "lost":
                    jump battle_2_lose

                #### Enemy will attack the random player.
                #
                $ party_member_to_attack = party_list[renpy.random.randint( 0, (len(party_list)-1) )]

                $ enemy_damage = current_enemy.generate_damage()

                $dmg = party_member_to_attack.take_damage(enemy_damage)

                "Rrrrr! [enemy.name] dealt [dmg] damage to [party_member_to_attack.name]"




            #### And the turn goes to the next party member.
            #
            $ enemy_index += 1


        #### Next round of the battle.
        #
        call battle_2_loop


#### The results of the game.
#
label battle_2_win:
    stop music fadeout 0.5
    $ renpy.pause(0.2)
    play sound "audio/victory.mp3"
    "Well done!"
    $ renpy.pause(2.0)
    $ xpgain(party_list, battlexp)
    "You have gained [battlexp]xp"
    return

label battle_2_lose:
    "X_X"
    hide screen battle_screen
    return
