#include <LiquidCrystal_I2C.h>

// 버튼 핀 번호
#define BTN_PIN 13


// 게임 상태를 나타내는 상수값
#define GAME_WAIT 0
#define GAME_RUN 1
#define GAME_END 2

//화면에 출력할 문자열들
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

//변수들 -------------------------------------------
LiquidCrystal_I2C lcd(32, 16, 2); // LCD 객체 생성

int gameState = GAME_WAIT; // 현재 게임 상태
int lastDisplayTime = 0;   // 화면이 마지막으로 갱신된 시간
int waitBtnRelease = 0; // 버튼의 연속 입력을 방지하기 위한 플래그

int heroX = 3; // 주인공의 x 좌표
int heroY = 1; // 주인공의 y 좌표
int lastHeroJumpTime = 0; // 주인공이 마지막으로 점프한 시간
int lastHeroLandTime = 0; // 주인공이 마지막으로 땅에 착지한 시간
int waitHeroLanding = 0; // 주인공이 연속 점프를 방지하기 위한 플래그

int obstacleX = -1; // 장애물의 x 좌표(음수면 장애물이 없음)
int obstacleY = 1; // 장애물의 y좌표
int lastObstacleMoveTime = 0; // 장애물이 마지막으로 움직인 시간

int score = 0;

//프로토타입 함수 정의 -------
void display(int time); // 화면 출력 함수(흐른 시간)
void process(int btnStat, int time); // 게임 처리 함수(버튼 상태, 흐른 시간)
void heroJump(int btinProcess, int time); // 주인공 점프 처리 함수(버튼 처리상태, 흐른 시간)
void obstacleMove(int time); // 장애물 이동 처리 함수(흐른 시간)
void collision(); // 주인공과 장애물의 충돌 검사 함수

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


//프로토타입 함수 구현 ----------

void display(int time)
{
	char(*view)[17] = NULL;

	// 50ms 마다 화면을 갱신
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
	// 버튼 입력 처리 플래그
	int btnProcess = 1;

	// 버튼이 눌리지 않은 경우 버튼 입력은 처리하지 않음
	if (!btnStat)
	{
		waitBtnRelease = 0;
		btnProcess = 0;
	}

	// 버튼이 눌렸으나 이전에 눌린 이후 떨어지기를 기다리는 상태라면 처리하지 않음
	else if (btnStat && waitBtnRelease) btnProcess = 0;

	//버튼을 처리하기로 결정했다면 버튼 떨어짐 플래그(0)을 기다림
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
	// 주인공의 착지를 기다리는 경우
	if (waitHeroLanding)
	{
		waitHeroLanding = 0;
		lastHeroLandTime = time;
		GAME_RUN_VIEW[heroY][heroX] = ' ';
		heroY = 1;
	}


	// 버튼을 처리해야하고 착지를 기다리는 상태가 아닌경우
	if (btnProcess && !waitHeroLanding)
	{
		//착지 후 200ms동안 땅에 있어야 함
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
	// 장애물이 없는 경우 장애물 생성
	if (obstacleX < 0)
	{
		obstacleY = random(0, 2);
		obstacleX = 16;
		lastObstacleMoveTime = time;
	}


	// 50ms 마다 장애물을 이동시킴
	else if (time - lastObstacleMoveTime > 50)
	{
		lastObstacleMoveTime = time;
		if (obstacleX < 16)
			GAME_RUN_VIEW[obstacleY][obstacleX] = ' ';
		obstacleX--;
		if (obstacleX >= 0)
			GAME_RUN_VIEW[obstacleY][obstacleX] = '[';

		//장애물이 사라지면 점수 증가
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