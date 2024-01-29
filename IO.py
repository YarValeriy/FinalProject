from abc import ABC, abstractmethod


class IO(ABC):
    @abstractmethod
    def print(self, *args, **kwargs):
        pass

    @abstractmethod
    def input(self, *args):
        pass


class Consol_io(IO):
    def print(self, *args, **kwargs):
        print(*args, **kwargs)

    def input(self, *args):
        return input(*args)
