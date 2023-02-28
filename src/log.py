from src.manipulador_de_log import ManipuladorDeLog


class Log(ManipuladorDeLog):

    def __init__(self, log):
        self.__manipuladores = log[list]

    def log(self):
        return super().log(self)

    def adicionar_manipulador(self):
        self.manipuladores

    def info(self):
        self.log("INFO")

    def alerta(self):
        self.log("ALERTA")

    def erro(self):
        self.log("ERRO")

    def debug(self):
        self.log("DEBUG")

    def __log(self):
        self.log("DEBUG")

    def __formatar(self):
        self.log = ZeroDivisionError