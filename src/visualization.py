import os
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set_style("whitegrid")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_DIR = os.path.join(BASE_DIR, "reports", "images")

os.makedirs(IMAGE_DIR, exist_ok=True)


def plot_sentiment_distribution(df):

    plt.figure(figsize=(8,5))

    sns.countplot(
        data=df,
        x="classification",
        order=df["classification"].value_counts().index
    )

    plt.title("Market Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "sentiment_distribution.png"))
    plt.show()


def plot_profit_distribution(df):

    plt.figure(figsize=(8,5))

    sns.histplot(df["Closed PnL"], bins=40)

    plt.title("Closed PnL Distribution")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "profit_distribution.png"))
    plt.show()


def plot_profit_by_sentiment(df):

    plt.figure(figsize=(8,5))

    sns.barplot(
        data=df,
        x="classification",
        y="Closed PnL",
        estimator="mean"
    )

    plt.title("Average Profit by Sentiment")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "profit_by_sentiment.png"))
    plt.show()


def plot_top_coins(df):

    plt.figure(figsize=(10,5))

    df["Coin"].value_counts().head(10).plot(kind="bar")

    plt.title("Top 10 Traded Coins")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "top_coins.png"))
    plt.show()


def plot_top_traders(df):

    trader_profit = (
        df.groupby("Account")["Closed PnL"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10,5))

    trader_profit.plot(kind="bar")

    plt.title("Top 10 Traders")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "top_traders.png"))
    plt.show()


def plot_buy_sell(df):

    plt.figure(figsize=(6,5))

    sns.countplot(
        data=df,
        x="Side"
    )

    plt.title("Buy vs Sell Trades")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "buy_sell.png"))
    plt.show()


def plot_boxplot(df):

    plt.figure(figsize=(8,5))

    sns.boxplot(
        data=df,
        x="classification",
        y="Closed PnL"
    )

    plt.title("Profit vs Sentiment")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "boxplot.png"))
    plt.show()


def plot_heatmap(df):

    numeric = df.select_dtypes(include="number")

    plt.figure(figsize=(10,8))

    sns.heatmap(
        numeric.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(os.path.join(IMAGE_DIR, "heatmap.png"))
    plt.show()


def create_all_visualizations(df):

    print("\nGenerating Graphs...")

    plot_sentiment_distribution(df)

    plot_profit_distribution(df)

    plot_profit_by_sentiment(df)

    plot_top_coins(df)

    plot_top_traders(df)

    plot_buy_sell(df)

    plot_boxplot(df)

    plot_heatmap(df)

    print("\nGraphs Saved Successfully!")