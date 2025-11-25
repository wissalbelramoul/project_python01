# utils.py
import pandas as pd
import numpy as np


def generate_random_sales(min_val, max_val, size, seed=None):
   
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_val, max_val + 1, size)


def generate_monthly_sales(seed=42):
   
    np.random.seed(seed)

    dates = pd.date_range("2025-01-01", "2025-12-01", freq="MS")

    data = {
        "Date": dates,
        "Product_A": generate_random_sales(50, 100, 12),
        "Product_B": generate_random_sales(30, 80, 12),
        "Product_C": generate_random_sales(20, 60, 12),
        "Product_D": generate_random_sales(10, 50, 12)
    }

    df = pd.DataFrame(data)
    df.to_csv("data/initial.csv", index=False)
    return df


if __name__ == "__main__":
    generate_monthly_sales()
