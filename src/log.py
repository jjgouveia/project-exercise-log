from datetime import datetime


class Log():

    def __init__(self, log: list):
        self.__manipuladores = set(log)

    def adicionar_manipulador(self, log):
        self.__manipuladores.add(log)

    def info(self, msg):
        self.__log("INFO", msg)

    def alerta(self, msg):
        self.__log("ALERTA", msg)

    def erro(self, msg):
        self.__log("ERRO", msg)

    def debug(self, msg):
        self.__log("DEBUG", msg)

    def __log(self, type, msg):
        for manipulador in self.__manipuladores:
            manipulador.log(self.__formatar(type, msg))

    def __formatar(self, type, msg):
        info = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return f'[{type} - {info}]: {msg}'
