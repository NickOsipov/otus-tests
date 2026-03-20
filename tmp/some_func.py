from src.some_func import some_function  # Импортируем функцию, которую будем тестировать

import unittest

class TestSomeFunctionality(unittest.TestCase):  # Имя обычно начинается с "Test"
    
    def setUp(self):
        # Подготовка окружения перед каждым тестом
        pass
        
    def tearDown(self):
        # Очистка окружения после каждого теста
        pass
        
    def test_some_feature(self):  # Имя метода начинается с "test_"
        # Тестовый код
        expected = 100000                   # Ожидаемое значение
        actual = some_function()            # Фактическое значение
        self.assertEqual(expected, actual)  # Проверка на равенство
        self.assertTrue(actual > 0)         # Проверка, что результат положительный
        self.assertIsNotNone(actual)        # Проверка, что результат не None
