def write_result(result: str):
    path = "files/results/log.txt"

    # escreve o resultado no arquivo "
    with open(path, "a") as file:
        file.write(f'{result} \n\n')

    # printa o resultado no terminal
    print("\n" + str(result) + "\n")
