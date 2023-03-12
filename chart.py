import matplotlib.pyplot as plt
import numpy as np
def show_chart(money):
    x = np.arange(len(money))
    y = money
    plt.title("Virtualization of spending money")
    plt.xlabel("Number of sales")
    plt.ylabel("Money")
    plt.plot(x,y)
    plt.show()