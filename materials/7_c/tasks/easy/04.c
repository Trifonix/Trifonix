/*
Факториал числа 
Ввод: целое положительное число `n`
Вывод: `n!`
*/
#include <stdio.h>
unsigned long long factorial(int n)
{
  unsigned long long result = 1;
  for (int i = 1; i <= n; i++)
  {
    result *= i;
  }
  return result;
}
int main()
{
  int n;
  printf("Enter a positive integer: ");
  scanf("%d", &n);
  if (n < 0)
  {
    printf("Error: negative input not allowed\n");
  }
  else
  {
    printf("Factorial of %d is %llu\n", n, factorial(n));
  }
  if (factorial(0) != 1)
  {
    printf("Test 1 failed (0! should be 1)\n");
  }
  else
  {
    printf("Test 1 passed\n");
  }
  return 0;
}
