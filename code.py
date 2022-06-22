#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my CPT game for the edgebadge




import constants
import time
import random
import stage
import ugame
import supervisor


def splash_scene():
    # this function is the main game scene

    # set a var to hold the soumd
    coin_sound = open("sounds/coin.wav", "rb")

    # accesses audio library
    sound = ugame.audio

    # Stops sound from playing
    sound.stop()

    # Ensures unmuted
    sound.mute(False)

    # Plays the coin sound at the beginning of the splash screen
    sound.play(coin_sound)

    # accesses the image bank and setting it to a variable st index 0
    image_bank_mt_background = stage.Bank.from_bmp16("images/mt_game_studio.bmp")

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # creates the 10 by 8 image grid, sets it to background
    # this allows us to knit together an image
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # used this program to split the image into tile:

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [background]

    # takes layers and shows them on the screen
    game.render_block()

    # this is the game loop so it is supposed to loop forever
    while True:
        # wait for two seconds
        time.sleep(2.0)

        # goes to the menu
        menu_scene()


def menu_scene():
    # his function is the main game scene

    # accesses audio library
    sound = ugame.audio

    # Stops sound from playing
    sound.stop()

    # Ensures unmuted
    sound.mute(False)

    # accesses the image bank and setting it to a variable st index 0
    image_bank_mt_background = stage.Bank.from_bmp16("images/mt_game_studio.bmp")

    # new variable called text set to list
    text = []

    # variable makes a piece of text // pallette selects the color
    name_text = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    name_text.move(5, 10)

    # What the text is going to say
    name_text.text("DE MEO GAME STUDIOS")

    # adds it to the list
    text.append(name_text)

    # making another text object
    mute_text = stage.Text(width = 29, height = 12, font = None, palette = constants.RED_PALETTE, buffer = None)

    # moves the cursor to this location
    mute_text.move(15, 60)

    # what the text will say
    mute_text.text("Press B to mute")

    # add to text list
    text.append(mute_text)

    # making another text object
    start_text = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    start_text.move(35, 110)

    # What the text will say
    start_text.text("PRESS START!")

    # making another text object
    muted_text = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    muted_text.move(constants.SCREEN_X, 75)

    # What the text will say
    muted_text.text("Muted!")


    # adding to text list
    text.append(start_text)

    # creating the B button
    b_button = constants.button_state["button_up"]

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = text + [muted_text] + [background]

    # takes layers and shows them on the screen
    game.render_block()

    # checks to see if sound is muted
    is_muted = False

    # this is the game loop so it is supposed to loop forever
    while True:
        # Get user input
        # getting the buttons that are pressed - 60 times a second
        keys = ugame.buttons.get_pressed()

        # The if statements decide what to do when a button is pressed
        if keys & ugame.K_START:
            print("Start")
            game_scene(is_muted)

        if keys & ugame.K_X != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"] 
        
        if b_button == constants.button_state["button_just_pressed"]:
            if is_muted == True:
                is_muted = False
                muted_text.move(constants.SCREEN_X, 75)
                game.render_block()
            elif is_muted == False:
                is_muted = True
                muted_text.move(60, 75)
                game.render_block()
                


        # wait until the specified 60th of a second is reached
        game.tick()


