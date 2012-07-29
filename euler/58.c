#include <stdio.h>
#include <strings.h>
#include <stdlib.h>

int is_prime(int n) {
  int m;

  for(m = 2; m < (n/2) + 1; m++) {
    if (n % m == 0)                
      return 0;
  }

  return 1;
}

float test_matrix(int size) {
  int matrix[size][size];

  int i = size / 2;
  int j = size / 2;

  int dir = 0;
  int number = 1;
  int impulse = 1;
  int movs = 1;
  int finish = 0;

  while (number <= size * size) {
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

  int s = 0;
  int total = 0;
  i = 0;

  while (i < size) {
    is_prime(matrix[i][i]) && s++;
    is_prime(matrix[i][size - i - 1]) && s++;
    i++;
    total += 2;
  }

  return s / (float) total;
}

int main(void) {
  int percent = 100;
  int size=9;

  while (1) {
    float percent = test_matrix(size);
    printf("%f\n", percent);
    if (percent < 0.1)
      break;
    size+=2;
  }

  printf("%d\n", size);
}
