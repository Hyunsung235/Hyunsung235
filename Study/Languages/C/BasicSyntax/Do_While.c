// do while�� Ȱ���� ���ڸ�����


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	int answer;	// ����
	int input;		// ���� ������ ����
	int try = 0;		// �õ� Ƚ��

	// answer = rand() % 100 + 1; n��°�� nn �̷������� �����ϴ�
	
	srand((unsigned int)time(NULL));	// �ð� + ����
	answer = rand() % 100 + 1;			// �ð� + ������ �޾ƿ�

	do
	{
		try++;

		printf("������ �����Ͽ� ���ÿ�: ");
		scanf("%d", &input);

		if (answer > input)			printf("\n ������ ������ �����ϴ�. \n");
		else if (answer < input)	printf("\n ������ ������ �����ϴ�. \n");

	}	while (answer != input);

	printf("�����մϴ�. �õ�Ƚ�� = %d", try);
	return 0;
}
