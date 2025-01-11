#include <stdio.h>

int add(int, int); // 함수의 원형
int main(void)
{
	int x = 3, y = 4;
	printf("add(x,y) = %d\n", add(x, y));
	printf("x = %d, y = %d", x, y);

	return 0;

} 