import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.loc[df['target'] == 0, 'target'] = 'setosa'
df.loc[df['target'] == 1, 'target'] = 'vasicolor'
df.loc[df['target'] == 2, 'target'] = 'virginica'

plt.scatter(df['sepal length (cm)'], df['petal length (cm)'])
plt.show()

sns.jointplot('sepal length (cm)', 'petal length (cm)', data=df)
