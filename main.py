import flet as ft 
from random import randint

def main(page: ft.Page):
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_full_screen = True

    # --Class to Contain Gameplay Events--
    class event:
        def exit(e):                                                # A function to exit the app. Used by the exit button.
            page.window_close()

        def spawn_bombs():                                          # We daclare a function to spawn bombs in a random
            tile = content.game_screen.tile                         # way. I tested a number of algorithms before landing
            for i in range(tile.__len__()):                         # on y=i*(i%3). Truthfully, I don't understand why
                y = i*(i%3)                                         # this one works since I landed on it by trial and
                x = randint(0,y)                                    # error. It does, however, work and does it
                if x > i:                                           # exceptionally well. This function needs to be called
                    tile[i].data['bomb'] = True                     # at the end of our main function after page.add()
            page.update()                                           # and before page.update().

        def reset(e):                                               # We declare a function to clean the gameplay window 
            page.clean()                                            # and then spawn a new one. 
            tile = content.game_screen.tile
            for i in range(tile.__len__()):                         # We need to reset data, content, and bgcolor
                tile[i].data['bomb'] = False                        # attributes. 
                tile[i].data['selected'] = False 
                tile[i].content = None 
                tile[i].bgcolor = ft.colors.BLUE_GREY
            page.add(                                               # Since we cleaned the page to remove the previous 
                content.game_screen.main,                           # game we use page.add() to reset page controls.
                btn.reset,
                btn.exit 
            )
            event.spawn_bombs()                                     # And finally we call event.spawn_bombs() to complete 
                                                                    # the function. 
            
        def bomb_pass(c):                                           #------------------------------------#
            print('Bomb sweep initiated...')                        # This function handles the sweep effect. It's called
            tile = content.game_screen.tile                         # within and is nearly identical to bomb_check() 
            selTiles = 0                                            # except that it recurses until no more nearby bombs
            bombs = 0                                               # can be found.
            for i in range(tile.__len__()):
                if tile[i].data['selected'] == True:                # We declare an algorithm to check the entire game 
                    selTiles += 1                                   # board for selected tiles and bombs. If they are
                if tile[i].data['bomb'] == True:                    # found we increment the corresponding variable by 1.
                    bombs += 1
            if selTiles + bombs == tile.__len__():                  # Here we check if all non bomb tiles have been
                page.controls.clear()                               # selected. If they have then the game is ended and 
                page.controls.append(ft.Text(value='You win!'))     # the game window is replaced with "You Win!" 
                page.controls.append(btn.reset)
                page.controls.append(btn.exit)
            if tile[c.key].data['selected'] == True:                # Here we need to declare an if statement to prevent
                return                                              # infinite recursion by checking the current index of
                                                                    # tile for a "selected" value of True.
            nearby = 0
            c.data['selected'] = True                               # Set "selected" for the current tile index to True
            c.bgcolor = None                                        
            s1 = c.key+1 if c.key+1 < 99 else c.key                 # A simple algorithm to grab the tile keys of nearby
            s2 = c.key-1 if c.key-1 > 0 else c.key                  # tiles. 
            s3 = c.key+10 if c.key+10 < 99 else c.key 
            s4 = c.key-10 if c.key-10 > 0 else c.key
            s5 = c.key+11 if c.key+11 < 99 else c.key
            s6 = c.key-11 if c.key-11 > 0 else c.key
            s7 = c.key+9 if c.key+9 < 99 else c.key 
            s8 = c.key-9 if c.key-9 > 0 else c.key
            if s1 == c.key:
                pass 
            else:
                if tile[s1].data['bomb'] == True:                   # as the algorithm continues through a set of
                        nearby += 1                                 # conditional statements it updates the variable
            if s2 == c.key:                                         # 'nearby' which is an int representing the number of
                pass                                                # nearby bombs.
            else:
                if tile[s2].data['bomb'] == True and s2 > 0:
                    nearby += 1
            if s3 == c.key:
                pass
            else:
                if tile[s3].data['bomb'] == True and s3 < 99:
                    nearby += 1
            if s4 == c.key:
                pass
            else:
                if tile[s4].data['bomb'] == True and s4 > 0:
                    nearby += 1
            if s5 == c.key:
                pass
            else:
                if tile[s5].data['bomb'] == True and s5 < 99:
                    nearby += 1
            if s6 == c.key:
                pass
            else:
                if tile[s6].data['bomb'] == True and s6 > 0:
                    nearby += 1
            if s7 == c.key:
                pass
            else:
                if tile[s7].data['bomb'] == True and s7 < 99:
                    nearby += 1
            if s8 == c.key:
                pass
            else:
                if tile[s8].data['bomb'] == True and s8 > 0:
                    nearby += 1
            if nearby > 0:                                          # Finally if nearby is greater than 0 we update the
                c.content = ft.Text(value=nearby,color='black')     # content attribute of the current tile index so that
                if tile[s1].data['bomb'] == False:                  # it displays the number of nearby bombs.
                    if tile[s1].data['selected'] == False:
                        print(tile[s1].data['selected'])
                        event.bomb_pass(c=tile[s1])
                else:
                    pass
                if tile[s2].data['bomb'] == False:                  # we have to do this for all nearby tiles as 
                    if tile[s1].data['selected'] == False:          # represented by the variable 's[int]'
                        print(tile[s2].data['selected'])
                        event.bomb_pass(c=tile[s2])
                else:
                    pass
                if tile[s3].data['bomb'] == False:
                    if tile[s1].data['selected'] == False:
                        print(tile[s3].data['selected'])
                        event.bomb_pass(c=tile[s3])
                else:
                    pass
                if tile[s4].data['bomb'] == False:
                    if tile[s1].data['selected'] == False:
                        print(tile[s4].data['selected'])
                        event.bomb_pass(c=tile[s4])
                else:
                    pass
                if tile[s5].data['bomb'] == False:
                    if tile[s1].data['selected'] == False:
                        print(tile[s5].data['selected'])
                        event.bomb_pass(c=tile[s5])
                else:
                    pass
                if tile[s6].data['bomb'] == False:
                    if tile[s1].data['selected'] == False:
                        print(tile[s6].data['selected'])
                        event.bomb_pass(c=tile[s6])
                else:
                    pass
                if tile[s7].data['bomb'] == False:
                    if tile[s1].data['selected'] == False:
                        print(tile[s7].data['selected'])
                        event.bomb_pass(c=tile[s7])
                else:
                    pass
                if tile[s8].data['bomb'] == False:
                    if tile[s1].data['selected'] == False:
                        print(tile[s8].data['selected'])
                        event.bomb_pass(c=tile[s8])
                else:
                    pass
                page.update()
        
        def bomb_check(e):
            print('Bomb check executed...')                         # Here we declare our initial bomb check. It's much
            tile = content.game_screen.tile                         # the same as bomb_pass() without the recursion aspect
            nearby = 0                                              # If e.control.data["bomb"] is True then you lose, 
            if e.control.data['bomb'] == True:                      # else display nearby bombs and enter bomb_pass()
                page.controls.clear()
                page.controls.append(ft.Text(value='YOU LOSE'))
                page.controls.append(btn.reset)
                page.controls.append(btn.exit)
            else:
                print('Bombs: None')
                e.control.data['selected'] = True
                e.control.bgcolor = None
                s1 = e.control.key+1 if e.control.key+1 < 99 else e.control.key
                s2 = e.control.key-1 if e.control.key-1 > 0 else e.control.key
                s3 = e.control.key+10 if e.control.key+10 < 99 else e.control.key
                s4 = e.control.key-10 if e.control.key-10 > 0 else e.control.key
                s5 = e.control.key+11 if e.control.key+11 < 99 else e.control.key
                s6 = e.control.key-11 if e.control.key-11 > 0 else e.control.key
                s7 = e.control.key+9 if e.control.key+9 < 99 else e.control.key
                s8 = e.control.key-9 if e.control.key-9 > 0 else e.control.key

                if s1 == e.control.key:
                    pass
                else:
                    if tile[s1].data['bomb'] == True:
                        nearby += 1
                if s2 == e.control.key:
                    pass
                else:
                    if tile[s2].data['bomb'] == True and s2 > 0:
                        nearby += 1
                if s3 == e.control.key:
                    pass
                else:
                    if tile[s3].data['bomb'] == True and s3 < 99:
                        nearby += 1
                if s4 == e.control.key:
                    pass
                else:
                    if tile[s4].data['bomb'] == True and s4 > 0:
                        nearby += 1
                if s5 == e.control.key:
                    pass
                else:
                    if tile[s5].data['bomb'] == True and s5 < 99:
                        nearby += 1
                if s6 == e.control.key:
                    pass
                else:
                    if tile[s6].data['bomb'] == True and s6 > 0:
                        nearby += 1
                if s7 == e.control.key:
                    pass
                else:
                    if tile[s7].data['bomb'] == True and s7 < 99:
                        nearby += 1
                if s8 == e.control.key:
                    pass
                else:
                    if tile[s8].data['bomb'] == True and s8 > 0:
                        nearby += 1

                if nearby > 0:
                    e.control.content = ft.Text(value=nearby,color='black')
                    if tile[s1].data['bomb'] == False:
                        event.bomb_pass(c=tile[s1])
                    if tile[s2].data['bomb'] == False:
                        event.bomb_pass(c=tile[s2])
                    if tile[s3].data['bomb'] == False:
                        event.bomb_pass(c=tile[s3])
                    if tile[s4].data['bomb'] == False:
                        event.bomb_pass(c=tile[s4])
                    if tile[s5].data['bomb'] == False:
                        event.bomb_pass(c=tile[s5])
                    if tile[s6].data['bomb'] == False:
                        event.bomb_pass(c=tile[s6])
                    if tile[s7].data['bomb'] == False:
                        event.bomb_pass(c=tile[s7])
                    if tile[s8].data['bomb'] == False:
                        event.bomb_pass(c=tile[s8])
            page.update()
                
    # --A Class To Store Buttons--
    class btn:
        reset = ft.ElevatedButton(
            text='RESET',
            on_click=event.reset
        )
        exit = ft.ElevatedButton(
            text='EXIT',
            on_click=event.exit
        )
    
    # --Interface Containers--
    class content:

        # --Main Gameplay Screen--
        class game_screen:

            # --Tiles and Rows--
            tile = [ft.Container() for x in range(100)]         #   We define our tiles and rows as lists populated with
            row = [ft.Row() for x in range(10)]                 #  their respective Flet objects using for loops.
            
            # --Tile Construction--
            for i in range(tile.__len__()):
                tile[i].width = 50                              #  Using a for loop we set the tile Container attributes.
                tile[i].height = 50                             # This could be accomplished within the tile definition
                tile[i].border = ft.border.all(1,'black')       # by passing them into the ft.Container parethesese, 
                tile[i].key = i                                 # however we'll also use the i variable to do some row
                tile[i].data = {                                # construction below so this is the best practice.
                    'bomb':False,
                    'selected':False,
                    'flagged':False
                }
                tile[i].bgcolor = ft.colors.BLUE_GREY
                tile[i].on_click = event.bomb_check
            
            # --Row Construction--
                if i >= 0 and i <= 9:                           #  We construct the rows beginning within the tile 
                    row[0].controls.append(tile[i])             # construction loop to make use of its i variable.
                elif i >= 10 and i <= 19:
                    row[1].controls.append(tile[i])             #  Using an if-elif-else statement we can assign
                elif i >= 20 and i <= 29:                       # the correct indexes of tile to their respective rows.
                    row[2].controls.append(tile[i])
                elif i >= 30 and i <= 39:
                    row[3].controls.append(tile[i])
                elif i >= 40 and i <= 49:
                    row[4].controls.append(tile[i])
                elif i >= 50 and i <= 59:
                    row[5].controls.append(tile[i])
                elif i >= 60 and i <= 69:
                    row[6].controls.append(tile[i])
                elif i >= 70 and i <= 79:
                    row[7].controls.append(tile[i])
                elif i >= 80 and i <= 89:
                    row[8].controls.append(tile[i])
                elif i >= 90 and i <= 99:
                    row[9].controls.append(tile[i])
            # --Row Construction Loop--
            for i in range(row.__len__()):                      # Here we use a new for loop to assign our row attributes.
                row[i].key = f'row-{i}'
                row[i].spacing = 0
                row[i].scroll = ft.ScrollMode.HIDDEN    # --note-- ScrollMode must be set to fix page.alignment bug.
            
            mainCol = ft.Column(                                # We create a Column Flet object to store our rows in a 
                controls=[                                      # central location.
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9]
                ],
                spacing=0,
                scroll=ft.ScrollMode.HIDDEN
            )
            main = ft.Container(
                content=mainCol,
                alignment= ft.alignment.center,
                margin=0,
                border_radius=25,
                bgcolor=ft.colors.BLUE_GREY_100,
                width=500
            )

    page.add(
        content.game_screen.main,
        btn.reset,
        btn.exit
    )

    event.spawn_bombs()
    # ---Display Bombs---
    # Uncomment the following to see bombs for dev purposes.
    # for i in range(content.game_screen.tile.__len__()):
    #     if content.game_screen.tile[i].data['bomb'] == True:
    #         content.game_screen.tile[i].content = ft.Text(value='B')
    page.update()

ft.app(target=main)