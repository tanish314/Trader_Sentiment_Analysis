import pandas as pd


def analyze_data(df):

    print("\n" + "="*60)
    print("DATA ANALYSIS")
    print("="*60)

    # --------------------------
    # Total Trades
    # --------------------------
    total_trades = len(df)

    print(f"\nTotal Trades : {total_trades}")

    # --------------------------
    # Total Profit
    # --------------------------

    total_profit = df["Closed PnL"].sum()

    print(f"Total Profit/Loss : {total_profit:.2f}")

    # --------------------------
    # Average Profit
    # --------------------------

    avg_profit = df["Closed PnL"].mean()

    print(f"Average Profit : {avg_profit:.2f}")

    # --------------------------
    # Win Rate
    # --------------------------

    wins = (df["Closed PnL"] > 0).sum()

    win_rate = (wins / total_trades) * 100

    print(f"Win Rate : {win_rate:.2f}%")

    # --------------------------
    # Top Coins
    # --------------------------

    print("\nTop 10 Most Traded Coins")

    print(df["Coin"].value_counts().head(10))

    # --------------------------
    # Top Traders
    # --------------------------

    print("\nTop 10 Traders by Profit")

    top_traders = df.groupby("Account")["Closed PnL"].sum()

    print(top_traders.sort_values(ascending=False).head(10))

    # --------------------------
    # Profit by Sentiment
    # --------------------------

    print("\nAverage Profit by Sentiment")

    print(
        df.groupby("classification")["Closed PnL"].mean()
    )

    print("\nTotal Profit by Sentiment")

    print(
        df.groupby("classification")["Closed PnL"].sum()
    )