from src.manipulador_de_log import ManipuladorDeLog


class LogEmTela(ManipuladorDeLog):
    def log(msg):
        with open('data/log.txt') as file:
            file.read(msg)
