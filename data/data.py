import pandas as pd

def product():
    product = pd.read_csv('product.csv')
    del product['Unnamed: 0']
    return product
def validation():
    validation = pd.read_csv('product.csv')
    del validation['Unnamed: 0']
    return validation
def feedback():
    feedback = pd.read_csv('product.csv')
    del feedback['Unnamed: 0']
    return feedback