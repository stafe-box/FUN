#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//цвета вывода текста в консоль используется ключ $s
#define KNRM  "\x1B[0m"//вернуть нормальный цвет
#define KRED  "\x1B[31m"//красный
#define KGRN  "\x1B[32m"//зелёный
#define KYEL  "\x1B[33m"//жёлтый
#define KBLU  "\x1B[34m"//голубой
#define KMAG  "\x1B[35m"//фиолетовый
#define KCYN  "\x1B[36m"//синий
#define KWHT  "\x1B[37m"//белый


/*
 микролиба которой нужны стоковые либы ;D
 
 n-количество элементов
 min-минимальное значение
 max-максимальное значение
 */
void randfill(int A[], int n, int min, int max)//заполнение массива рандомными числами в заданном диапозоне
{
    srand(time(NULL));
    int i;
    for(i=0; i<n; i++)
        A[i] = rand()%(max -min + 1) + min;
}

void reverce(int A[], int n, int B[])//записть развёрнутого массива А в массив В
{
    int i;
    for(i=0; i<n; i++)
        B[i] = A[n-1-i];
}

void outM(int A[], int n)//выыод одномерных массивов
{
    int i;
    for(i=0; i<n; i++){
        printf("%i ", A[i]);
    }
    printf("\n");
}

void sort(int A[], int n, int B[], int direction) //сортировка массива А в массив В, длинной n, с direction направлением убывающий(1) и возрастающий(2)
{
    int i, j, t=0;
    for(i=0; i<n; i++)
        B[i] = A[i];
    for(i = 0; i < n - 1; i++)
    {
        for(j = 0; j < n - i - 1; j++)
        {
            if(B[j] > B[j+1])
            {
                t=B[j];
                B[j] = B[j+1];
                B[j+1] = t;
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

int main()//это для проверки функций
{
    int n, max, min, direction;
    printf("Input list lenght here >>> ");
    scanf("%i", &n);
    printf("Input minimum >>> ");
    scanf("%i", &min);
    printf("Input maximum >>> ");
    scanf("%i", &max);
    printf("Choose sorting direction %s1-minimum to maximum, 2-maximum to minimum%s >>> ", KRED, KNRM);
    scanf("%i", &direction);
    int A[n], B[n], C[n];
    randfill(A, n, min, max);
    reverce(A, n, B);
    sort(A, n, C, direction);
    printf("Starting list >>> ");
    outM(A, n);
    printf("Reverced list >>> ");
    outM(B, n);
    printf("Sorted list >>> ");
    outM(C, n);
    return 0;
}
