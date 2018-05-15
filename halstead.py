"""
O programa calcula as métricas de Halstead e o LOC
na linguagem Python, reconhecendo um arquivo .c.
"""

import math
import time
import argparse  # para argumentos em linha de comando


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
        self.num_uni_operators = 0  # n1
        self.num_uni_operands = 0  # n2
        self.num_tot_operators = 0  # N1
        self.num_tot_operands = 0  # N2
        self.lines_of_code = 0
        self.unique_operators = {}
        self.unique_operands = {}
        self.program_lenght = 0  # N = N1+N2
        self.program_vocabulary = 0  # n = n1+n2
        self.volume = 0  # V = N*log2(n)
        self.difficulty = 0  # D = (n1/2)*(N2/n2)
        self.effort = 0  # E = V*D
        self.program_time = 0  # T = E/18
        self.number_of_bugs = 0  # B = V/3000

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
        #for i in open(self.fi

    def calculates_n1(self):
        """
        Calcula o n1, que é o número de operadores distintos
        :return: int
        """

        return self.num_uni_operators

    def calculates_n2(self):
        """
        Calcula o n2, que é o número de operandos distintos
        :return: int
        """

        return self.num_uni_operands

    def calculates_N1(self):
        """
        Calcula o N1, que é o numero total de operadores
        :return: int
        """

        return self.num_tot_operands

    def calculates_N2(self):
        """
        Calcula o N2, que é o número total de operandos
        :return: int
        """

        return self.num_tot_operands

    def calculates_n(self):
        """
        Calcula o n, que é o vocabulário do programa -> n1+n2
        :return: int
        """
        self.program_vocabulary = self.num_uni_operands + self.num_uni_operators
        return self.program_vocabulary

    def calculates_N(self):
        """
        Calcula o N, que é o tamanho do programa -> N1+N2
        :return: int
        """
        self.program_lenght = self.num_tot_operands + self.num_tot_operators
        return self.program_lenght

    def calculates_V(self):
        """
        Calcula o V, que é o volume do programa -> N * log2 (n)
        :return: float
        """
        if self.program_vocabulary != 0:
            self.volume = (self.program_lenght) * math.log(self.program_vocabulary, 2)
        return self.volume

    def calculates_D(self):
        """
        Calcula o D, que é a dificuldade do programa -> (n1/2) * (N2/n2)
        :return: float
        """
        if self.num_uni_operands != 0:
            self.difficulty = (self.num_uni_operators / 2) * (self.num_tot_operands / self.num_uni_operands)
        return self.difficulty

    def calculates_E(self):
        """
        Calcula o E, que é o esforço do programa -> D * V
        :return: float
        """
        self.effort = self.difficulty * self.volume
        return self.effort

    def calculates_T(self):
        """
        Calcula o T, que é o tempo do programa -> E/18
        :return: float
        """
        self.time = self.effort / 18
        return self.effort

    def calculates_B(self):
        """
        Calcula o B, que é o número de bugs -> V/3000
        :return: float
        """
        self.number_of_bugs = self.volume / 3000
        return self.number_of_bugs


def main():
    # Trata o argumento pela linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Nome do arquivo", type=str)
    args = parser.parse_args()
    print("Nome do arquivo:", args.file)

    # Cria a classe que fará as metricas
    h = Halstead(args.file)
    print("Arquivo é válido?", h.check_if_file_is_valid())
    print("LOC:", h.count_lines_in_file())
    print("n1:", h.calculates_n1())
    print("n2:", h.calculates_n2())
    print("N1:", h.calculates_N1())
    print("N2:", h.calculates_N2())
    print("n:", h.calculates_n())
    print("N:", h.calculates_N())
    print("V:", h.calculates_V())
    print("D:", h.calculates_D())
    print("E:", h.calculates_E())
    print("T:", h.calculates_T())
    print("B:", h.calculates_B())

    #talvez  ^N = n1*log2(n1) + n2*log2(n2)

if __name__ == "__main__":
    main()
