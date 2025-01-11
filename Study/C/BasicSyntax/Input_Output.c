#include <stdio.h>
#define STUDENTS 5
int main(void)
{

	int grade[STUDENTS];
	int sum = 0;
	int i, average;
	for (i = 0; i < STUDENTS; i++)
	{
		printf("학생들의 성적을 입력하시요:");
		scanf("%d", grade[i]);
	}

	for (i = 0; i < STUDENTS; i++)
		sum += grade[i];
	
	average = sum / STUDENTS;
	printf("성적 평균 = %d\n", average);

	return 0;

}