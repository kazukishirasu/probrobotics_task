#!/usr/bin/python3
# coding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

score = ["true", "false", "false", "true", "true"]
# score = ["true", "true", "true", "true", "true"]
x = np.arange(0, 1.01, step=0.01)
y = []

if score[0] == "true":
    const = 1 / (sum(np.arange(0, 1.01, step=0.01) * 1/101))
    t_y = const * np.arange(0, 1.01, step=0.01) * 1/101
    # print(t_y)
    flag = True
    y.append(t_y)
elif score[0] == "false":
    const = 1 / (sum((1 - np.arange(0, 1.01, step=0.01)) * 1/101))
    f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * 1/101
    # print(f_y)
    flag = False
    y.append(f_y)

for i in score[1:]:
    if i == "true":
        if flag:
            const = 1/(sum(np.arange(0, 1.01, step=0.01) * t_y))
            t_y = const * np.arange(0, 1.01, step=0.01) * t_y
            # print(t_y)
        else:
            const = 1/(sum(np.arange(0, 1.01, step=0.01) * f_y))
            t_y = const * np.arange(0, 1.01, step=0.01) * f_y
            # print(t_y)
        flag = True
        y.append(t_y)
    elif i == "false":
        if flag:
            const = 1/(sum((1 - np.arange(0, 1.01, step=0.01)) * t_y))
            f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * t_y
            # print(f_y)
        else:
            const = 1/(sum((1 - np.arange(0, 1.01, step=0.01)) * f_y))
            f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * f_y
            # print(f_y)
        flag = False
        y.append(f_y)
print(y)
fig, ax = plt.subplots(2, 3, sharex="all", sharey="all", tight_layout=True)
x0 = [0, 1]
y0 = [1/101, 1/101]
ax[0, 0].plot(x0, y0)
ax[0, 0].set_xlabel("t")
ax[0, 0].set_ylabel("確率")
ax[0, 0].set_xlim(0, 1)
ax[0, 0].set_ylim(0, 0.1)
ax[0, 0].grid()
ax[0, 1].plot(x, y[0])
ax[0, 1].grid()
ax[0, 2].plot(x, y[1])
ax[0, 2].grid()
ax[1, 0].plot(x, y[2])
ax[1, 0].grid()
ax[1, 1].plot(x, y[3])
ax[1, 1].grid()
ax[1, 2].plot(x, y[4])
ax[1, 2].grid()
plt.show()