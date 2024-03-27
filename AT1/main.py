import sys

import data_inout.input_data as din
import data_inout.output_result as dout
import processing.matrix as mt


def main(instance: str):
    # leitura dos dados
    matrix = din.read_instance(instance)
    # processamento de informações
    matrix_info = mt.get_meta_data(matrix, instance)
    # escrita no console e no arquivo "resultados.txt"
    dout.write_result(matrix_info)


if __name__ == '__main__':
    main(sys.argv[1])
