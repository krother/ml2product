"""
Slightly modifies the data and packages it into chunks.
"""
import pandas as pd
import numpy as np
import math
import time
import os

START_TIME = "2022-10-11 9:00"
N_PERIODS = 80

np.random.seed(42)

path = os.path.split(__file__)[0]
filename = os.path.join("data_ex.csv")

df = pd.read_csv(filename, index_col=0)

# insert rare NaNs but not in first chunk
mask = np.random.randint(1, 504, size=df.shape[0])
mask = mask == 1
df.loc[mask, "gender"] = None

# insert rare outliers (data errors)
mask = np.random.randint(1, 234, size=df.shape[0])
mask = mask == 1
df.loc[mask, "age_of_car_M"] *= 99

# apply constant bias to car power
df["Car_power_M"] += math.pi * 8

# apply multiplier to one column
df["Insuredcapital_continent_re"] *= 2

# Claims1, Claims2: upwards drift
df["Claims1x"] = (
    df["Claims1"] + np.random.normal(size=df.shape[0]) * df["Claims1"].max() * 0.05
)
df.sort_values(by="Claims1x", inplace=True)
df.reset_index(inplace=True)
del df["Claims1x"]
del df["index"]

# create timestamps with chunk release dates
ts = pd.date_range(START_TIME, freq="1h", periods=N_PERIODS)

# divide data into chunks
N = df.shape[0]
size_of_chunks = N // N_PERIODS
index_for_chunks = list(range(0, N, size_of_chunks))
index_for_chunks.extend([N + 1])

chunks = {}
for i in range(len(index_for_chunks) - 1):
    chunks[i] = df.iloc[index_for_chunks[i] : index_for_chunks[i + 1]]


def get_number_of_chunks():
    # count the number of chunks past current time
    active = ts < time.asctime()
    n_active = active.sum()
    return int(n_active)


def get_chunk(i):
    active = ts < time.asctime()
    n_active = active.sum()
    if i < n_active:
        return chunks[i].to_json(orient="records")
    else:
        return None
