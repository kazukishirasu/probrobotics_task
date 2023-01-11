# probabilistic_robotics
確率ロボティクス課題用リポジトリ
# 実行環境
* CPU : Intel Core i5-8265U 1.6[GHz]
* OS : Ubuntu 20.04.5 LTS  
* メモリ : 8 [GB]
* Python : 3.8.10
# 作成したプログラム
試行結果から事後分布を計算し, グラフにプロットするプログラムを作成した. 試行結果は以下に示す通りである.  

* 改良前 : [完走, 失敗, 失敗, 完走, 完走]  
* 改良後 : [完走, 完走, 完走, 完走, 完走]  

作成したプログラムは以下に記載する.  
[calc_distribution.py](https://github.com/kazukishirasu/probrobotics_task/blob/master/calc_distribution.py)  
はじめに必要なライブラリのインポートや変数などを定義した. グラフの表示にはmatplotlibを用いた.
```
#!/usr/bin/python3
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
```
```all()```は試行一回ずつの結果を表示するための関数である.  
```last()```は最後の結果のみを表示するための関数である.  
```
def all():
    fig, ax = plt.subplots(2, ncols=int((len(score1[0]) / 2) + 1), tight_layout=True)
    ax = ax.ravel()
    for num in range(int(len(y) / 2)):
        ax[num].plot(x, y[num], color="blue")
        ax[num].plot(x, y[num + len((score1)[0]) + 1], color="red")
        ax[num].set_xlabel("t")
        ax[num].set_ylabel("prob")
        ax[num].set_xlim(0, 1)
        ax[num].set_ylim(0, 0.1)
        ax[num].set_xticks(np.arange(0.0, 1.1, 0.5))
        ax[num].set_yticks(np.arange(0.0, 0.11, 0.02))
        ax[num].grid(axis="x")
        ax[num].minorticks_on()
        ax[num].grid(which="both", axis="y")
        
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
```
以下のコードで試行結果に応じて事後分布を計算し, グラフを表示する.  
```
for i in range(len(score1)):
    y.append(np.full_like(x, 1/101))
    if score1[i][0] == "完走":
        const = 1 / (sum(np.arange(0, 1.01, step=0.01) * 1/101))
        t_y = const * np.arange(0, 1.01, step=0.01) * 1/101
        flag = True
        y.append(t_y)
    elif score1[i][0] == "失敗":
        const = 1 / (sum((1 - np.arange(0, 1.01, step=0.01)) * 1/101))
        f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * 1/101
        flag = False
        y.append(f_y)
    for j in score1[i][1:]:
        if j == "完走":
            if flag:
                const = 1/(sum(np.arange(0, 1.01, step=0.01) * t_y))
                t_y = const * np.arange(0, 1.01, step=0.01) * t_y
            else:
                const = 1/(sum(np.arange(0, 1.01, step=0.01) * f_y))
                t_y = const * np.arange(0, 1.01, step=0.01) * f_y
            flag = True
            y.append(t_y)
        elif j == "失敗":
            if flag:
                const = 1/(sum((1 - np.arange(0, 1.01, step=0.01)) * t_y))
                f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * t_y
            else:
                const = 1/(sum((1 - np.arange(0, 1.01, step=0.01)) * f_y))
                f_y = const * (1 - np.arange(0, 1.01, step=0.01)) * f_y
            flag = False
            y.append(f_y)
all()
# last()
plt.show()
```
これらのプログラムを用いて, 試行結果から事後分布を計算すると以下に示すグラフが得られた. 青線が改良前, 赤線が改良後である.  

<p align="center">
  <img src="https://user-images.githubusercontent.com/72000550/211546123-21dae3fc-5c4e-4e03-baed-4ff426ba4075.png">
</p>

すべての試行が終了した5つ目のグラフに注目すると改良後の方が完走率は高いと考えられる. しかし, 改良前と改良後の分布では重なりがあり, 今後試行回数を増やしていくと改良前は｢完走｣が増え, 改良後は｢失敗｣が増え分布が大きく変わる可能性がある. そこで, 次に分布の重なりがほぼなくなる程度まで試行回数を増やす実験を行った.  試行回数は以下に示すように, 単純にもとの試行結果を2倍(10回), 4倍(20回), 6倍(30回)したものを用いた.  

* 改良前 : [完走, 失敗, 失敗, 完走, 完走, 完走, 失敗, 失敗, 完走, 完走, ･･･]  
* 改良後 : [完走, 完走, 完走, 完走, 完走, 完走, 完走, 完走, 完走, 完走, ･･･]  

結果を以下に示す. 左から順に試行回数が10回, 20回, 30回のときのグラフである. 10回, 20回のときは分布が重なっているが, 30回のときでは重なりはほぼなく今後試行回数を増やし場合でも完走率が逆転することは低いと考えられる. よって, 試行回数は最低でも30回は必要であると考える.

<img src="https://user-images.githubusercontent.com/72000550/211583540-2418539c-069d-4527-aae4-2226da517b08.png" width=33%><img src="https://user-images.githubusercontent.com/72000550/211583553-fb3bf8d3-1b79-4ec9-9116-2505c2f22176.png" width=33%><img src="https://user-images.githubusercontent.com/72000550/211583560-af555547-e5b1-48ca-b081-76ab5a54856d.png" width=33%>

# LICENSE
The source code is licensed MIT, see [LICENSE](https://github.com/kazukishirasu/probrobotics_task/blob/master/LICENSE).
