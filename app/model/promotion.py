from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, promo_id: str):
        self.promo_id = promo_id

    @abstractmethod
    def apply(self, total: float) -> float:
        pass