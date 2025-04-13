import unittest
from thomas import thomas

class TestThomasAlgorithm(unittest.TestCase):
    def test_example_from_code(self):
        """Тест примера из исходного кода"""
        a = [0, 3, 2]
        b = [2, 4, 5]
        c = [1, 1, 0]
        d = [5, 6, 7]
        expected = [3.19048, -1.38095, 1.95238]
        result = thomas(a, b, c, d)
        for res, exp in zip(result, expected):
            self.assertAlmostEqual(res, exp, places=5)

    def test_diagonal_matrix(self):
        """Тест диагональной матрицы (внедиагональные элементы = 0)"""
        a = [0, 0, 0, 0]
        b = [2, 4, 6, 8]
        c = [0, 0, 0, 0]
        d = [4, 8, 12, 16]
        expected = [2, 2, 2, 2]
        result = thomas(a, b, c, d)
        self.assertEqual(result, expected)

    def test_larger_system(self):
        """Тест системы 4x4"""
        a = [0, 1, 1, 1]    # a[0] не используется
        b = [4, 5, 6, 7]    # Главная диагональ
        c = [2, 3, 4, 0]    # c[-1] не используется
        d = [6, 9, 11, 8]
        expected = [1, 1, 1, 1]
        result = thomas(a, b, c, d)
        for res, exp in zip(result, expected):
            self.assertAlmostEqual(res, exp, places=5)

    def test_another_example(self):
        """Еще один пример с известным решением"""
        a = [0, 2, 3]
        b = [5, 6, 7]
        c = [1, 2, 0]
        d = [14, 30, 37]
        expected = [2, 3, 4]
        result = thomas(a, b, c, d)
        self.assertEqual([round(x) for x in result], expected)

if __name__ == '__main__':
    unittest.main()