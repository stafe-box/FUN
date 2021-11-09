#import <stdio.h>
#import <locale.h>
#import <wchar.h>


void T1(int n){
  printf('Подсчёт первого тура\n');
  int i = 0, score = 0;
  for (i = 0; i < n; i++){
    printf('Введите номер ответа команды ', n, ' >>> ');
    scanf("%i", &score);
    printf('\nОчки ', n, 'комманды: ', score);
  }
}


void T2(int n){
  printf('Подсчёт второго тура\n');
  int i = 0, score = 0;
  for (i = 0; i < n; i++){
    printf('Введите номер ответа команды ', n, ' >>> ');
    scanf("%i", &score);
    printf('\nОчки ', n, 'комманды: ', score * 2);
  }
}


void T3(int n){
  printf('Подсчёт третьего тура\n');
  int i = 0, score = 0;
  wchar_t pic;
  for (i = 0; i < n; i++){
    printf('Введите номер ответа команды ', n, ' >>> ');
    scanf("%i", &score);
    printf('Угадана верная картинка [Д/Н]?\n')
    scanf("%lc", &pic)
    if (pic == 'Y' or pic == 'y' or pic == '1' or pic == 'д' or pic == 'Д'){
        printf('\nОчки ', n, 'комманды: ', score * 3 + 5);
    }
    else{
      printf('\nОчки ', n, 'комманды: ', score * 3);
    }
  }
}
