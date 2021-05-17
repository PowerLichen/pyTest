"""
  Project: Homework 10.1
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 17, 2021
  Detail: 정규분포의 난수를 10000개 생성하고 통계분석 후 mu와 sigma 값
          간의 관계를 확인하라
"""

import numpy as np

mu, sigma = map(float, input("mu and sigma(in float) : ").split())
G = np.random.normal(mu, sigma, 10000)

print("mean of G =  {}".format(np.mean(G)))
print("var of G =  {}".format(np.var(G)))
print("std of G =  {}".format(np.std(G)))