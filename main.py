from data.loader import DataLoader

loader = DataLoader()

df = loader.load_yahoo(
    ticker="AAPL",
    start="2024-01-01",
    end="2025-01-01",
)

print(df.head())