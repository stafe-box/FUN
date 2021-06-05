#include <stdio.h>

int main()
{
  printf("let's get to know how many ♂︎fisting♂︎ you could get\n");
  printf("how many ♂︎bucks♂︎ you have >>> ");
  int bucks = 0, fisting = 0, more = 0;
  scanf("%i", &bucks);
  if(bucks < 300){
    more = 300 - bucks;
    printf("You have not enough ♂︎bucks♂︎ for ♂︎fisting♂︎ you need %i ♂︎bucks♂︎ more\n", more);
  }
  else{
    fisting = bucks / 300;
    printf("You are ♂︎fucking slave♂︎ you could get %i ♂︎fisting♂︎ by ♂︎van♂︎\n", fisting);
  }
  return 0;
}
