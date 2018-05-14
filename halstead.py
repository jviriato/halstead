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
        self.num_operators    = 0
        self.num_operands     = 0
        self.lines_of_code    = 0
        self.unique_operators = {}
        self.unique_operands  = {}

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
        self.lines_of_code = 0
        for i in open(self.file):
            if i.strip():
                self.lines_of_code += 1
        return self.lines_of_code

    def find_operators_and_operands(self):
        """
        Acha os operadores e operandos distintos do .c para os
        respectivos vetores
        :return: void
        """
        for i in open(self.file):


    def calculates_n1(self):
        """
        Calcula o n1, que é o número de operadores distintos
        :return: int
        """

        return self.num_operators

    def calculates_n2(self):
        """
        Calcula o n2, que é o número de operandos distintos
        :return: int
        """

        return self.num_operands

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
    print("n2:", h.calculates_n2())

if __name__ == "__main__":
    main()
