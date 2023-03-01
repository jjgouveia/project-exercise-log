from src.manipulador_de_log import ManipuladorDeLog


class LogEmArquivo(ManipuladorDeLog):

    def log(self, msg):
        with open('data/log.txt', mode="w") as file:
            file.write(msg)
