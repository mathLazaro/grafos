import sys

import data_inout.input_data as din
import data_inout.output_result as dout
import processing.matrix as mt


def main(instance: str):
    matrix = din.read_instance(instance)                # leitura dos dados
    matrix_info = mt.get_meta_data(matrix, instance)    # processamento de informações
    dout.write_result(matrix_info)                      # escrita no console e no arquivo "resultados.txt"


if __name__ == '__main__':
    main(sys.argv[1])
