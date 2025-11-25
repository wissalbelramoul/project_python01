# utils.py
import pandas as pd
import numpy as np

def generate_monthly_sales(seed=42):
    np.random.seed(seed)
    
   
    dates = pd.date_range("2025-01-01", "2025-12-01", freq="MS")
    
    data = []
    for date in dates:
        row = {
            "Date": date,
            "Product_A": np.random.randint(50, 101),  
            "Product_B": np.random.randint(30, 81),    
            "Product_C": np.random.randint(20, 61),   
            "Product_D": np.random.randint(10, 51),   
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    df.to_csv("data/initial.csv", index=False)
    return df

if __name__ == "__main__":
    generate_monthly_sales()