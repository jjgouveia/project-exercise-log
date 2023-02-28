from src.manipulador_de_log import ManipuladorDeLog


class Log(ManipuladorDeLog):

    def __init__(self, log: set):
        self.__manipuladores = log

    def log(self, msg):
        return super().log(self)

    def adicionar_manipulador(self, msg):
        self.__manipuladores

    def info(self, msg):
        self.log("INFO")

    def alerta(self, msg):
        self.log("ALERTA")

    def erro(self, msg):
        self.log("ERRO")

    def debug(self, msg):
        self.log("DEBUG")

    def __log(self):
        self.log("DEBUG")

    def __formatar(self):
        self.log = ZeroDivisionError