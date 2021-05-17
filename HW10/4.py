"""
  Project: Homework 10.4
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 17, 2021
  Detail: 싸인파 그래프를 pyplot 모듈을 사용하여 출력
"""

import numpy as np
import matplotlib.pyplot as plt

# 싸인파 그래프
def sine_graph(amp, freq, theta, pattern):
    x = np.linspace(-np.pi, np.pi, num=41)
    y = amp * np.sin(freq * x + theta)
    plt.plot(x, y, "k--", x, y, pattern)


    # y 극대 극소점 확인 후 y축 범위 재할당
    xmin, xmax, ymin, ymax = x[0], x[-1], y.min(), y.max()
    plt_y_scale = plt.ylim()
    if plt_y_scale[0] > ymin and plt_y_scale[1] < ymax:
        plt.axis([xmin, xmax, ymin, ymax])

# 입력된 그래프 출력
def plot_showing():
    plt.xlabel("x")
    plt.ylabel("sin(freq * x + theta)")
    plt.title("Example of matplotlib - sin(freq * x + theta)")
    plt.grid(True)
    plt.show()




if __name__ == "__main__":
    sine_graph(1,2,0,"ro")
    sine_graph(1,2,np.pi/2,"bo")
    sine_graph(1,2,np.pi,"go")

    plot_showing()