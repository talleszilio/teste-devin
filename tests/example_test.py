"""
Testes unitários de exemplo para o projeto
Simula testes que você encontraria em um ambiente real
"""

import unittest
from datetime import datetime


class TestExemplo(unittest.TestCase):
    """Classe de teste de exemplo"""
    
    def test_soma(self):
        """Teste simples de soma"""
        resultado = 2 + 2
        self.assertEqual(resultado, 4)
    
    def test_string_length(self):
        """Teste de tamanho de string"""
        texto = "Devin"
        self.assertEqual(len(texto), 5)
    
    def test_datetime_now(self):
        """Teste de data atual"""
        agora = datetime.now()
        self.assertIsNotNone(agora)
    
    def test_list_operations(self):
        """Teste de operações com listas"""
        lista = [1, 2, 3, 4, 5]
        self.assertIn(3, lista)
        self.assertEqual(len(lista), 5)
    
    def test_dictionary_access(self):
        """Teste de acesso a dicionário"""
        dados = {"nome": "Talles", "email": "talleszilio@gmail.com"}
        self.assertEqual(dados["nome"], "Talles")
        self.assertIn("email", dados)


if __name__ == "__main__":
    unittest.main()