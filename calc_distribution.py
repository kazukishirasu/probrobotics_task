import matplotlib.pyplot as plt
import numpy as np

score = [["完走", "失敗", "失敗", "完走", "完走"],
         ["完走", "完走", "完走", "完走", "完走"]]
score1 = [[], []]
for i in range(1):
    score1[0].extend(score[0])
    score1[1].extend(score[1])
x = np.arange(0, 1.01, step=0.01)
y = []
print("試行回数 : ", len(score1[0]))

# それぞれの試行における結果の表示
def all():
    fig, ax = plt.subplots(2, ncols=int((len(score1[0]) / 2) + 1), tight_layout=True)
    ax = ax.ravel()
    for num in range(int(len(y) / 2)):
        ax[num].plot(x, y[num], color="blue")
        ax[num].plot(x, y[num + len((score1)[0]) + 1], color="red")
        ax[num].set_xlabel("t")
        ax[num].set_ylabel("prob")
        ax[num].set_title(num)
        ax[num].set_xlim(0, 1)
        ax[num].set_ylim(0, 0.1)
        ax[num].set_xticks(np.arange(0.0, 1.5, 0.5))
        ax[num].set_yticks(np.arange(0.0, 0.12, 0.02))
        ax[num].grid(axis="x")
        ax[num].minorticks_on()
        ax[num].grid(which="both", axis="y")

# 最終的な結果の表示
def last():
    plt.plot(x, y[int((len(y) - 1) / 2)], color="blue")
    print("改良前 : ", max(y[int((len(y) - 1) / 2)]))
    plt.plot(x, y[int(len(y) - 1)], color="red")
    print("改良後 : ", max(y[int(len(y) - 1)]))
    plt.xlabel("t")
    plt.ylabel("prob")
    plt.xlim(0, 1.0)
    plt.ylim(0, 0.3)
    plt.xticks(np.arange(0.0, 1.1, 0.1))
    plt.yticks(np.arange(0.0, 0.35, 0.05))
    plt.grid(axis="x")
    plt.minorticks_on()
    plt.grid(which="both", axis="y")

for i in range(len(score1)):
    y.append(np.full_like(x, 1/101))
    # 1回目の事後分布を計算し, リストに追加
    # 完走だった場合
    if score1[i][0] == "完走":
        const = 1 / (sum(x * 1/101))
        t_y = const * x * 1/101
        flag = True
        y.append(t_y)
    # 失敗だった場合
    elif score1[i][0] == "失敗":
        const = 1 / (sum((1 - x) * 1/101))
        f_y = const * (1 - x) * 1/101
        flag = False
        y.append(f_y)
    # 2回目以降の事後分布を計算し, リストに追加
    for j in score1[i][1:]:
        if j == "完走":
            # 一つ前の試行が｢完走｣かつ現在の試行が｢完走｣だった場合
            if flag:
                const = 1/(sum(x * t_y))
                t_y = const * x * t_y
            # 一つ前の試行が｢失敗｣かつ現在の試行が｢完走｣だった場合
            else:
                const = 1/(sum(x * f_y))
                t_y = const * x * f_y
            flag = True
            y.append(t_y)
        elif j == "失敗":
            # 一つ前の試行が｢完走｣かつ現在の試行が｢失敗｣だった場合
            if flag:
                const = 1/(sum((1 - x) * t_y))
                f_y = const * (1 - x) * t_y
            # 一つ前の試行が｢失敗｣かつ現在の試行が｢失敗｣だった場合
            else:
                const = 1/(sum((1 - x) * f_y))
                f_y = const * (1 - x) * f_y
            flag = False
            y.append(f_y)
all()
# last()
plt.show()
