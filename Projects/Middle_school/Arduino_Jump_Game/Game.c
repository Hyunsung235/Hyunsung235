#include <LiquidCrystal_I2C.h>

// ��ư �� ��ȣ
#define BTN_PIN 13


// ���� ���¸� ��Ÿ���� �����
#define GAME_WAIT 0
#define GAME_RUN 1
#define GAME_END 2

//ȭ�鿡 ����� ���ڿ���
char GAME_WAIT_VIEW[2][17] =
{
  "Press button to",
  "start game !   "
};

char GAME_RUN_VIEW[2][17] =
{
  "                ",
  "                "
};

char GAME_END_VIEW[2][17] =
{
  "   Your score  ",
  "               "
};

//������ -------------------------------------------
LiquidCrystal_I2C lcd(32, 16, 2); // LCD ��ü ����

int gameState = GAME_WAIT; // ���� ���� ����
int lastDisplayTime = 0;   // ȭ���� ���������� ���ŵ� �ð�
int waitBtnRelease = 0; // ��ư�� ���� �Է��� �����ϱ� ���� �÷���

int heroX = 3; // ���ΰ��� x ��ǥ
int heroY = 1; // ���ΰ��� y ��ǥ
int lastHeroJumpTime = 0; // ���ΰ��� ���������� ������ �ð�
int lastHeroLandTime = 0; // ���ΰ��� ���������� ���� ������ �ð�
int waitHeroLanding = 0; // ���ΰ��� ���� ������ �����ϱ� ���� �÷���

int obstacleX = -1; // ��ֹ��� x ��ǥ(������ ��ֹ��� ����)
int obstacleY = 1; // ��ֹ��� y��ǥ
int lastObstacleMoveTime = 0; // ��ֹ��� ���������� ������ �ð�

int score = 0;

//������Ÿ�� �Լ� ���� -------
void display(int time); // ȭ�� ��� �Լ�(�帥 �ð�)
void process(int btnStat, int time); // ���� ó�� �Լ�(��ư ����, �帥 �ð�)
void heroJump(int btinProcess, int time); // ���ΰ� ���� ó�� �Լ�(��ư ó������, �帥 �ð�)
void obstacleMove(int time); // ��ֹ� �̵� ó�� �Լ�(�帥 �ð�)
void collision(); // ���ΰ��� ��ֹ��� �浹 �˻� �Լ�

void setup()
{
	randomSeed(analogRead(0));
	lcd.init();
	lcd.backlight();
	pinMode(BTN_PIN, INPUT_PULLUP);
}

void loop()
{
	int time = millis();
	int btnStat = digitalRead(BTN_PIN) == LOW ? 1 : 0;

	display(time);
	process(btnStat, time);
}


//������Ÿ�� �Լ� ���� ----------

void display(int time)
{
	char(*view)[17] = NULL;

	// 50ms ���� ȭ���� ����
	if (time - lastDisplayTime < 50) return;

	lastDisplayTime = time;
	switch (gameState)
	{
	case GAME_WAIT:
		view = GAME_WAIT_VIEW;
		break;
	case GAME_RUN:
		view = GAME_RUN_VIEW;
		break;
	case GAME_END:
		view = GAME_END_VIEW;
		break;
	}

	lcd.setCursor(0, 0);
	lcd.print(view[0]);
	lcd.setCursor(0, 1);
	lcd.print(view[1]);

}

void process(int btnStat, int time)
{
	// ��ư �Է� ó�� �÷���
	int btnProcess = 1;

	// ��ư�� ������ ���� ��� ��ư �Է��� ó������ ����
	if (!btnStat)
	{
		waitBtnRelease = 0;
		btnProcess = 0;
	}

	// ��ư�� �������� ������ ���� ���� �������⸦ ��ٸ��� ���¶�� ó������ ����
	else if (btnStat && waitBtnRelease) btnProcess = 0;

	//��ư�� ó���ϱ�� �����ߴٸ� ��ư ������ �÷���(0)�� ��ٸ�
	if (btnProcess) waitBtnRelease = 1;
	switch (gameState)
	{

	case GAME_WAIT:
		if (btnProcess) gameState = GAME_RUN;
		break;
	case GAME_RUN:
		heroJump(btnProcess, time);
		obstacleMove(time);
		collision();
		break;
	case GAME_END:
		if (btnProcess)
		{
			GAME_RUN_VIEW[heroY][heroX] = ' ';
			GAME_RUN_VIEW[obstacleY][obstacleX] = ' ';
			heroX = 3;
			heroY = 1;
			obstacleX = -1;
			obstacleY = 0;
			score = 0;
			gameState = GAME_WAIT;
		}
		break;
	}
}

void heroJump(int btnProcess, int time)
{
	// ���ΰ��� ������ ��ٸ��� ���
	if (waitHeroLanding)
	{
		waitHeroLanding = 0;
		lastHeroLandTime = time;
		GAME_RUN_VIEW[heroY][heroX] = ' ';
		heroY = 1;
	}


	// ��ư�� ó���ؾ��ϰ� ������ ��ٸ��� ���°� �ƴѰ��
	if (btnProcess && !waitHeroLanding)
	{
		//���� �� 200ms���� ���� �־�� ��
		if (time - lastHeroLandTime > 100)
		{
			waitHeroLanding = 1;
			lastHeroJumpTime = time;
			GAME_RUN_VIEW[heroY][heroX] = ' ';
			heroY = 0;
		}
	}
	GAME_RUN_VIEW[heroY][heroX] = '@';
}

void obstacleMove(int time)
{
	// ��ֹ��� ���� ��� ��ֹ� ����
	if (obstacleX < 0)
	{
		obstacleY = random(0, 2);
		obstacleX = 16;
		lastObstacleMoveTime = time;
	}


	// 50ms ���� ��ֹ��� �̵���Ŵ
	else if (time - lastObstacleMoveTime > 50)
	{
		lastObstacleMoveTime = time;
		if (obstacleX < 16)
			GAME_RUN_VIEW[obstacleY][obstacleX] = ' ';
		obstacleX--;
		if (obstacleX >= 0)
			GAME_RUN_VIEW[obstacleY][obstacleX] = '[';

		//��ֹ��� ������� ���� ����
		if (obstacleX < 0)
			score++;
	}
}


void collision()
{
	if (obstacleX == heroX && obstacleY == heroY)
	{
		gameState = GAME_END;
		sprintf(GAME_END_VIEW[1], "%16d", score);
	}
}