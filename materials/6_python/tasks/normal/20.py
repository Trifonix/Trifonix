'''
Удаление дубликатов из списка
Ввод: список
Вывод: новый список без повторяющихся значений, сохраняя порядок
'''
import unittest
def remove_duplicates(lst):
  seen = set()
  result = []
  for item in lst:
    if item not in seen:
      seen.add(item)
      result.append(item)
  return result
class TestRemoveDuplicates(unittest.TestCase):
  def test_table(self):
    test_cases = [
      ([1, 2, 2, 3, 1, 4], [1, 2, 3, 4]),
      (['a', 'b', 'a', 'c'], ['a', 'b', 'c']),
      ([], []),
      ([1, 1, 1], [1]),
      ([42], [42])
    ]
    for input_data, expected_output in test_cases:
      with self.subTest(input=input_data):
        self.assertEqual(remove_duplicates(input_data), expected_output)
unittest.main()
