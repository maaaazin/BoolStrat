from data.loader import DataLoader
from strategies.sma_cross import SMACrossoverStrategy

loader = DataLoader()

data = loader.load_yahoo(
    "AAPL",
    "2024-01-01",
    "2025-01-01",
)

strategy = SMACrossoverStrategy()

signals = strategy.generate_signals(data)

print(signals.tail())