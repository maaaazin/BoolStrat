import pandas as pd
from indicators import SMA
from strategies.base import Strategy

class SMACrossoverStrategy(Strategy):
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df["SMA_SHORT"] = SMA(self.short_window).calculate(df)
        df["SMA_LONG"] = SMA(self.long_window).calculate(df)
        df["Signal"] = 0

        current = df["SMA_SHORT"] > df["SMA_LONG"]
        previous = current.shift(1)

        # buy on bullish crossover
        df.loc[current & ~previous.fillna(False), "Signal"] = 1

        # sell on bearish crossover
        df.loc[(~current) & previous.fillna(False), "Signal"] = -1
        return df