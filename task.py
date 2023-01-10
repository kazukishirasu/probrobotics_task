#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np

score = [["true", "false", "false", "true", "true"], 
         ["true", "true", "true", "true", "true"]]
score1 = [[], []]
for i in range(1):
    score1[0].extend(score[0])
    score1[1].extend(score[1])
x = np.arange(0, 1.01, step=0.01)
y = []
print("試行回数 : ", len(score1[0]))

for i in range(len(score1)):
    y.append(np.full_like(x, 1/101))
    if score1[i][0] == "true":
        const = 1 / (sum(np.arange(0, 1.01, step=0.01) * 1/101))
        t_y = const * np.arange(0, 1.01, step=0.01) * 1/101
        flag = True
        y.append(t_y)
    elif score1[i][0] == "false":
        const = 1 / (sum((1 - np.arange(0, 1.01, step=0.01)) * 1/101))
        f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * 1/101
        flag = False
        y.append(f_y)
    for j in score1[i][1:]:
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
#それぞれでの結果↓
fig, ax = plt.subplots(2, ncols=int((len(score1[0]) / 2) + 1), tight_layout=True)
ax = ax.ravel()
for num in range(int(len(y) / 2)):
    ax[num].plot(x, y[num])
    ax[num].plot(x, y[num + len((score1)[0]) + 1])
    ax[num].set_xlim(0, 1)
    ax[num].set_ylim(0, 0.1)
    ax[num].set_xticks(np.arange(0.0, 1.1, 0.5))
    ax[num].set_yticks(np.arange(0.0, 0.11, 0.02))
    ax[num].grid(axis="x")
    ax[num].minorticks_on()
    ax[num].grid(which = "both", axis="y")

#最後の結果↓
# plt.plot(x, y[int((len(y) - 1) / 2)])
# print("改良前 : ", max(y[int((len(y) - 1) / 2)]))
# plt.plot(x, y[int(len(y) - 1)])
# print("改良後 : ", max(y[int(len(y) - 1)]))
# plt.xlim(0, 1.0)
# plt.ylim(0, 0.3)
# plt.xticks(np.arange(0.0, 1.1, 0.1))
# plt.yticks(np.arange(0.0, 0.35, 0.05))
# plt.grid(axis="x")
# plt.minorticks_on()
# plt.grid(which = "both", axis="y")

plt.show()