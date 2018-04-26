import math
import argparse # para argumentos em linha de comando

class Halstead:

    def __init__(self, file):
        self.file = file
        self.num_operators = 0
        self.num_operands  = 0
        self.lines_of_code = 0

    def check_if_file_is_valid(self):
        return(self.file[-1] == 'c' and self.file[-2] == '.')

def main():

    #Trata o argumento pela linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Nome do arquivo", type= str)
    args = parser.parse_args()
    print(args.file)

    #Cria a classe que fará as verificações
    h = Halstead(args.file)
    print(h.check_if_file_is_valid())



if __name__ == "__main__":
    main()