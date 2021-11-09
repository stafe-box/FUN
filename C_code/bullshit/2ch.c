#import <stdio.h>
#import <locale.h>
#import <wchar.h>

int main()
{
  setlocale(LC_ALL, "ru_RU.utf-8");
  wchar_t q = 0;
  printf("Оттарабанить автора в сраку? [Д/Н]\n");
  scanf("%lc", &q);
  if(q == '1' || q == 'Y' || q == 'y' || q == L'Д' || q == L'д')
    printf("Автор успешно оттрарабанен в сраку!\n");
    else
      if(q == '0' || q == 'N' || q == 'n' || q == L'Н' || q == L'н')
        printf("Автор к сожалению не оттрарабанен в сраку!\n");
          else
            printf("%sERROR: WRONG ENTITY%s\n\nНо автора всё равно оттрарабанили\n","\x1B[31m", "\x1B[0m");
  return 0;
}
