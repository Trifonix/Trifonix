<?php
# Сумма двух чисел
# Ввод: два целых числа 
# Вывод: их сумма
function sum($a, $b)
{
  return $a + $b;
}
echo "Введите первое число: ";
$first = readline();
echo "Введите второе число: ";
$second = readline();
echo "Сумма: " . sum($first, $second) . "\n";
function test_sum($a, $b, $expected)
{
  $result = sum($a, $b);
  if ($result === $expected)
  {
    echo "Тест пройден";
  }
  else
  {
    echo "Тест не пройден для данных ($a, $b): получено $result, ожидалось $expected\n";
  }
}
# https://onecompiler.com/php
?>