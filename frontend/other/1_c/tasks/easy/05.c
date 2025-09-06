/*
Является ли число простым
Ввод: целое положительное число
Вывод: `True` или `False`
*/
#include <stdio.h>
#include <stdbool.h>
bool is_prime(int n)
{
  if (n <= 1)
  {
    return false;
  }
  for (int i = 2; i * i <= n; i++)
  {
    if (n % i == 0)
    {
      return false;
    }
  }
  return true;
}
int main()
{
  int number;
  printf("Enter a positive integer: ");
  scanf("%d", &number);
  if (is_prime(number))
  {
    printf("True\n");
  }
  else
  {
    printf("False\n");
  }
  if (is_prime(1) != true)
  {
    printf("Test 1 failed (1 is not prime)\n");
  }
  else
  {
    printf("Test 1 passed\n");
  }
  return 0;
}
