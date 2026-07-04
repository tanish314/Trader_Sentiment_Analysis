import pandas as pd
import os

# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")


def load_sentiment_data():
    """
    Load Bitcoin Fear & Greed dataset
    """
    file_path = os.path.join(RAW_DATA, "fear_greed_index.csv")

    sentiment = pd.read_csv(file_path)

    print("Sentiment Dataset Loaded Successfully")
    print(sentiment.head())

    return sentiment


def load_trader_data():
    """
    Load Historical Trader dataset
    """
    file_path = os.path.join(RAW_DATA, "historical_data.csv")

    trader = pd.read_csv(file_path)

    print("Trader Dataset Loaded Successfully")
    print(trader.head())

    return trader