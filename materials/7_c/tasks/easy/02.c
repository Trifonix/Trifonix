/*
Определить чётность числа
Ввод: одно целое число
Вывод: `"Чётное"` или `"Нечётное"`
*/
#include <stdio.h>
#include <stdbool.h>
bool is_even(int n)
{
  return n % 2 == 0;
}
int main()
{
  int number;
  printf("Enter num: ");
  scanf("%d", &number);
  if(is_even(number))
  {
    printf("even\n");
  } else
  {
    printf("odd\n");
  }
  if(is_even(2) != true)
  {
    printf("Test 1 failed: 2 is even\n");
  } else
  {
    printf("Test 1 passed\n");
  }
  return 0;
}