def game_scene(mute):
    # this function is the main game scene

    def create_pipe():
        amount_of_pipes = random.randint(0, 3)
        rest_of_pipes = 3 - amount_of_pipes
        counter = 0


        for pipe in range(amount_of_pipes):
            
            middle_pipes[pipe].move(constants.SCREEN_X, counter * 16)
            counter += 1
        
        top_pipe.move(constants.SCREEN_X, counter * 16)
        # added 4 to account for the empty space that the sprite 
        counter += 4
        bottom_pipe.move(constants.SCREEN_X, counter * 16)
        counter +=1

        for pipe2 in range(rest_of_pipes):
            if pipe2 + amount_of_pipes < 3:
                middle_pipes[pipe2 + amount_of_pipes].move(constants.SCREEN_X, counter * 16)
                counter += 1
        

    # to keep track of score
    score = 0

    # creates the text cursor
    score_text = stage.Text(width = 29, height = 14)

    # clears the text from previous game
    score_text.clear()

    # sets the cursor to screen
    score_text.cursor(0, 0)

    # moves the cursor to this point
    score_text.move(1, 1)

    # sets what the text will say
    score_text.text("Score: {0}".format(score))

    # accesses the image bank and setting it to a variable st index 0
    image_bank_background = stage.Bank.from_bmp16("images/space_aliens_background.bmp")

    # sets up a new image bank, this one for the sprites
    image_bank_sprites = stage.Bank.from_bmp16("images/space_aliens.bmp")

    # Making the A button
    a_button = constants.button_state["button_up"]

    # The next portion is to set up the sound
    # this sets a variable to the wav file that holds the sound
    pew_sound = open("sounds/pew.wav", "rb")

    boom_sound = open("sounds/boom.wav", 'rb')

    crash_sound = open("sounds/crash.wav", 'rb')

    # uses the audio library in ugame
    sound = ugame.audio

    # makes sure there is no sound in the beginning
    sound.stop()

    # Sets whether the sound is muted or not depending on what was selected on the screen
    if mute == True:
        # mutes sound
        sound.mute(True)
    elif mute == False:
        #unmutes sound
        sound.mute(False)

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # This loop creates a random background with the tiles
    # first for loop goes through the x axis
    for x_location in range(constants.SCREEN_GRID_X):
        # this loop goes through the y axis
        for y_location in range(constants.SCREEN_GRID_Y):
            if y_location > 5:
                tile_picked = random.randint(11, 12)
            else:
                # picks a random tile from the background
                tile_picked = random.randint(13, 15)

            # places tile at the specified location
            background.tile(x_location, y_location, tile_picked)

    # creates the bird sprite and sets it to the index 5 of the sprite list
    # puts it to the middle on the screen
    bird  = stage.Sprite(image_bank_sprites, 5, int((constants.SCREEN_X / 2) - (constants.SPRITE_SIZE / 2)), int(constants.SCREEN_Y / 2))

    # holds pipes
 
    middle_pipes = []

    # creates all the necessary sprites for the bottom portion of the opening
    bottom_pipe = stage.Sprite(image_bank_sprites, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

    # bottom_pipe2 = stage.Sprite(image_bank_sprites, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    # bottom_pipes.append(bottom_pipe2)
    # bottom_pipe3 = stage.Sprite(image_bank_sprites, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    # bottom_pipes.append(bottom_pipe3)

    # creates all the necessary sprites for the top portion of the opening
    top_pipe = stage.Sprite(image_bank_sprites, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    # top_pipe2 = stage.Sprite(image_bank_sprites, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    # top_pipes.append(top_pipe2)
    # top_pipe3 = stage.Sprite(image_bank_sprites, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    # top_pipes.append(top_pipe3)

    # creates all the necessary sprites for the middle portion of the pipes
    middle_pipe1 = stage.Sprite(image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    middle_pipes.append(middle_pipe1)
    middle_pipe2 = stage.Sprite(image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    middle_pipes.append(middle_pipe2)
    middle_pipe3 = stage.Sprite(image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    middle_pipes.append(middle_pipe3)
    middle_pipe4 = stage.Sprite(image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    middle_pipes.append(middle_pipe4)
    

    # initialization of the gravity feature
    # set to -1 to give user some time to react
    gravity = -1

    # calls a funcction that will create a pipe
    create_pipe()

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [score_text] + [bird] + [top_pipe] + [bottom_pipe] + middle_pipes + [background]

    # takes layers and shows them on the screen
    game.render_block()

    while True:
        # checks to see if keys are pressed
        keys = ugame.buttons.get_pressed()

        # this updates the state of the A button
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"] 
        
        # checks to see if A button was pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # updates gravity so that it goes up the screen
            gravity = -3

            # plays sound
            sound.play(pew_sound)
        
        # adds speed every frame to gravity to make it more realistic, as if the bird was on earth 
        gravity += 0.2

        # moves bird with the gravity
        bird.move(bird.x, bird.y + gravity)

        # checks to see if bird is past the top of the screen
        if bird.y < 0:
            # keeps bird from going past the top
            bird.move(bird.x, 0)

        # checks to see if bird hits bottom of screen
        if bird.y > constants.SCREEN_Y - 14:
            # plays sound
            sound.play(crash_sound)

            # wait 0.5 seconds
            time.sleep(0.5)

            # calls the game over scene because the bird has crashed
            game_over_scene(score)
        
        # this loop is used to move the filler pipes at the top and bottom of screen
        for pipe3 in middle_pipes:
            if pipe3.x > (-1 *constants.SPRITE_SIZE):
                # moves the pipe across the screen
                pipe3.move(pipe3.x - 1.5, pipe3.y)
            else:
                # if the pipe is past the edge, it will move the pipe to its idle position
                pipe3.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # this is to move the top pipe opening piece across screen
        if top_pipe.x > (-1 * constants.SPRITE_SIZE):
            # moves pipe across screen
            top_pipe.move(top_pipe.x - 1.5, top_pipe.y)
        else:
            # if pipe is past screen move to its idle position
            top_pipe.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        
        if bottom_pipe.x > (-1 * constants.SPRITE_SIZE):
            bottom_pipe.move(bottom_pipe.x - 1.5, bottom_pipe.y)
        else:
            # if the pipe is past the edge, it will move the pipe to its idle position
            bottom_pipe.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

            # creates a new pipe at the right side of the screen
            create_pipe()
        
        # if the pipe makes it past the bird without crashing, add 1 to score
        if top_pipe.x == (constants.SCREEN_X / 4):
            score += 1
            # clears the text from previous game
            score_text.clear()

            # sets the cursor to screen
            score_text.cursor(0, 0)

            # moves the cursor to this point
            score_text.move(1, 1)

            # sets what the text will say
            score_text.text("Score: {0}".format(score))

        # this is the collision detection for the top pipe and the bird. Includes all filler pipes above the top pipe
        if stage.collide(bird.x, bird.y + 2, bird.x + constants.SPRITE_SIZE, bird.y +14, top_pipe.x + 1, top_pipe.y - constants.SCREEN_Y, top_pipe.x + 16, top_pipe.y + 16):
            sound.play(crash_sound)
            time.sleep(0.5)
            # goes to the game over screen
            game_over_scene(score)
        
        # this is the collisiont detection for the bottom pipe and the bird. Includes all filler pipes below the bottom pipe
        if stage.collide(bird.x, bird.y + 2, bird.x + constants.SPRITE_SIZE, bird.y +14, bottom_pipe.x + 1, bottom_pipe.y, bottom_pipe.x + 16, bottom_pipe.y + constants.SCREEN_Y):
            sound.play(crash_sound)
            time.sleep(0.5)
            # goes to the game over screen
            game_over_scene(score)
            
        
            
        game.render_sprites([bird] + [bottom_pipe] + [top_pipe] + middle_pipes)

        game.tick()  # ensures specified time is met before next frame

def game_over_scene(final_score):

    # creates the imgae bank
    image_bank_2 = stage.Bank.from_bmp16("images/mt_game_studio.bmp")

    # sets the new background for the game over scene
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # Making a text variable
    text = []

    # creates the text cursor
    final_score_text = stage.Text(width = 29, height = 14, font = None, palette = constants.RED_PALETTE, buffer = None)
    
    # moves the text 
    final_score_text.move(22, 20)

    # what the text will say
    final_score_text.text("Final Score: {:0>2d}".format(final_score))

    # append to text list
    text.append(final_score_text)

    # creates the game over text
    game_over_text = stage.Text(width = 29, height = 14, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move the cursor
    game_over_text.move(43, 60)

    # what the text will say
    game_over_text.text("GAME OVER")

    # add to texts list
    text.append(game_over_text)

    # making select text
    select_text = stage.Text(width = 29, height = 14, font = None, palette = constants.RED_PALETTE, buffer = None)

    # move the cursor
    select_text.move(32, 110)

    # what the text will say
    select_text.text("PRESS SELECT")

    # add to text list
    text.append(select_text)

    # creating the stage and layers for the background and foreground to show up on
    game = stage.Stage(ugame.display, constants.FPS)

    # This is setting the layers so the items show up in order
    game.layers = text + [background]

    # render the backgroynd and location of texts
    game.render_block()

    # game loop
    while True:
        # looking for user input
        keys = ugame.buttons.get_pressed()

        # If select button is pressed
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # updating the game
        game.tick()  # waiting until refresh rate finishes



if __name__ == "__main__":
    splash_scene()
                                                     