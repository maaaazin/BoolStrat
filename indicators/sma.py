import pandas as pd
from indicators.base import Indicator

class SMA(Indicator): # Simple Moving Average
    def __init__(self, period: int):
        self.period = period

    def calculate(self, data: pd.DataFrame) -> pd.Series:
        return data["Close"].rolling(window=self.period).mean()