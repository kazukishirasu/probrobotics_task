#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

score = [["true", "false", "false", "true", "true"], 
         ["true", "true", "true", "true", "true"]]
x = np.arange(0, 1.01, step=0.01)
y = []

for i in range(len(score)):
    y.append(np.full_like(x, 1/101))
    if score[i][0] == "true":
        const = 1 / (sum(np.arange(0, 1.01, step=0.01) * 1/101))
        t_y = const * np.arange(0, 1.01, step=0.01) * 1/101
        flag = True
        y.append(t_y)
    elif score[i][0] == "false":
        const = 1 / (sum((1 - np.arange(0, 1.01, step=0.01)) * 1/101))
        f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * 1/101
        flag = False
        y.append(f_y)
    for j in score[i][1:]:
        if j == "true":
            if flag:
                const = 1/(sum(np.arange(0, 1.01, step=0.01) * t_y))
                t_y = const * np.arange(0, 1.01, step=0.01) * t_y
            else:
                const = 1/(sum(np.arange(0, 1.01, step=0.01) * f_y))
                t_y = const * np.arange(0, 1.01, step=0.01) * f_y
            flag = True
            y.append(t_y)
        elif j == "false":
            if flag:
                const = 1/(sum((1 - np.arange(0, 1.01, step=0.01)) * t_y))
                f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * t_y
            else:
                const = 1/(sum((1 - np.arange(0, 1.01, step=0.01)) * f_y))
                f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * f_y
            flag = False
            y.append(f_y)
print(y)
fig, ax = plt.subplots(2, 3, tight_layout=True)
ax = ax.ravel()
for num in range(int(len(y) / 2)):
    ax[num].plot(x, y[num])
    ax[num].plot(x, y[num + 6])
    ax[num].set_xlim(0, 1)
    ax[num].set_ylim(0, 0.1)
    ax[num].minorticks_on()
    ax[num].grid(axis="x")
    ax[num].grid(which = "both", axis="y")
plt.show()