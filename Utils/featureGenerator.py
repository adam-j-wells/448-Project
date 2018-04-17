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
Raw Data Format:
    columns (n=1:10):
        - datetime (YYYY-MM-DD H:M:S)
        - bid{n}
        - ask{n}
        - bsize{n}
        - asize{n}
        - bnum{n}
        - anum{n}
        - vwap
        - notional
        - volumne
        - last_price
        - mid
        - spread
        - wmid
        - last_size
        - last_SRO
'''

data_dir = '../../ProjectData/'


def calculateImbalance(data):
    '''
    Calulate Order Book imbalance
    '''
    pass

def createFeatures(data_path, out_path):
    '''
    Generates features from Order Book Data

    Inputs:
        - data_path: path to order book data
        - out_path: path to place generated file
    Output:
        - featureMatrix: data frame containing original data and features
    '''
    data = pd.read_csv(data_path)
    data = calculateImbalance(data)
