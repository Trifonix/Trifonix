/*
Максимум из трёх чисел
Ввод: три числа 
Вывод: наибольшее из них
*/
#include <stdio.h>
int max_of_three(int a, int b, int c)
{
  int max = a;
  if (b > max)
  {
    max = b;
  }
  if (c > max)
  {
    max = c;
  }
  return max;
}
int main()
{
  int x, y, z;
  printf("Enter three integers: ");
  scanf("%d %d %d", &x, &y, &z);
  printf("Maximum: %d\n", max_of_three(x, y, z));
  if (max_of_three(1, 2, 3) != 3)
  {
    printf("Test 1 failed\n");
  }
  else
  {
    printf("Test 1 passed\n");
  }
  return 0;
}
