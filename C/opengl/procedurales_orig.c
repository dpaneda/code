//To compile $ gcc -O NAME.c -o OUTPUTNAME -lglut

#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>


#define    WIDTH 524
#define    HEIGHT 524

GLubyte MatrixImage[HEIGHT][WIDTH][3];
float RGB[3];
static GLint height;


float InterPolation (float a, float b, float c) {
  return a + (b - a) * c * c * (3 - 2 * c);
}


float InterLinear (float a, float b, float c) {
  return a * (1 - c) + b * c;
}

float Noise (int x) {
  x = (x << 13) ^ x;
  return (((x * (x * x * 15731 + 789221) + 1376312589) & 0x7fffffff) / 2147483648.0);
}

float PerlinNoise (float x, float y, int width, int octaves, int seed, double periode)
{
  double a, b, value, freq, tam_pas, zone_x, zone_y;
  int s, box, num, step_x, step_y;
  int amplitude = 120;
  int noisedata;

  freq = 1 / (float) (periode);

  for (s = 0; s < octaves; s++) {
      num = (int) (width * freq);
      step_x = (int) (x * freq);
      step_y = (int) (y * freq);
      zone_x = x * freq - step_x;
      zone_y = y * freq - step_y;
      box = step_x + step_y * num;
      noisedata = (box + seed);
      a = InterPolation (Noise (noisedata), Noise (noisedata + 1), zone_x);
      b = InterPolation (Noise (noisedata + num), Noise (noisedata + 1 + num), zone_x);
      value = InterPolation (a, b, zone_y) * amplitude;
  }
  return value;
}



void colour (float valor) {
  int r = InterLinear (valor, 0, 0);
  int g = InterLinear (valor, 0, 0);
  int b = InterLinear (valor, 0, 0);

  RGB[0] = 0;
  RGB[1] = g;
  RGB[2] = 0;
}

void makeImage (void) {

  int x, y;
  float color;
  int seed;
  int width;
  float disp1, disp2, disp3, disp4, disp5, disp6, scale;

  for (y = 0; y < WIDTH; y++)
    {
      for (x = 0; x < HEIGHT; x++)
	{
	  scale = 1;
	  width = 12413;
	  seed = 43;
	  disp1 = PerlinNoise (x * scale, y * scale, width, 1, seed, 100);
	  disp2 = PerlinNoise (x * scale, y * scale, width, 1, seed, 25);
	  disp3 = PerlinNoise (x * scale, y * scale, width, 1, seed, 12.5);
	  disp4 = PerlinNoise (x * scale, y * scale, width, 1, seed, 6.25);
	  disp5 = PerlinNoise (x * scale, y * scale, width, 1, seed, 3.125);
	  disp6 = PerlinNoise (x * scale, y * scale, width, 1, seed, 1.56);

	  colour ((int) disp1 + (int) (disp2 * .25) + (int) (disp3 * .125) +
		  (int) (disp4 * .0625) + (int) (disp5 * .03125) +
		  (int) (disp6 * .0156));

	  MatrixImage[x][y][0] = RGB[0];
	  MatrixImage[x][y][1] = RGB[1];
	  MatrixImage[x][y][2] = RGB[2];
    }}
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
  switch (key) {
    case 27:
      exit (0);
      break;
    default:
      break;
  }
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
