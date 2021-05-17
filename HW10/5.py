"""
  Project: Homework 10.5
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 17, 2021
  Detail: 
"""

import numpy as np
import matplotlib.pyplot as plt

# 메인함수
def main():
    X = np.linspace(-8, 8, num=100)    

    # normal_distribution_graph_1 그래프
    mu = 0

    sigma = 0.5
    y1 = gauss(mu, sigma, X)
    plt.plot(X, y1, color="red", label="sigma=0.5")

    sigma = 1
    y2 = gauss(mu, sigma, X)
    plt.plot(X, y2, color="blue", label="sigma=1")

    sigma = 2
    y3 = gauss(mu, sigma, X)
    plt.plot(X, y3, color="green", label="sigma=2")

    plt.title("Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

    # normal_distribution_graph_2 그래프
    sigma = 1

    mu = -2.0
    y1 = gauss(mu, sigma, X)
    plt.plot(X, y1, color="red", label="mu=-2.0")

    mu = 0.0
    y2 = gauss(mu, sigma, X)
    plt.plot(X, y2, color="blue", label="mu=0")

    mu = 2.0
    y3 = gauss(mu, sigma, X)
    plt.plot(X, y3, color="green", label="mu=2.0")

    plt.title("Normal Distribution Graph 2 - mi = [-2.0, 0.0, 2.0], sigma = 1")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

# Y 값 반환
def gauss(mu, sigma, X):
    Y = 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-((X-mu)**2)/(2*sigma**2))
    return Y

if __name__ == "__main__":
    main()