 // 반복을 이용한 정수합 프로그램


#include <stdio.h>

int main(void)
{
	int i, sum;
	sum = 0;

	for(i = 1; i <= 10; i++)
		sum += i; // sum = sum + i;와 같음

	printf("1부터 10까지 정수의 합 = %d\n", sum);

	return 0;

}
