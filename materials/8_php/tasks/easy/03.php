<?php
# Максимум из трёх чисел
# Ввод: три числа 
# Вывод: наибольшее из них
echo "Введите первое число: ";
$a = (int)readline();
echo "Введите второе число: ";
$b = (int)readline();
echo "Введите третье число: ";
$c = (int)readline();
$max = $a;
if ($b > $max) {
  $max = $b;
}
if ($c > $max) {
  $max = $c;
}
echo "$max\n";
?>
