import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

boston = load_boston()

data_boston = pd.DataFrame(boston.data, columns=boston.feature_names)
data_boston['PRICE'] = boston.target

# print(data_boston)

sns.pairplot(data_boston, vars=["PRICE", "RM", "DIS"])
