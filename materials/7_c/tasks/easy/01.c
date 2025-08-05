/*
Сумма двух чисел
Ввод: два целых числа  
Вывод: их сумма
*/
#include <stdio.h>
int sum(int a, int b)
{
  return a + b;
}
int main()
{
  int x, y;
  printf("Enter 2 nums: ");
  scanf("%d %d", &x, &y);
  printf("Sum: %d\n", sum(x, y));
  if (sum(2,3) != 5)
  {
    printf("Test 1 failed: sum(2, 3) != 5\n");
  }
  else
  {
    printf("Test 1 passed\n");
  }
  return 0;
}
