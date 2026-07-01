from data.loader import DataLoader
from indicators import SMA, EMA

loader = DataLoader()

data = loader.load_yahoo(
    ticker="AAPL",
    start="2024-01-01",
    end="2025-01-01",
)

sma20 = SMA(20)
ema50 = EMA(50)

data["SMA20"] = sma20.calculate(data)
data["EMA50"] = ema50.calculate(data)

print(data.tail())