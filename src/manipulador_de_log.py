from abc import ABC, abstractmethod


class ManipuladorDeLog(ABC):
    @abstractmethod
    def log(self, msg):
        pass
   
