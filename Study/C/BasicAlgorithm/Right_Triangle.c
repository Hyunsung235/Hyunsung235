// 각 변의 길이가 100보다 작은 삼각형 중 직각 삼각형 찾기


#include <stdio.h>

int main(void)
{
	int a, b, c;
	int count = 0;

	for (a = 1; a < 100; a++) {
		for (b = 1; b < 100; b++) {
			for (c = 1; c < 100; c++) {
				if (a < b && (a * a) + (b * b) == (c * c)) {
					printf("각 변의 길이가 %-3d, %-3d, %-3d 인 삼각형은 직각삼각형 입니다. \n", a, b, c);
					count++;
				}
			}
		}
	}

		printf("직각 삼각형의 개수는 %d\n", count);
		return 0;
}
