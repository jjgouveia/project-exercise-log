from src.manipulador_de_log import ManipuladorDeLog


class LogEmArquivo(ManipuladorDeLog):

    def log(msg):
        with open('data/log.txt', mode="w") as file:
            file.write(msg)
