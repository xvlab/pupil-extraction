import numpy as np
import matplotlib.pyplot as plt
import scipy.io

path = "Thy1-GCaMP6s-M5-K-airpuff-0707"

data = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\info.mat')  # 读取mat文件
strengthData = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\strength.mat')
fps = 25
time_offset = float(data['sync1'][0][0]) - 261 / fps  # 4178 / fps
proc = np.load(r'D:\mokoghost\video\test\Thy1-GCaMP6s-M5-K-airpuff-0707_proc.npy', allow_pickle=True).item()
pupilAreaSeries = proc['pupil'][0]['area_smooth']
pupilComSeries = proc['pupil'][0]['com_smooth']
blinkSeries = proc['blink'][0]
pupilXSeries, pupilYSeries = np.squeeze(np.split(pupilComSeries, [1], axis=1))
motSVD = proc['motSVD'][1][1:-1, :]
pupilXSeries = pupilXSeries[1:-1]
pupilYSeries = pupilYSeries[1:-1]
pupilAreaSeries = pupilAreaSeries[1:-1]
timeSeries = np.linspace(1, len(pupilXSeries), len(pupilXSeries)) / fps + time_offset
strengthSeries = np.array(strengthData['puff_list'][0])
airpuffSeries = np.squeeze(data['sync2'])[3:]
counter = 0
for x in airpuffSeries:
    if x > max(timeSeries):
        airpuffSeries = airpuffSeries[0:counter]
        break
    counter = counter + 1
indexSeries = []
strengthSeries = strengthSeries[0:counter]
for x in airpuffSeries:
    indexSeries.append(round((x - time_offset) * fps))
pupilXAccumulate = np.zeros((750, 4))
pupilYAccumulate = np.zeros((750, 4))
pupilAreaAccumulate = np.zeros((750, 4))
motSVDAccumulate = np.zeros((750, motSVD.shape[1], 4))
k = 0
for index in indexSeries:
    for num in range(750):
        if strengthSeries[k] == 70:
            pupilXAccumulate[num, 0] = pupilXAccumulate[num, 0] + pupilXSeries[index + num]
            pupilYAccumulate[num, 0] = pupilYAccumulate[num, 0] + pupilYSeries[index + num]
            pupilAreaAccumulate[num, 0] = pupilAreaAccumulate[num, 0] + pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 0] = motSVDAccumulate[num, :, 0] + motSVD[index + num, :]
        elif strengthSeries[k] == 75:
            pupilXAccumulate[num, 1] = pupilXAccumulate[num, 1] + pupilXSeries[index + num]
            pupilYAccumulate[num, 1] = pupilYAccumulate[num, 1] + pupilYSeries[index + num]
            pupilAreaAccumulate[num, 1] = pupilAreaAccumulate[num, 1] + pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 1] = motSVDAccumulate[num, :, 1] + motSVD[index + num, :]
        elif strengthSeries[k] == 80:
            pupilXAccumulate[num, 2] = pupilXAccumulate[num, 2] + pupilXSeries[index + num]
            pupilYAccumulate[num, 2] = pupilYAccumulate[num, 2] + pupilYSeries[index + num]
            pupilAreaAccumulate[num, 2] = pupilAreaAccumulate[num, 2] + pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 2] = motSVDAccumulate[num, :, 2] + motSVD[index + num, :]
        elif strengthSeries[k] == 85:
            pupilXAccumulate[num, 3] = pupilXAccumulate[num, 3] + pupilXSeries[index + num]
            pupilYAccumulate[num, 3] = pupilYAccumulate[num, 3] + pupilYSeries[index + num]
            pupilAreaAccumulate[num, 3] = pupilAreaAccumulate[num, 3] + pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 3] = motSVDAccumulate[num, :, 3] + motSVD[index + num, :]
    k = k + 1

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
ax1.plot(timespan, pupilXAccumulate[:, 0], c='darkred', linestyle=':', label='强度70')
ax1.plot(timespan, pupilXAccumulate[:, 1], c='#7f5e00', linestyle=':', label='强度75')
ax1.plot(timespan, pupilXAccumulate[:, 2], c='#4b6113', linestyle=':', label='强度80')
ax1.plot(timespan, pupilXAccumulate[:, 3], c='#01386a', linestyle=':', label='强度85')
ax1.set_title("小鼠瞳孔水平方向的偏移")
ax2.plot(timespan, pupilYAccumulate[:, 0], c='r', linestyle=':')
ax2.plot(timespan, pupilYAccumulate[:, 1], c='#a87900', linestyle=':')
ax2.plot(timespan, pupilYAccumulate[:, 2], c='#728639', linestyle=':')
ax2.plot(timespan, pupilYAccumulate[:, 3], c='#014182', linestyle=':')
ax2.set_title("小鼠瞳孔竖直方向的偏移")
ax3.plot(timespan, pupilAreaAccumulate[:, 0], c='tomato', linestyle=':')
ax3.plot(timespan, pupilAreaAccumulate[:, 1], c='#ffc512', linestyle=':')
ax3.plot(timespan, pupilAreaAccumulate[:, 2], c='#90b134', linestyle=':')
ax3.plot(timespan, pupilAreaAccumulate[:, 3], c='#3b638c', linestyle=':')
ax3.set_title("小鼠瞳孔面积的变化")
ax4.plot(timespan, motSVDAccumulate[:, :, 0], c='salmon', linestyle=':')
ax4.plot(timespan, motSVDAccumulate[:, 1], c='#fbdd7e', linestyle=':')
ax4.plot(timespan, motSVDAccumulate[:, 2], c='#bbf90f', linestyle=':')
ax4.plot(timespan, motSVDAccumulate[:, 3], c='#a2cffe', linestyle=':')
ax4.set_title("小鼠面部动作SVD的变化")
figure.legend(loc='upper left', frameon='True')
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
