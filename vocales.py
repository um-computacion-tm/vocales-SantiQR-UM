import unittest


def contar_vocales(word):
    vocales = ("aeiou")
    dict = {}
    for letter in word.lower():
        if letter in vocales:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    return dict


class TestVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_normal(self):
        resultado = contar_vocales('aa')
        self.assertEqual(resultado, {'a':2})

    def test_mayusculas(self):
        resultado = contar_vocales('AVION   ')
        self.assertEqual(resultado, {'a':1, 'i':1, 'o':1})
    
    def test_espacios(self):
        resultado = contar_vocales(' aisd fo ausdef ')
        self.assertEqual(resultado, {'a':2, 'e':1, 'i':1, 'o':1, 'u':1})

if __name__ == "__main__":
    unittest.main()

