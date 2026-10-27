assert para testes diretos


unittest metodos da classe test case
self.assertEqual(a, b)

self.assertTrue(x)

self.assertFalse(x)

self.assertRaises(), etc.

exemplo:

import unittest

class TestMatematica(unittest.TestCase):
    def test_soma(self):
        resultado = 2 + 3
        self.assertEqual(resultado, 5)

if __name__ == "__main__":
    unittest.main()

    Aqui, você não usa a palavra assert simples, mas sim os métodos da classe.

Esses métodos geram relatórios de teste mais detalhados e integração com frameworks.
