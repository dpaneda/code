#include <stdio.h>
#include <string.h>

int main () {
    int valids = 0;
    int valids2 = 0;
    int counter;
    int min, max, c = '\0';
    char s[200];
    int i;

    while (scanf("%d-%d %c: %s\n", &min, &max, &c, s) > 0) {
        printf("%d-%d %c: %s\n", min, max, c, s);
        counter = 0;
        for (i = 0; i < strlen(s); i++) {
            if (s[i] == c)
                counter++;
        }
        if ((min <= counter) && (counter <= max))
            valids++;

        // 1-based index
        min--; max--;

        if (max > strlen(s) && s[min] == c)
            valids2++;
        else if ((s[min] != s[max]) && (s[min] == c || s[max] == c))
            valids2++;
    }

    printf("Valids: %d\n", valids);
    printf("Valids2: %d\n", valids2);
}
