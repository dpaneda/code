#include <stdio.h>
#include <stdlib.h>

int main (void) {
    int i, j, numcases;
    int r, k, s;
    int *groups = NULL;
    int *round = NULL;
    int next, ride, free, first;
    unsigned long long int *rmoney = NULL;
    unsigned long long int money;

    groups = malloc(10000000 * sizeof(int));
    round  = malloc(10000000 * sizeof(int));
    rmoney = malloc(10000000 * sizeof(unsigned long long int));

    scanf("%d", &numcases);

    for (i = 1; i < numcases + 1; i++) {
        scanf("%d %d %d",&r, &k, &s);
        
        for (j = 0; j <s; j++) {
            scanf("%d", &groups[j]);
            round[j] = -1;
            rmoney[j] = 0;
        }

        money = next = ride = 0;

        while (ride < r) {
            if ((round[next] > 0) && (money > 0)) {
                unsigned long long int md = money - rmoney[next];
                unsigned int rd = ride - round[next];
                round[next] = rmoney[next] = -1;
                if (ride + rd < r) {
                    unsigned int times = (r - ride) / rd; 
                    ride += rd * times;
                    money += md * times;
                    continue;
                }
            }
            free = k;
            first = -1;
 
            while ((free >= groups[next]) && (first != next)) {
                if (first == -1) {
                    first = next;
                    round[first] = ride;
                    rmoney[first] = money;
                }
                free -= groups[next];
                money += groups[next];
                next = (next + 1) % s; 
            }
            ride++;
        }
        printf("Case #%d: %llu\n", i, money);
    }
}
