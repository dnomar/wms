import abc

class EventTransformer(abc.ABC):

    @abc.abstractmethod
    def write(self):
        raise NotImplementedError

    @abc.abstractmethod
    def read(self):
        raise NotImplementedError
