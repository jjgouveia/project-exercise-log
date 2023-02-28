from manipulador_de_log import ManipuladorDeLog

class LogEmArquivo(ManipuladorDeLog):
    def __init__(self) -> None:
        super().__init__()

    def log(msg):
        with open('data/log.txt', mode="w") as file:
            file.write(msg)