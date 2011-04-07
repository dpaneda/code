//To compile $ gcc -O NAME.c -o OUTPUTNAME -lglut

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>


#define    WIDTH 524
#define    HEIGHT 524

GLubyte MatrixImage[HEIGHT][WIDTH][3];
float color;
static GLint height;
/*
float Interpolate (float a, float b, float c) {
  return a + (b - a) * c * c * (3 - 2 * c);
}


float InterLinear (float a, float b, float c) {
  return a * (1 - c) + b * c;
}
*/
float Interpolate(float a, float b, float c) {
	float ft = c * 3.1415927;
	float f = (1 - cos(ft)) * 0.5;

	return  a*(1-f) + b*f;
}

float Noise (int x,int y) {
  int n = x + y*5778;
  n = (n << 13) ^ n;
  return (((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 2147483648.0);
}

float SmoothNoise_1 (float x, float y) {
	float corners = ( Noise(x-1, y-1) + Noise(x+1, y-1) + Noise(x-1, y+1) + Noise(x+1, y+1) ) / 16;
	float sides   = ( Noise(x-1, y)   + Noise(x+1, y)   + Noise(x, y-1)   + Noise(x, y+1) ) /  8;
	float center  =  Noise(x, y) / 4;
	return corners + sides + center;
}

float InterpolatedNoise_1(float x, float y) {
      float integer_X    = (int)x;
      float fractional_X = x - integer_X;

      float integer_Y    = (int)y;
      float fractional_Y = y - integer_Y;

      float v1 = SmoothNoise_1(integer_X,     integer_Y);
      float v2 = SmoothNoise_1(integer_X + 1, integer_Y);
      float v3 = SmoothNoise_1(integer_X,     integer_Y + 1);
      float v4 = SmoothNoise_1(integer_X + 1, integer_Y + 1);

      float i1 = Interpolate(v1 , v2 , fractional_X);
      float i2 = Interpolate(v3 , v4 , fractional_X);

      return Interpolate(i1 , i2 , fractional_Y);
}

float PerlinNoise (float x, float y, int octaves) {
  int s; 
  double amplitude,freq,value=0;

  for (s = 0; s < octaves; s++) {
      freq =  pow(2,s) / 80.0;
      amplitude = 256 * pow(0.25,s);
      //value += SmoothNoise_1 (x * freq, y * freq) * amplitude;
      value += InterpolatedNoise_1 (x * freq, y * freq) * amplitude;
      //printf("%f %f %f\n", freq, amplitude, value);
  }
  return value;
}

void makeImage (void) {
  int x, y;

  for (y = 0; y < WIDTH; y++) 
    for (x = 0; x < HEIGHT; x++) {
      MatrixImage[x][y][0] = MatrixImage[x][y][1] = MatrixImage[x][y][2] = PerlinNoise (x, y , 8);
    }
}

void init (void) {
  glClearColor (0.0, 0.0, 0.0, 0.0);
  glShadeModel (GL_FLAT);
  makeImage ();
  glPixelStorei (GL_UNPACK_ALIGNMENT, 1);
}

void display (void) {
  glClear (GL_COLOR_BUFFER_BIT);
  glRasterPos2i (0, 0);
  glDrawPixels (WIDTH,HEIGHT, GL_RGB, GL_UNSIGNED_BYTE, MatrixImage);
  glFlush ();
}

void reshape (int w, int h) {
  glViewport (0, 0, (GLsizei) w, (GLsizei) h);
  height = (GLint) h;
  glMatrixMode (GL_PROJECTION);
  glLoadIdentity ();
  gluOrtho2D (0.0, (GLdouble) w, 0.0, (GLdouble) h);
  glMatrixMode (GL_MODELVIEW);
  glLoadIdentity ();
}

void keyboard (unsigned char key, int x, int y) {
  if (key == 27) 
    exit (0);
}

int main (int argc, char **argv) {
  glutInit (&argc, argv);
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
  glutInitWindowSize (WIDTH,HEIGHT);
  glutInitWindowPosition (100, 100);
  glutCreateWindow (argv[0]);
  init ();
  glutDisplayFunc (display);
  glutReshapeFunc (reshape);
  glutKeyboardFunc (keyboard);
  glutMainLoop ();
  return 0;
}
