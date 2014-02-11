# import lib stuff
import pyglet
from pyglet.window import key
from pyglet.gl import *
from pyglet.window import mouse

# import other stuff
from bird import *
from sprites import *

# set up screen transitioning
titleScreenMode = True
highScoreScreenMode = False
gamePlayScreenMode = False
gameOverScreenMode = False
instructionsScreenMode = False
pause = False

def changeState(state):
    global titleScreenMode
    global highScoreScreenMode
    global gamePlayScreenMode
    global gameOverScreenMode
    global instructionsScreenMode
    global bird_sprite

    if(state == 'title'):
	titleScreenMode = True
        highScoreScreenMode = False
        gamePlayScreenMode = False
        gameOverScreenMode = False
	instructionsScreenMode = False
    if(state == 'highscores'):
	titleScreenMode = False
        highScoreScreenMode = True
        gamePlayScreenMode = False
        gameOverScreenMode = False
	instructionsScreenMode = False
    if(state == 'gameplay'):
	titleScreenMode = False
        highScoreScreenMode = False
        gamePlayScreenMode = True
        gameOverScreenMode = False
	instructionsScreenMode = False
    if(state == 'gameover'):
	titleScreenMode = False
        highScoreScreenMode = False
        gamePlayScreenMode = False
        gameOverScreenMode = True
	instructionsScreenMode = False
    if(state == 'instructions'):
	titleScreenMode = False
        highScoreScreenMode = False
        gamePlayScreenMode = False
        gameOverScreenMode = False
	instructionsScreenMode = True

# Set up the current state as the title screen
changeState('title')

# Set up buffer variables
bufferedHeight = 256
bufferedWidth = 144

# Scale resolution
glScalef(1.0, 1.0, 1.0)

# Create the window
window = pyglet.window.Window(bufferedWidth, bufferedHeight, resizable=True)

# Handle the keypress
@window.event
def on_key_release(symbol, modifiers):
    global titleScreenMode
    global highScoreScreenMode
    global gamePlayScreenMode
    global gameOverScreenMode
    global instructionsScreenMode
    global player

    if symbol == key.SPACE:
        print 'The SPACE key was pressed.'
	player.jump()
        player.acc = 0
    if symbol == key.PAGEUP:
        glScalef(2.0, 2.0, 2.0)
	window.set_size(window.width * 2, window.height * 2)
    if symbol == key.PAGEDOWN:
        glScalef(0.5, 0.5, 0.5)
	window.set_size(window.width / 2 , window.height /2)

# Handle mouse presses
@window.event
def on_mouse_release(x, y, button, modifiers):
    global titleScreenMode
    global highScoreScreenMode
    global gamePlayScreenMode
    global gameOverScreenMode
    global instructionsScreenMode

    if button == mouse.LEFT:
        print 'The left mouse button was pressed at %d, %d' % (x, y)
	
	""" Add logic for switching game states """
	if(instructionsScreenMode):
	    changeState('gameplay')
	    print "Changed to gameplay screen"
	    pyglet.clock.schedule_interval(player.bounce_player, .05)
	if(titleScreenMode):
	    # Play button logic
	    if(x > 21 and x < 60 and y > 63 and y < 75):
		changeState('instructions')
		print "Changed to instuctions screen"
	    # Score button logic
	    if(x > 80 and x < 119 and y > 63 and y < 75):
	        changeState('highscores')
		print "Changed to highscores screen"
        if(gamePlayScreenMode):
	   pyglet.clock.unschedule(player.gravity)
	   pyglet.clock.schedule_interval(player.gravity, .05)
	   pyglet.clock.unschedule(player.bounce_player)
        if(gameOverScreenMode):
	   pass
        if(highScoreScreenMode):
	   pass

# Grab fps count
fps_display = pyglet.clock.ClockDisplay()

# Create the player object
player = Bird(bird_animation, 41, 120)

# Handle the drawing
@window.event
def on_draw():
    global titleScreenMode
    global highScoreScreenMode
    global gamePlayScreenMode
    global gameOverScreenMode
    global instructionsScreenMode
	
    # Clear the window
    window.clear()
    
    # The following two lines will change how textures are scaled.
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    
    # Draw the title screen if nessecary
    if(titleScreenMode):
    	title_sprite.draw()
	flappybird_sprite.draw()
	bird_sprite.draw()
	ground_sprite.draw()

    # Draw the gameplay screen if nessecary
    if(gamePlayScreenMode):
    	background_sprite.draw()
        player.draw()
	player.draw_score()
	# Make sure bird dies when it hits the ground
	if(player.y <= 60):
            player.image = middleflap_image
        else:
            ground_sprite.draw()

    # Draw the highscore screen if nessecary
    if(highScoreScreenMode):
    	pass

    # Draw the gameover screen if nessecary
    if(gameOverScreenMode):
    	pass
    
    # Draw the instructions screen if nessecary
    if(instructionsScreenMode):
    	instructions_sprite.draw()
	bird_sprite2.draw()
	ground_sprite.draw()

    fps_display.draw()
