#!/usr/bin/python
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import pow,sqrt
import copy

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

class coord:
        def __init__(self,x,y,z):
                self.x = x
                self.y = y
                self.z = z

        def tuple(self):
                return (self.x,self.y,self.z)

        def __neg__(self):
                return coord (-self.x , -self.y , -self.z) 

        def __add__(self, other):
                return coord (self.x + other.x, self.y + other.y, self.z + other.z)

        def __sub__(self, other):
                return coord (self.x - other.x, self.y - other.y, self.z - other.z)

        def escalar_mul(self, k):
                return coord (self.x*k, self.y*k, self.z*k)

        def escalar_div(self, k):
                return coord (self.x/k, self.y/k, self.z/k)

        def dist(self, c):
                aux = c - self
                return sqrt(pow(aux.x,2) + pow(aux.y,2) + pow(aux.z,2))
			
        def mod(self):
                return self.dist(coord(0,0,0))

        def unitary(self):
                return self.escalar_div(self.mod())

class color:
	def __init__(self,color,alpha):
		self.color = color
		self.alpha = alpha

	def get_color(self):
		return (self.color.x,self.color.y,self.color.z,self.alpha)

class planet:
	def __init__(self, pos, radius=1, vel=coord(0,0,0), name="Unknown", mass=1):
	        self.pos = pos
		self.vel = vel
		self.radius = radius
		self.slices = 10
		self.stacks = 10
		self.name = name
		self.mass = mass
		self.color = color(coord (0.6, 0.6, 1.0), 1)

	def get_pos(self):
		return self.pos.tuple()

	def get_vel(self):
		return self.vel.tuple()

	def get_data(self):
		return (self.radius, self.slices, self.stacks)
	
	def get_color(self):
		return self.color.get_color()

profundidad = -60
sun   = planet(coord(0.0, 0.0, profundidad), 	4, 	mass=9000,	name="Sun", 	vel=coord(0,		0.008,	0))
earth = planet(coord(0.0, -15.0, profundidad), 	2, 	mass=50,	name="Earth", 	vel=coord(-1.3,		0,	0))
moon  = planet(coord(0.0, -17, profundidad), 1, 	mass=0.005,	name="Moon",	vel=coord(-1.87,	0,	0))
mars  = planet(coord(-4.0, -7.0,profundidad), 	1, 	mass=500,	name="Mars",	vel=coord(5,		-5,	0))

planets = [sun,earth,moon]
universo = []
time = 0
interval = 0.0008
G = 0.003
camera = coord (0.0, 0.0, 0.0)

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):					# We call this right after our OpenGL window is created.
	glClearColor(0.0, 0.0, 0.0, 0.0)			# This Will Clear The Background Color To Black
	glShadeModel(GL_SMOOTH)
	glEnable(GL_CULL_FACE)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	lightZeroPosition = [10.0, 4.0, 10.0, 1.0]
	lightZeroColor = [1.0, 1.0, 0.8, 1.0] 			# green tinged
	glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
	glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	glEnable(GL_LIGHT0)
	glMatrixMode(GL_PROJECTION)
	gluPerspective(40.0, 1.0, 1.0 ,40.0)
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	
# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:				# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 500.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def DrawGLScene():
	global universo,time
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View 

        glMatrixMode(GL_PROJECTION)
	glTranslatef(*camera.tuple())
	glMatrixMode(GL_MODELVIEW)

	for moment in universo:
	    for i in moment:
		glPushMatrix()
		glTranslatef(*i.get_pos())
                glMaterialfv(GL_FRONT,GL_DIFFUSE,i.get_color())
		glutSolidSphere(*i.get_data())
		glPopMatrix()

	for i in planets:
                glPushMatrix()
                glTranslatef(*i.get_pos())
                glMaterialfv(GL_FRONT,GL_DIFFUSE,i.get_color())
                glutSolidSphere(*i.get_data())
                glPopMatrix()

	
	#  since this is double buffered, swap the buffers to display what just got drawn. 
	glutSwapBuffers()

	if not time % 20:
		for moment in universo:
			 for i in moment:
				i.color.color = i.color.color.escalar_mul(0.95)
		if len(universo) > 10:
			universo.pop(0)	
		universo.append(copy.deepcopy(planets))
		


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
    if args[0] == '+':
	camera.z -= 1
	print "Camera moving " + str(camera.tuple())
    if args[0] == '-':
	camera.z += 1
	print "Camera moving " + str(camera.tuple())

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
    if args[0] == '+':
	camera.z = 0
	print "Camera stopped"
    if args[0] == '-':
	camera.z = 0
	print "Camera stopped"

def recalculate(a):
	global time,interval

	t = interval

        for i in planets:
                #print "---"
                for j in planets:
                        if j==i:
                                continue

                        u = j.pos - i.pos
                        u = u.unitary()

                        dist = i.pos.dist(j.pos)
			
                        #if dist < j.radius+i.radius:
                        #	i.vel = coord (0,0,0)
			#	continue

                        g = (G * j.mass / pow(dist,2)) / i.mass
                        u = u.escalar_mul(g)

                        i.vel += u.escalar_mul(t)

			v = i.vel.escalar_mul(t)
			a = u.escalar_mul(pow(t,2) / 2)

                        i.pos += v + a

                        #print i.name, j.name
                        #print "%f -> %f" % (dist,g)
			#print u.tuple()
                        #print i.vel.mod()
               		#print earth.vel.tuple()

	time += 1;

#	if not (time % 5):
	DrawGLScene();
		
	glutTimerFunc(10, recalculate,0)



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
	#glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE )
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

	glutTimerFunc(10, recalculate,0)
	glutIgnoreKeyRepeat(1)

	# Initialize our window. 
	InitGL(1024, 768)

	# Start Event Processing Engine	
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print "Hit ESC key to quit."
main()
    	
