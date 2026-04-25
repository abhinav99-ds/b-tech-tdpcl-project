# data.py
import pandas as pd
import numpy as np

def generate_data(n=1000):
    data = pd.DataFrame({
        "altitude": np.random.randint(20000, 40000, n),
        "speed": np.random.randint(400, 900, n),
        "temperature": np.random.randint(-50, 20, n),
        "weight": np.random.randint(50000, 90000, n),
        "fuel_used": np.random.randint(2000, 8000, n)
    })
    return data

df = generate_data()
df.to_csv("flight_data.csv", index=False)