import os

INSTANCES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'files/instances')) + '/'


def read_instance(instance: str) -> list:
    # caminho relativo da instância
    relative = INSTANCES_PATH + instance + ".txt"
    # dados lidos
    data = []

    # verifica a existência do diretório dado
    if not os.path.exists(relative):
        raise Exception("Não existe o diretório: "
                        + str(relative))

    # lê cada linha do arquivo, sendo que cada linha é
    with open(relative, "r") as file:
        for line in file:
            data.append(line.strip().split(" "))

    return data
