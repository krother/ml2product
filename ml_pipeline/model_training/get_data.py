"""
Retrieve data from REST API

adapted from code by Lennard Böckenförde and Marie Mink

https://github.com/Pf4rR3R/ppi_implementation

Distributed under the conditions of the MIT License
"""

import requests
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

BASE_URL = "http://127.0.0.1:8000"


def get_number_of_chunks():
    url = f"{BASE_URL}/n_chunks"
    response = requests.get(url)
    n_chunks = response.json()["chunks"]
    return n_chunks


def get_clean_chunk(chunk):
    """
    the json file comes with an extra pair of quotes
    that needs to be replaced in order to read the chunk content
    """
    url = f"{BASE_URL}/chunk/{chunk}"
    response = requests.get(url)
    text = response.text
    cleaned_text = text[1:-1].replace("\\", "")
    df = pd.read_json(cleaned_text)
    return df


def load_and_sort_data(n_chunks=None):
    """
    Loads chunks and sorts them into train / test according to their index
    """
    if n_chunks is None:
        n_chunks = get_number_of_chunks()
    else:
        n_chunks = min([n_chunks, get_number_of_chunks()])

    mega_train = []
    mega_test = []
    for i in range(n_chunks):
        # adds every chunk with an even number to test data and every chunk with an uneven number to train data
        if int(i) % 2 == 0:
            mega_test.append(get_clean_chunk(i))
        else:
            mega_train.append(get_clean_chunk(i))

    return pd.concat(mega_train), pd.concat(mega_test)


if __name__ == "__main__":
    n_chunks = get_number_of_chunks()
    print(f"downloading {n_chunks} chunks")
    train_df, test_df = load_and_sort_data(n_chunks)
    print("train shape:", train_df.shape)
    print("test shape:", test_df.shape)
