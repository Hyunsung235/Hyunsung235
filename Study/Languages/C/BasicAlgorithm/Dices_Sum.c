// �ֻ��� �ΰ��� �������� ���� n�� �ǰ� �ϴ� ������ ( a, b )
// �ֻ��� ������ ������ �� ���� n�� �ǰ� �ϴ� ������ ( a, b, c )

#include <stdio.h>

#include <stdio.h>

void two_Dices(void) {
    int sum, a, b;

    sum = 6;

    for (a = 1; a <= 6; a++) {
        for (b = 1; b <= 6; b++) {
            if (a <= b && a + b == sum) {
                printf("( %d, %d )\n", a, b);
            }
        }
    }
}

void three_Dices(void) {
    int sum, a, b, c;

    sum = 10;

    for (a = 1; a <= 6; a++) {
        for (b = 1; b <= 6; b++) {
            for (c = 1; c <= 6; c++) {
                if (c >= b && b >= a && a + b + c == sum) {
                    printf("( %d, %d, %d )\n", a, b, c);
                }
            }
        }
    }
}

int main(void) {
    two_Dices();
    three_Dices();
    return 0;
}
