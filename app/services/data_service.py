from abc import ABC, abstractmethod

class DataService(ABC):
    @abstractmethod
    def load_data(self) -> list[dict]:
        pass