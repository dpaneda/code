#!/usr/bin/python
#
# This code was created by Richard Campbell '99 (ported to Python/PyOpenGL by John Ferguson 2000)
#
# The port was based on the PyOpenGL tutorial module: dots.py  
#
# If you've found this code useful, please let me know (email John Ferguson at hakuin@voicenet.com).
#
# See original source and C based tutorial at http://nehe.gamedev.net
#
# Note:
# -----
# This code is not a good example of Python and using OO techniques.  It is a simple and direct
# exposition of how to use the Open GL API in Python via the PyOpenGL package.  It also uses GLUT,
# which in my opinion is a high quality library in that it makes my work simpler.  Due to using
# these APIs, this code is more like a C program using function based programming (which Python
# is in fact based upon, note the use of closures and lambda) than a "good" OO program.
#
# To run this code get and install OpenGL, GLUT, PyOpenGL (see http://www.python.org), and PyNumeric.
# Installing PyNumeric means having a C compiler that is configured properly, or so I found.  For 
# Win32 this assumes VC++, I poked through the setup.py for Numeric, and chased through disutils code
# and noticed what seemed to be hard coded preferences for VC++ in the case of a Win32 OS.  However,
# I am new to Python and know little about disutils, so I may just be not using it right.
#
# BTW, since this is Python make sure you use tabs or spaces to indent, I had numerous problems since I 
# was using editors that were not sensitive to Python.
#
# Modified on May 2nd,2004 by Travis Wells to fix some GLUT issues and missing import
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

triangle = { 'x':0.0, 'y':0.0, 'z':-12, \
	'rotx':0.0, 'roty':10.0, 'rotz':0.0 }
keys = { 'up':0, 'down':0, 'left':0, 'right':0 }
acel = { 'x':0, 'y':0 }

# A general OpenGL initialization function.  Sets all of the initial parameters. 
#def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
#    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
#    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
#    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
#    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
#    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	
#    glMatrixMode(GL_PROJECTION)
#    glLoadIdentity()					# Reset The Projection Matrix
#										# Calculate The Aspect Ratio Of The Window
#    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

#    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def DrawGLScene():
	global triangle
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View 

	# Move Left 1.5 units and into the screen 6.0 units.
	#glTranslatef(-1.5, 0.0, -6.0)
	glTranslatef(triangle['x'],triangle['y'],triangle['z'])
	glRotatef(triangle['roty'], 0.0, 1.0, 0.0)

	# Draw a triangle
	glBegin(GL_TRIANGLES)

	glColor3f(0.0, 1.0, 0.0)           
	glVertex3f(0.0, 1.0, 0.0)           
	glVertex3f(-1.0, -1.0, 1.0)          
	glVertex3f(1.0, -1.0, 1.0)         

	glColor3f(1.0, 0.0, 0.0)          
	glVertex3f(0.0, 1.0, 0.0)           
	glVertex3f(1.0, -1.0, 1.0)          
	glVertex3f(1.0, -1.0, -1.0)         

	glColor3f(0.0, 0.0, 1.0)         
	glVertex3f(0.0, 1.0, 0.0)           
	glVertex3f(1.0, -1.0, -1.0)          
	glVertex3f(-1.0, -1.0, -1.0)         

	glColor3f(0.0, 0.5, 1.0)         
	glVertex3f(0.0, 1.0, 0.0)           
	glVertex3f(-1.0, -1.0, -1.0)          
	glVertex3f(-1.0, -1.0, 1.0)         

	glEnd()                             # We are done with the polygon

	triangle['roty'] += 0.2

	#  since this is double buffered, swap the buffers to display what just got drawn. 
	glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    global keys
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
	    glutDestroyWindow(window)
	    sys.exit()
    if args[0] == 'w':
	keys['up'] = 1
    if args[0] == 's':
	keys['down'] = 1
    if args[0] == 'a':
	keys['left'] = 1
    if args[0] == 'd':
	keys['right'] = 1

def keyPressedUp(*args):
    global keys
    if args[0] == 'w':
	keys['up'] = 0
    if args[0] == 's':
	keys['down'] = 0
    if args[0] == 'a':
	keys['left'] = 0
    if args[0] == 'd':
	keys['right'] = 0


def timeMachine(a):
	global triangle,keys,acel

	acel['y'] += keys['up'] / 1000.0
	acel['y'] -= keys['down'] / 1000.0 
	acel['x'] -= keys['left'] / 1000.0 
	acel['x'] += keys['right'] / 1000.0 

	triangle['x'] += acel['x']; 
	triangle['y'] += acel['y']; 

	movement = keys['up'] + keys['down'] +  keys['left'] + keys['right'];
	if (not movement):
		acel['x'] *= 0.98
		acel['y'] *= 0.98

	DrawGLScene();	
	glutTimerFunc(5, timeMachine,0)


def main():
	global window
	# For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
	# Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
	glutInit(())

	# Select type of Display mode:   
	#  Double buffer 
	#  RGBA color
	# Alpha components supported 
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glEnable(GL_CULL_FACE)
	
	# get a 640 x 480 window 
	glutInitWindowSize(1024, 768)
	
	# the window starts at the upper left corner of the screen 
	glutInitWindowPosition(200, 100)
	
	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("No me cierres que me ofendo!!")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.	
	glutDisplayFunc (DrawGLScene)
	
	#glutFullScreen()

	glutReshapeFunc (ReSizeGLScene)

	glutKeyboardFunc (keyPressed)
	glutKeyboardUpFunc (keyPressedUp)

	glutTimerFunc(100, timeMachine,0)
	glutIgnoreKeyRepeat(1)

	# Initialize our window. 
	#InitGL(640, 480)

	# Start Event Processing Engine	
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print "Hit ESC key to quit."
main()
    	
