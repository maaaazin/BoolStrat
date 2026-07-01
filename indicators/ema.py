import pandas as pd
from indicators.base import Indicator

class EMA(Indicator): # Exponential Moving Average
    def __init__(self, period: int):
        self.period = period

    def calculate(self, data: pd.DataFrame) -> pd.Series:
        return data["Close"].ewm(span=self.period, adjust=False).mean()