from src.load_data import load_sentiment_data
from src.load_data import load_trader_data

from src.preprocess import preprocess_sentiment
from src.preprocess import preprocess_trader

from src.merge_data import merge_datasets

from src.analysis import analyze_data

from src.visualization import create_all_visualizations

def main():

    print("=" * 50)
    print("PRIME TRADE DATA ANALYSIS")
    print("=" * 50)

    # Load datasets
    sentiment = load_sentiment_data()
    trader = load_trader_data()

    # Clean datasets
    sentiment = preprocess_sentiment(sentiment)
    trader = preprocess_trader(trader)

    # Merge
    merged = merge_datasets(trader, sentiment)

    print("\nMerged Dataset Shape:")
    print(merged.shape)
    
    print("\nFirst Five Rows:")
    print(merged.head())

    analyze_data(merged)
    
    create_all_visualizations(merged)

    print("\nMerged Dataset Shape:")
    print(merged.shape)

    print("\nFirst Five Rows:")
    print(merged.head())


if __name__ == "__main__":
    main()