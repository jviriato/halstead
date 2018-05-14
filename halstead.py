"""
O programa calcula as métricas de Halstead e o LOC 
na linguagem Python, reconhecendo um arquivo .c.
"""

import math
import argparse # para argumentos em linha de comando

class Halstead:
    """
    Classe que encapsula todas as métricas de Halstead
    """
    def __init__(self, file):
        """
        Construtor de um novo objeto 'Halstead'
        :param file: nome do arquivo
        """
        self.file = file
        self.num_operators = 0
        self.num_operands  = 0
        self.lines_of_code = 0

    def check_if_file_is_valid(self):
        """
        Verifica se o arquivo é .c
        :return: bool
        """
        return self.file[-2:] == '.c'

    def count_lines_in_file(self):
        """
        Conta as linhas de código de um arquivo, excluindo as linhas em branco
        :return: int
        """
        loc = 0
        for i in open(self.file):
            if i.strip():
                loc += 1
        return loc
        
    def calculates_n1(self):
        """
        Calcula o n1, que é o número de operadores distintos
        :return: int
        """
        n1 = 0

def main():

    # Trata o argumento pela linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Nome do arquivo", type= str)
    args = parser.parse_args()
    print("Nome do arquivo:", args.file)

    # Cria a classe que fará as metricas
    h = Halstead(args.file)
    print("Arquivo é válido?", h.check_if_file_is_valid())
    print("LOC:", h.count_lines_in_file())
    print("n1:", h.calculates_n1())


if __name__ == "__main__":
    main()
