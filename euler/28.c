#include <stdio.h>
#include <strings.h>

#define SIZE 1001

int main(void) {
  int matrix[SIZE][SIZE];
  bzero(&matrix, SIZE * SIZE * sizeof(int));

  int i = SIZE / 2;
  int j = SIZE / 2;

  int dir = 0;
  int number = 1;
  int impulse = 1;
  int movs = 1;
  int finish = 0;

  while (number <= SIZE * SIZE) {
    matrix[i][j] = number++;
    
    if (movs == 0) {
      dir = (dir + 1) % 4;
      movs = impulse;
      if (dir % 2)
        impulse++;
    }

    movs--;

    switch (dir) {
      case 0:
        j++;
        break;
      case 1:
        i++;
        break;
      case 2:
        j--;
        break;
      case 3:
        i--;
        break;
    }
  }

  /*
  i = j = 0;
  while (i < SIZE) {
    j = 0;
    while (j < SIZE) {
      printf("%2d ", matrix[i][j]);
      j++;
    }
    printf("\n");
    i++;
  }
  */

  int sum = 0;

  while (i < SIZE) {
    sum += matrix[i][i];
    sum += matrix[i][SIZE - i - 1];
    i++;
  }

  printf("%d", --sum);
}
