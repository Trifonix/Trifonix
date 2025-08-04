<?php
# Является ли число простым
# Ввод: целое положительное число
# Вывод: `True` или `False`
echo "Введите целое положительное число: ";
$n = (int)readline();
if ($n < 2) {
  echo "False\n";
  exit;
}
$is_prime = true;
for ($i = 2; $i * $i <= $n; $i++) {
  if ($n % $i == 0) {
    $is_prime = false;
    break;
  }
}
if ($is_prime) {
  echo "True\n";
} else {
  echo "False\n";
}
?>
