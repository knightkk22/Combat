import arcade
import random
import os
import time

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.975 # NOTE: Set Slightly Below 1.0 to Prevent Unwanted Side Effects
SPRITE_SCALING_INVADER = 0.975 # NOTE: Set Slightly Below 1.0 to Prevent Unwanted Side Effects
MOVEMENT_SPEED = 5 # Used With Keyboard
MOVEMENT_MULTIPLIER = 5 # Used With Joystick
DEAD_ZONE = 0.05 # Joystick Related Constant (See Arcade Documentation Regarding Joysticks)
LAZER_SPEED = 7
DEATH_RAY_SPEED = 4

class Lazer(arcade.Sprite):
    def update(self):
        self.center_y += LAZER_SPEED

class DeathRay(arcade.Sprite):
    def update(self):
        self.center_y -= DEATH_RAY_SPEED

class Invader(arcade.Sprite):
    def __init__(self, imageFilenameA, imageFilenameB):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        self.texture_left = arcade.load_texture(imageFilenameA, scale=0.975)
        self.texture_right = arcade.load_texture(imageFilenameB, scale=0.975)

        # By default, face right.
        self.texture = self.texture_left

        # current direction (facing either "left" or "right")
        self.facing = "left"

class Defender(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture_standard = arcade.load_texture("Defender.png", scale=0.975)
        self.texture_hidden = arcade.load_texture("HiddenDefender.png", scale=0.975)
        self.texture = self.texture_standard
        self.hidden = False

    def flash(self):
        if self.hidden == False:
            self.texture = self.texture_hidden
            self.hidden = True
        else:
            self.texture = self.texture_standard
            self.hidden = False

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True, resizable=True)

        # Add Joystick
        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick.on_joybutton_press = self.on_joybutton_press
            self.joystick.on_joybutton_release = self.on_joybutton_release
            self.joystick.on_joyhat_motion = self.on_joyhat_motion
        else:
            print("There are no Joysticks")
            self.joystick = None

        # Set Background Color
        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None
        '''
        self.defender_list = None
        self.invader_list = None
        self.lazer_list = None
        self.death_ray_list = None
        self.shield_list = None
        '''

        # Set up the player info
        '''
        self.defender_sprite = None
        '''

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Debugging Variable
        self.iteration = 0

        # Create Game State Variables
        '''
        self.invaderDirection = "left"
        self.bottom_invader_y_position = 99999999
        '''

        # Get Full Screen Width & Height
        self.FULL_SCREEN_WIDTH, self.FULL_SCREEN_HEIGHT = self.get_size()
        self.CENTER_X =  self.FULL_SCREEN_WIDTH / 2
        self.CENTER_Y =  self.FULL_SCREEN_HEIGHT / 2
        self.LEFT_BOUNDARY_X = self.CENTER_X - (self.CENTER_X * 0.5)
        self.RIGHT_BOUNDARY_X = self.CENTER_X + (self.CENTER_X * 0.5)

        self.leftButtonDown = False
        self.rightButtonDown = False

        '''
        self.invader_speed = 1
        self.invader_advancements = 0
        self.pause = False
        self.flash = False
        self.flashCount = -1
        self.lives = 3
        '''

    def setup(self):
        # Create Sprite Lists
        '''
        self.defender_list = arcade.SpriteList()
        self.invader_list = arcade.SpriteList()
        '''
        print("on button press")

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        '''
        # Call draw() on all your sprite lists below
        self.defender_list.draw()
        self.invader_list.draw()
        self.lazer_list.draw()
        self.shield_list.draw()
        self.death_ray_list.draw()
        '''
        print("on button press")

    def update(self, delta_time):
        # do stuff
        print("on update")

    def on_key_press(self, key, key_modifiers):
        # EXIT FULL SCREEN WHEN ESCAPE KEY IS PRESSED
        if key == arcade.key.ESCAPE:
            self.is_full_screen = False
            self.set_fullscreen(self.is_full_screen)
            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)
            print("on button press")
        # MOVE DEFENDER WHEN LEFT KEY IS PRESSED
        elif key == arcade.key.LEFT:
            '''
            self.defender_sprite.change_x = -MOVEMENT_SPEED
            self.leftButtonDown = True
            '''
            print("on button press")
        # MOVE DEFENDER WHEN RIGHT KEY IS PRESSED
        elif key == arcade.key.RIGHT:
            '''
            self.defender_sprite.change_x = MOVEMENT_SPEED
            self.rightButtonDown = True
            '''
            print("on button press")
        elif key == arcade.key.SPACE:
            # If there are no other lazer beams currently on screen, then fire.
            '''
            if len(self.lazer_list) == 0:
                # Instantiate Lazer
                lazer = Lazer("Lazer.png", 0.975)
                # Position Lazer Beam
                lazer.center_x = self.defender_sprite.center_x
                lazer.bottom = self.defender_sprite.top
                # Add Lazer Beam to lazer_list
                self.lazer_list.append(lazer)
             '''
            print("on button press")


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        '''
        if key == arcade.key.LEFT:
            if self.rightButtonDown == False:
                self.defender_sprite.change_x = 0
            self.leftButtonDown = False
        elif key == arcade.key.RIGHT:
            if self.leftButtonDown == False:
                self.defender_sprite.change_x = 0
            self.rightButtonDown = False
        '''

    def on_joybutton_press(self, joystick, button):
        # If there are no other lazer beams currently on screen, then fire.
        '''
        if len(self.lazer_list) == 0:
            # Instantiate Lazer
            lazer = Lazer("Lazer.png", 0.975)
            # Position Lazer Beam
            lazer.center_x = self.defender_sprite.center_x
            lazer.bottom = self.defender_sprite.top
            # Add Lazer Beam to lazer_list
            self.lazer_list.append(lazer)
        '''
        print("on button press")



    def on_joybutton_release(self, joystick, button):
        print("Button {} up".format(button))

    def on_joyhat_motion(self, joystick, hat_x, hat_y):
        print("Hat ({}, {})".format(hat_x, hat_y))


def main():
    """ Main method """
    game = MyGame()
    game.setup()
    arcade.run()

# RUN GAME
main()
