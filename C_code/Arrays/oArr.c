#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Цвета вывода текста в консоль используется ключ $s
#define KNRM  "\x1B[0m"//Вернуть нормальный цвет
#define KRED  "\x1B[31m"//Красный
#define KGRN  "\x1B[32m"//Зелёный
#define KYEL  "\x1B[33m"//Жёлтый
#define KBLU  "\x1B[34m"//Голубой
#define KMAG  "\x1B[35m"//Фиолетовый
#define KCYN  "\x1B[36m"//Синий
#define KWHT  "\x1B[37m"//Белый


/*
 Микролиба которой нужны стоковые либы ;D

 Ниже расшифровка общих для всего кода переменных
 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
 n-количество элементов
 min-минимальное значение
 max-максимальное значение
 */
void randfill(int A[], int n, int min, int max)//заполнение массива рандомными числами в заданном диапозоне
{
    srand(time(NULL));
    int i;
    for(i = 0; i < n; i++)
        A[i] = rand()%(max - min + 1) + min;
}

void keyfill(int A[], int n)//заполнение массива с клавиатуры A[]-передаём массив, n-длинна массива
{
    int i;
    for(i = 0; i < n; i++)
        scanf("%i", &A[i]);
}

void reverce(int A[], int n, int B[])//записть развёрнутого массива А в массив В
{
    int i;
    for(i = 0; i < n; i++)
        B[i] = A[n - 1 - i];
}

void outM(int A[], int n)//выыод одномерных массивов
{
    int i;
    for(i = 0; i < n; i++){
        printf("%i ", A[i]);
    }
    printf("\n");
}

void sort(int A[], int n, int B[], int direction) //сортировка массива А в массив В, длинной n, с direction направлением убывающий(1) и возрастающий(2)
{
    int i, j, t = 0;
    for(i = 0; i < n; i++)
        B[i] = A[i];
    for(i = 0; i < n - 1; i++)
    {
        for(j = 0; j < n - i - 1; j++)
        {
            if(B[j] > B[j+1])
            {
                t = B[j];
                B[j] = B[j + 1];
                B[j + 1] = t;
            }
        }
    }
    if(direction == 2)
        for(i=0; i < n / 2; i++)
        {
            t = B[i];
            B[i] = B[n - 1 - i];
            B[n - 1 - i] = t;
        }
    else
        if(direction == 1);
    else
    {
        printf("%sWRONG ENTITY%s\n", KRED, KNRM);
        exit(0);
    }
}

void shufle(int A[], int n, int B[])//Здесь мы преремешиванм массив и записываем его в другой
{
  srand(time(NULL));
  int i, j, tmp;
  for(i = 0; i < n; i++)
      B[i] = A[n - 1 - i];

  for(i = n - 1; i >= n; i--)
  {
    j = rand() % (i + 1);
    tmp = B[j];
    B[j] = B[i];
    B[i] = tmp;
  }
}

int main()//это для проверки функций
{
    int n, max, min, direction, type;
    printf("Input list lenght here >>> ");
    scanf("%i", &n);
    printf("Input type of filling %s[1-by keyboard, 2-random]%s >>> ", KRED, KNRM);
    scanf("%i", &type);
    int A[n], B[n], C[n], D[n], E[n];
    if(type == 2)
    {
        printf("Input minimum >>> ");
        scanf("%i", &min);
        printf("Input maximum >>> ");
        scanf("%i", &max);
        randfill(A, n, min, max);
    }
    else
        if(type == 1)
        {
            printf("Input nubers here\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n");
            keyfill(A, n);
        }
    else
    {
        printf("%sWRONG ENTITY%s\n", KRED, KNRM);
        exit(0);
    }
    printf("Choose sorting direction %s[1-increasing, 2-decreasing]%s >>> ", KRED, KNRM);
    scanf("%i", &direction);
    reverce(A, n, B);
    sort(A, n, C, direction);
    printf("Starting list >>> ");
    outM(A, n);
    printf("Reverced list >>> ");
    outM(B, n);
    printf("Sorted   list >>> ");
    outM(C, n);
    shufle(A, n, D);
    printf("Sguffled list >>> ");
    outM(D, n);
    return 0;
}
