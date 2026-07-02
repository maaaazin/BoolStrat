from abc import ABC, abstractmethod
import pandas as pd

class Strategy(ABC): # Base class for all strategies.
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Takes market data and returns the same DataFrame
        with trading signals.
        """
        pass