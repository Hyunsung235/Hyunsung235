#include <stdio.h>

int main(void) {
    int loop;
    scanf("%d", &loop);

    for (int i = 0; i < loop; i++) {
        int grade[1000] = { 0 };
        int over;
        int sum = 0;
        scanf("%d", &over);

        if (over > 1000) {
            printf("Input size exceeds limit.\n");
            return 1;
        }

        for (int j = 0; j < over; j++) {
            scanf("%d", &grade[j]);
        }

    }

    return 0;
}
