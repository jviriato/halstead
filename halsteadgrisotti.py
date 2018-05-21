# -*- coding: utf-8 -*-
import string
import re
"""
O programa calcula as métricas de Halstead e o LOC
na linguagem Python, reconhecendo um arquivo .c.
"""

import math
import argparse  # para argumentos em linha de comando
import re        # para expressões regulares

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
        self.num_uni_operators  = 0  # n1
        self.num_uni_operands   = 0  # n2
        self.num_tot_operators  = 0  # N1
        self.num_tot_operands   = 0  # N2
        self.lines_of_code      = 0
        self.operators          = []
        self.operands           = []
        self.unique_operators   = []
        self.unique_operands    = []
        self.total_operators    = []
        self.total_operands     = []
        self.functions          = []
        self.program_lenght     = 0  # N = N1+N2
        self.program_vocabulary = 0  # n = n1+n2
        self.volume             = 0  # V = N*log2(n)
        self.difficulty         = 0  # D = (n1/2)*(N2/n2)
        self.effort             = 0  # E = V*D
        self.program_time       = 0  # T = E/18
        self.number_of_bugs     = 0  # B = V/3000

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

    def search(self):
        """
        Função que procura os nomes das funções que são operadores.
        :return: void
        """
        #print("\nFunções presentes no código: (em stack)\n")
        stack_of_functions = []
        with open(self.file) as f:
            lines = f.readlines()
            #print(lines)
            for line in lines:
                regex = re.compile(r"(unsigned |signed |long |short )*(int|float|char|long|short|signed|unsigned|double|void|bool)+['*']*[' ']+['*']*[\w]+[' ']*['(']")
                p = regex.match(line)
                if p:
                    stack_of_functions.append(p.group())
                    self.functions.append(p.group())
                    #print(stack_of_functions)
        #print("Quantidade funções: " + str(len(self.functions)))

    def find_total_operators_and_operands(self):
        """
        Acha os operadores e operandos distintos do .c para os
        respectivos vetores
        :return: void
        """
        self.operators = ['unsigned', 'signed', 'long', 'short', 'int', 'float',
                          'char', 'double', 'void', 'bool', 'break', 'case',
                          'continue', 'default', 'do', 'if', 'enum', 'for',
                          'goto', 'if', 'return', 'else', 'sizeof', 'struct',
                          'switch', 'while', 'scanf', 'printf', '>>=', '<<=', '+=',
                          '-=', '=+', '=-', '*=', '=*', '/=', '=/', '%=', '=%', '&=',
                          '=&', '^=', '|=', '>>', '<<', '++', '--', '->', '&&', '||',
                          '<=', '>=', '==', '!=', ';', ',', ';', '=', '.', '&', '!',
                          '~', '-', '+', '*', '/', '%', '<', '>', '^', '|', '?', ':']
                            # Outros elementos:
                            # '{}', '()', '[]', '? :'

        self.search() # Procura os nomes das funções
        #Trata a linha dos nomes
        for i, operator in enumerate(self.functions):
            self.functions[i] = operator.split()

        for operator in self.functions:
            for each in operator:
                if each in self.operators:
                    self.total_operators.append(each)
                elif each == "(":
                    self.total_operators.append(each+")")
                else: # nome de função ou tem ponteiro junto ou tem parenteses junto
                    if re.search(".*", each): #tem ponteiro
                        if each[-1] == '*':
                            each = each.replace('*', '')
                            self.total_operators.append(each)
                            self.total_operators.append('*')
                        elif each[0] == '*' and each[-1] == '(':
                            each = each.replace('*', '')
                            each = each.replace('(', '')
                            self.total_operators.append(each)
                            self.total_operators.append('*')
                            self.total_operators.append('()')
                        elif each[0] == '*':
                            each = each.replace('*', '')
                            self.total_operators.append(each)
                            self.total_operators.append('*')
                        elif each[-1] == '(':
                            each = each.replace('(', '')
                            self.total_operators.append(each)
                            self.total_operators.append('()')
                        else:
                            self.total_operators.append(each)

        for i, operator in enumerate(self.functions):
            self.functions[i] = (" ").join(operator)

        #Trata as linhas do código
        with open(self.file) as f:
            lines = f.readlines()
            indexline = 0
            for line in lines:
                if re.search('#include', line):    #include
                    pass
                elif line == '\n':                 #linha em branco
                    pass
                elif line[0] == '/':               #comentário
                    pass
                elif line[0] == '{':               #ignora }, porque pra cada { tem um }
                    self.total_operators.append("{}")
                elif re.search("//", line):
                    pass
                else:                              #linha de código normal
                    for function in self.functions:
                        if line.find(function) > -1:  #definição de função e falta coisa para ser tratada
                            #print(function)
                            #print(line)
                            pos = line.find('(')
                            #print(line[pos + 1:])
                            temp = line[pos + 1:]
                            #regex = re.compile(r"(unsigned |signed |long |short)*(int|float|char|long|short|signed|unsigned|double|void|bool)+([' ']+['*']*[\w]+[', ']*)*[')']+['{']*")
                            #p = regex.match(temp)
                            #print(p)
                    index = 0
                    start = -1
                    end = -1
                    for letter in line:  # pega a chamada de funções e coloca nos operators
                        if letter == '(':
                            end = index
                            break
                        if letter == ' ':
                            if line[index + 1] == '(':
                                pass
                            else:
                                start = index + 1
                        index += 1
                    #print(line)
                    if start != -1 & end != -1:
                        word = line[start:index]
                        self.total_operators.append(word)
                        #print(word)
                    else:
                        word = " "

                    if word == "printf" or word == "scanf":  # pega o conteudo entre as "" do printf e scanf, e coloca nos operands
                        #print("linha:", line)
                        start = -1
                        end = -1
                        index = 0
                        for letter in line:
                            if letter == '"':
                                if start == -1:
                                    start = index + 1
                                else:
                                    end = index
                            index += 1
                        word3 = line[start:end]
                        self.total_operands.append(word3)
                        if line.find('",') != -1:#pega os parametros do scanf e printf e coloca nos operands
                            pos = line.find("\",")
                            #print(line[pos + 1:])
                            word = line[pos + 1:]
                            regex = re.compile(r"['&']*[\w]+")
                            p = regex.findall(word)
                            #print(p)
                            self.total_operands.extend(p)
                    elif word != " ": #pega os parametros das outras funções e coloca nos operands
                        parameters = line[end:]
                        regex = re.compile(r"['&']*['*']*[\w]+")
                        p = regex.findall(parameters)
                        for i in p:
                            if i in self.operators:
                                pass
                            else:
                                self.total_operands.append(i)
                    for words in line.split():
                        if words in self.operators:
                            self.total_operators.append(words)
                    for letter in line:
                        if letter == '{':
                            self.total_operators.append("{}")
                        if letter == '(':
                            self.total_operators.append("()")
                        if letter == '[':
                            self.total_operators.append("[]")

                    #ta faltando conseguir pegar as declarações de int, float etc de variaveis, n descobri como, tipo...
                    #int i, j;
                    #colocar o 'i' e 'j' nos operandos, n consegui fazer isso
                    indexline += 1






                    #print(line)








    def find_unique_operators_and_operands(self):
        """
        Acha os operandos e operadores únicos, n1 e n2
        :return: void
        """
        self.unique_operators = set(self.total_operators)
        self.unique_operands = set(self.total_operands)

    def calculates_n1(self):
        """
        Calcula o n1, que é o número de operadores distintos
        :return: int
        """
        self.num_uni_operators = len(self.unique_operators)  # pode ser trocado se for outra implementação

        return self.num_uni_operators

    def calculates_n2(self):
        """
        Calcula o n2, que é o número de operandos distintos
        :return: int
        """
        self.num_uni_operands = len(self.unique_operands)  # pode ser trocado se for outra implementação

        return self.num_uni_operands

    def calculates_N1(self):
        """
        Calcula o N1, que é o numero total de operadores
        :return: int
        """
        self.num_tot_operators = len(self.total_operators)  # pode ser trocado se for outra implementação
        return self.num_tot_operators

    def calculates_N2(self):
        """
        Calcula o N2, que é o número total de operandos
        :return: int
        """
        self.num_tot_operands = len(self.total_operands)  # pode ser trocado se for outra implementação

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

        return self.time

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
    h.find_total_operators_and_operands()
    h.find_unique_operators_and_operands()
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


if __name__ == "__main__":
    main()
