import numpy as np
import matplotlib.pyplot as plt
import scipy.io

path = "Thy1-GCaMP6s-M5-K-airpuff-0707"  # "thy1-gcamp6s-m2-0114-2(airpuff)"  #

data = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\info.mat')  # 读取mat文件
fps = 25
time_offset = float(data['sync1'][0][0]) - 261 / fps  # 4178 / fps  #
proc = np.load(r'D:\mokoghost\video\test\Thy1-GCaMP6s-M5-K-airpuff-0707_proc.npy', allow_pickle=True).item()
pupilAreaSeries = proc['pupil'][0]['area_smooth']
pupilComSeries = proc['pupil'][0]['com_smooth']
blinkSeries = proc['blink'][0]
pupilXSeries, pupilYSeries = np.squeeze(np.split(pupilComSeries, [1], axis=1))
motSVD = proc['motSVD'][1][1:-2, :]
pupilXSeries = pupilXSeries[1:-2]
pupilYSeries = pupilYSeries[1:-2]
pupilAreaSeries = pupilAreaSeries[1:-2]
timeSeries = np.linspace(1, len(pupilXSeries), len(pupilXSeries)) / fps + time_offset
airpuffSeries = np.squeeze(data['sync2'])[3:]
counter = 0
for x in airpuffSeries:
    if x > max(timeSeries):
        airpuffSeries = airpuffSeries[0:counter]
        break
    counter = counter + 1
indexSeries = []
for x in airpuffSeries:
    indexSeries.append(round((x - time_offset) * fps))
pupilXAccumulate = np.zeros((750,))
pupilYAccumulate = np.zeros((750,))
pupilAreaAccumulate = np.zeros((750,))
motSVDAccumulate = np.zeros((750, motSVD.shape[1]))
for index in indexSeries:
    for num in range(750):
        pupilXAccumulate[num] = pupilXAccumulate[num] + pupilXSeries[index + num]
        pupilYAccumulate[num] = pupilYAccumulate[num] + pupilYSeries[index + num]
        pupilAreaAccumulate[num] = pupilAreaAccumulate[num] + pupilAreaSeries[index + num]
        motSVDAccumulate[num, :] = motSVDAccumulate[num, :] + motSVD[index + num, :]

pupilAreaAccumulate = pupilAreaAccumulate / len(indexSeries)
pupilXAccumulate = pupilXAccumulate / len(indexSeries)
pupilYAccumulate = pupilYAccumulate / len(indexSeries)
timespan = np.linspace(1, 30, 750)
# timespan
figure, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1,
                                            figsize=(8, 12),
                                            dpi=300, sharex=True)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
ax1.plot(timespan, pupilXAccumulate, c='darkred', linestyle=':')
ax1.set_title("小鼠瞳孔水平方向的偏移")
ax2.plot(timespan, pupilYAccumulate, c='#7f5e00', linestyle=':')
ax2.set_title("小鼠瞳孔竖直方向的偏移")
ax3.plot(timespan, pupilAreaAccumulate, c='#4b6113', linestyle=':')
ax3.set_title("小鼠瞳孔面积的变化")
ax4.plot(timespan, motSVDAccumulate[:, :], c='#01386a', linestyle=':')
ax4.set_title("小鼠面部动作SVD的变化")
# ax1.plot(timeSeries, pupilXSeries, c='blue')
# for x in airpuffSeries:
#     ax1.vlines(x, min(pupilXSeries), max(pupilXSeries), colors="c", linestyles="dashed")
# ax2.plot(timeSeries, pupilYSeries, c='orange', linestyle=':')
# for x in airpuffSeries:
#     ax2.vlines(x, min(pupilYSeries), max(pupilYSeries), colors="c", linestyles="dashed")
# ax3.plot(timeSeries, pupilAreaSeries, c='r', linestyle=':')
# for x in airpuffSeries:
#     ax3.vlines(x, min(pupilAreaSeries), max(pupilAreaSeries), colors="c", linestyles="dashed")

figure.subplots_adjust(hspace=0.3)
plt.show()
