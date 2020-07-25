import abc

class AbstracMessage(abc.ABC):

    @abc.abstractmethod
    def send(self, contact:str, body:str):
        raise NotImplementedError
