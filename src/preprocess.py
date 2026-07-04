import pandas as pd


def preprocess_sentiment(sentiment):
    sentiment = sentiment.copy()

    # Convert date column
    sentiment["date"] = pd.to_datetime(sentiment["date"]).dt.date

    # Remove duplicates
    sentiment = sentiment.drop_duplicates()

    # Remove missing values
    sentiment = sentiment.dropna()

    return sentiment


def preprocess_trader(trader):
    trader = trader.copy()

    # Convert Unix timestamp (milliseconds) to datetime
    trader["Timestamp"] = pd.to_datetime(trader["Timestamp"], unit="ms")

    # Create date column
    trader["date"] = trader["Timestamp"].dt.date

    trader = trader.drop_duplicates()
    trader = trader.dropna(how="all")

    print("\nTrader Date Range:")
    print("Min Date:", trader["date"].min())
    print("Max Date:", trader["date"].max())

    return trader