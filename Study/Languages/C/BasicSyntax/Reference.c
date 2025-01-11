#include <stdio.h>

int main(void)
{
    int i = 10;
    float f = 1.51234;
    double d = 3.141592;

    int* pi = &i;
    float* pf = &f;
    double* pd = &d;

    printf("size of i = %zu\n", sizeof(i));
    printf("size of f = %zu\n", sizeof(f));
    printf("size of d = %zu\n", sizeof(d));

    printf("size of pi = %zu\n", sizeof(pi));
    printf("size of pf = %zu\n", sizeof(pf));
    printf("size of pd = %zu\n", sizeof(pd));

    int i2 = 3000;  // 변수 선언
    int* p = &i2;   // 변수와 포인터 연결

    printf("i2 = %d\n", i2);    // 변수의 값 출력
    printf("&i2 = %p\n", &i2);  // 변수의 주소 출력

    printf("*p = %d\n", *p);    // 포인터를 통한 간접 참조 값 출력
    printf("p = %p\n", p);      // 포인터의 값 출력

    char* pc;
    int* pi2;
    double* pd2;

    pc = (char*)10000;
    pi2 = (int*)10000;
    pd2 = (double*)10000;
    printf("증가 전 pc = %p, pi2 = %p, pd2 = %p\n", pc, pi2, pd2);

    pc++;
    pi2++;
    pd2++;
    printf("증가 후 pc = %p, pi2 = %p, pd2 = %p\n", pc, pi2, pd2);

    i2 = 10;
    pi2 = &i2;

    printf("i2 = %d, pi2 = %p\n", i2, pi2);
    (*pi2)++;
    printf("i2 = %d, pi2 = %p\n", i2, pi2);

    printf("i2 = %d, pi2 = %p\n", i2, pi2);
    pi2++;
    printf("i2 = %d, pi2 = %p\n", i2, pi2);

    int a[] = { 10, 20, 30, 40, 50 };
    printf("&a[0] = %p\n", &a[0]);
    printf("&a[1] = %p\n", &a[1]);
    printf("&a[2] = %p\n", &a[2]);
    printf("a = %p\n", a);
    return 0;
}
