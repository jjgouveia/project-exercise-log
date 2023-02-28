from src.manipulador_de_log import ManipuladorDeLog


class Log(ManipuladorDeLog):

    def __init__(self):
        super().__init__()
        self.manipuladores = []

    def adicionar_manipulador(self, msg):
        self.manipuladores.append(msg)

    def info(self):
        self.log("INFO")

    def alerta(self):
        self.log("ALERTA")

    def erro(self):
        self.log("ERRO")

    def debug(self):
        self.log("DEBUG")
