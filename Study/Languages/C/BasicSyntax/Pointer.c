#include <stdio.h>

int main(void)
{
    int list[5][5] = {
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50}
    };

    int(*pl)[5] = list;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", pl[i][j]);
            pl[i][j] += 10;
        }
        printf("\n");
    }

    pl = list;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", pl[i][j]);
            pl[i][j] += 10;
        }
        printf("\n");
    }

    int arr[5][5] = {
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50},
        {10, 20, 30, 40, 50}
    };

    int* pi = (int*)arr;

    for (int i = 0; i < 25; i++) {
        *(pi + i) += 10;
    }

    for (int i = 0; i < 25; i++) {
        if (i % 5 == 0)
            printf("\n");
        printf("%03d ", *(pi + i));
    }

    return 0;
}
