import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_DIR = os.path.join(BASE_DIR, "data", "processed")


def merge_datasets(trader, sentiment):

    merged = pd.merge(
        trader,
        sentiment,
        on="date",
        how="left"
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, "merged_data.csv")

    merged.to_csv(output_path, index=False)

    print("\nMerged dataset created successfully.")
    print("Saved to:")
    print(output_path)

    return merged