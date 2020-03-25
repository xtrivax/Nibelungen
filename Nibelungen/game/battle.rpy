define battle_narrator = Character(None, interact=False)

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
                    if players_turn and each_enemy_member.hp > 0:
                        textbutton "Attack ->" action Return(i) yminimum 75
                    else:
                        textbutton "Attack ->" action None yminimum 75
                    
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
    # is described by a dictionary.
    #
    $ testmc = Char("Main Character", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
    #$ party_list =[{"name":"MC", "maxhp":30, "hp":30, "maxmp":30, "mp":30, "min_damage":5, "max_damage":6}]
    $ party_list =[testmc]
    $ potions_left = 10
    $ players_turn = False
    
    #### Enemies list will have the description for enemies.
    #
    $ enemies_list = []
    
    scene black
    
    #### Let's show the game screen.
    #
    show screen battle_screen
    
    
    #### We can add some allies to the party:
    #
    menu:
        "Who do you take with you?"
        
        "Friend 1":
            $ testf1 = Char("Testfriend", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
            $ party_list.append (testf1)
        "Friend 2":
            $ testf2 = Char("Testfriend2", 5, 604, 210, 504, 359, 419, 279, [slash], [], 0, 0)
            $ party_list.append (testf2)

        "Noone... :(":
            pass
            
    
    #### Enemies party can be set manually or automatically like:
    #
    python:
        testenemy1 = Char("Goblin", 5, 274, 1, 185, 80, 152, 80, [], [], 0, 5)
        testenemy2 = Char("Hobgoblin", 5, 354, 1, 284, 149, 209, 152, [], [], 0, 10)
        testenemy3 = Char("Slime", 5, 304, 1, 80, 125, 180, 200, [], [], 0, 5)
        enemies=[testenemy1,testenemy2,testenemy3]
        for i in enemies:
            enemies_list.append (i)
            
    
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
                
                else:
                    $ player_damage = current_player.generate_damage()
                    $ enemies_list[res].hp -= player_damage
                    "Take this! (damage dealt - [player_damage]hp)"
                    
            
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
                
                $ party_member_to_attack.hp -= enemy_damage
                
                "Rrrrr! ([current_enemy.name] dealt [enemy_damage]hp damage to [party_member_to_attack.name])"
                
            
            #### And the turn goes to the next party member.
            #
            $ enemy_index += 1
            
            
        #### Next round of the battle.
        #
        jump battle_2_loop
            
            
#### The results of the game.
#
label battle_2_win:
    "Well done!"
    hide screen battle_screen
    return
    
label battle_2_lose:
    "X_X"
    hide screen battle_screen
    return