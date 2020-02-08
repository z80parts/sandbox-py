from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

x = [1, 2, 3, 4]
y = [2, 5, 7, 9]

plt.plot(x, y)
plt.show()

sns.lineplot(x, y)
