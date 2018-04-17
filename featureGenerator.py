'''
Generates features from Order Book data
Data format:
    - data_dir folder contains CSVs with order book data for a given stock
    (msft, goog, amzn, aapl) at a given depth (1-10)
    - Order book data is second-by-second
'''
import pandas as pd
import numpy as np

'''
Local path containing data
Raw Data Format:
columns:
    - datetime (YYYY-MM-DD H:M:S)
    - bid{n} n=1:10
    - ask{n} n=1:10
'''
data_dir = '../ProjectData/'


def createFeatures(data_path, out_path):
    '''
    Generates features from Order Book Data

    Inputs:
        - data_path: path to order book data
        - out_path: path to place generated file
    Output:
        - featureMatrix: data frame containing original data and features
    '''
    pass
