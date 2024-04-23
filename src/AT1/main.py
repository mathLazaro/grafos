import sys

import processing.matrix as mt
from data_inout.convert_to_npdata import *
from data_inout.output_result import *
from data_inout.read_instance import *


def main(instance: str):
    # leitura dos dados
    matrix = list_to_matrix(read_instance(instance))
    # processamento de informações
    matrix_info = mt.get_meta_data(matrix, instance)
    # escrita no console e no arquivo "resultados.txt"
    write_result(matrix_info)


if __name__ == '__main__':
    main(sys.argv[1])
