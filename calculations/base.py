from abc import ABC, abstractmethod


class InvestmentProjectCalculator(ABC):
    """Абстрактный класс."""

    @abstractmethod
    def calc(self):
        pass
