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
        - volume
        - last_price
        - mid
        - spread
        - wmid
        - last_size
        - last_SRO
'''

data_dir = '../../ProjectData/'


def createResponseVariable(data, response_type = 'Classification'):
    '''
    Generates response variable for raw input data.
    Response variable will be:
        - mid price of next tick order book (response_type = 'Regression')
        - Up , Down, No Change (response_type = 'Classification')
    '''
    if response_type.upper() == 'REGRESSION':
        response_col = [data.loc[i+1, 'direct.mid'] for i in range(len(data)-1)]

    elif response_type.upper() == 'CLASSIFICATION':
        response_col = []
        for i in range(len(data)-1):
            current_price = data.loc[i, 'direct.mid']
            next_price = data.loc[i+1, 'direct.mid']
            diff = next_price - current_price
            if diff == 0:
                response_col.append(0)
            elif diff > 0:
                response_col.append(1)
            elif diff < 0:
                response_col.append(2)

    data = data[:-1] # get rid of last row, which won't have a response variable
    data['Response'] = response_col
    return data

def calculateImbalance(data):
    '''
    Calulate Order Book imbalance
    '''
    pass

def createFeatures(data_path, out_path, response_type):
    '''
    Generates features from Order Book Data

    Inputs:
        - data_path: path to order book data
        - out_path: path to place generated file
    Output:
        - featureMatrix: data frame containing original data and features
    '''
    data = pd.read_csv(data_path)
    #data = calculateImbalance(data)
    data = createResponseVariable(data, response_type)
    data.to_csv(out_path, index = False)
