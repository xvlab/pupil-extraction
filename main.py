import cv2
import json
import matplotlib.pyplot as plt
import scipy.io
import numpy as np

path = "thy1-gcamp6s-m2-0112-1(sleep)"
name = "thy1-gcamp6s-m2-0112-1-1"

data = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\info.mat')  # 读取mat文件
video = cv2.VideoCapture('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\' + name + '.mp4')
fps = video.get(cv2.CAP_PROP_FPS)
time_offset = float(data['sync1'][0][0]) - 682 / fps
pupilSeries = []
areaSeries = []
xSeries = []
ySeries = []
timeSeries = []
wakeSeries_start = []
wakeSeries_end = []
NREMSeries_start = []
NREMSeries_end = []
REMSeries_start = []
REMSeries_end = []
success, frame = video.read()
r = cv2.selectROI('input', frame, False)
roi_center_y = int(r[3] / 2)
roi_center_x = int(r[2] / 2)
counter = 0
lastState = state = 100
while success:
    roi = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 28, 255, cv2.THRESH_BINARY)
    # print(binary)

    # cv2.imshow('mouse', roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if 0.4 < area / 1000 < 2.5:
            # areaSeries[counter] = area
            M = cv2.moments(contour)  # 计算各阶矩,字典形式
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            x = center_x - roi_center_x
            y = center_y - roi_center_y
            time = counter / fps + time_offset
            lastState = state
            state = int(data['brainState_01'][int(time / 5)][0])
            pupilDict = {'frame': counter, 'time': float(time), 'area': area, 'x': center_x - roi_center_x,
                         'y': center_y - roi_center_y, 'state': state}
            xSeries.append(x)
            ySeries.append(y)
            areaSeries.append(area)
            pupilSeries.append(pupilDict)
            timeSeries.append(time)
            if state != lastState:
                if state == 0:
                    NREMSeries_start.append(time)
                elif state == -1:
                    REMSeries_start.append(time)
                elif state == 1:
                    wakeSeries_start.append(time)
                if lastState == 0:
                    NREMSeries_end.append(time)
                elif lastState == -1:
                    REMSeries_end.append(time)
                elif lastState == 1:
                    wakeSeries_end.append(time)
                break

    counter = counter + 1
    # print(sortedContourAreaKeySet)
    # cv2.drawContours(roi, contourAreaKeySet[sortedContourAreaKeySet[1]], -1, (0, 0, 255), 3)
    # cv2.imshow("img", roi)
    # cv2.waitKey(0)
    success, frame = video.read()

if len(NREMSeries_start) != len(NREMSeries_end):
    NREMSeries_end.append(time)
if len(REMSeries_start) != len(REMSeries_end):
    REMSeries_end.append(time)
if len(wakeSeries_start) != len(wakeSeries_end):
    wakeSeries_end.append(time)

NREM = []
REM = []
wake = []
for i in range(len(NREMSeries_start)):
    NREM.append([NREMSeries_start[i], NREMSeries_end[i]])
for i in range(len(REMSeries_start)):
    REM.append([REMSeries_start[i], REMSeries_end[i]])
for i in range(len(NREMSeries_start)):
    wake.append([wakeSeries_start[i], wakeSeries_end[i]])

print('NREM: ', NREM)
print('REM: ', REM)
print('wake: ', wake)
# timespan
figure, (ax1, ax2, ax3) = plt.subplots(3, 1,
                                       figsize=(6, 6),
                                       dpi=300, sharex=True)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
minxSeries = min(xSeries)
maxxSeries = max(xSeries)
minySeries = min(ySeries)
maxySeries = max(ySeries)
minareaSeries = min(areaSeries)
maxareaSeries = max(areaSeries)
ax1.plot(timeSeries, xSeries, c='blue')
for i in range(len(NREM)):
    if i == 0:
        ax1.fill_between(timeSeries[timeSeries.index(NREM[i][0]):timeSeries.index(NREM[i][1])], minxSeries, maxxSeries,
                         facecolor='#fb5ffc', alpha=0.3, label='NREM')
    else:
        ax1.fill_between(timeSeries[timeSeries.index(NREM[i][0]):timeSeries.index(NREM[i][1])], minxSeries, maxxSeries,
                         facecolor='#fb5ffc', alpha=0.3)
for i in range(len(REM)):
    if i == 0:
        ax1.fill_between(timeSeries[timeSeries.index(REM[i][0]):timeSeries.index(REM[i][1])], minxSeries, maxxSeries,
                         facecolor='green', alpha=0.3, label='REM')
    else:
        ax1.fill_between(timeSeries[timeSeries.index(REM[i][0]):timeSeries.index(REM[i][1])], minxSeries, maxxSeries,
                         facecolor='green', alpha=0.3)
for i in range(len(wake)):
    if i == 0:
        ax1.fill_between(timeSeries[timeSeries.index(wake[i][0]):timeSeries.index(wake[i][1])], minxSeries, maxxSeries,
                         facecolor='#0165fc', alpha=0.3, label='wake')
    else:
        ax1.fill_between(timeSeries[timeSeries.index(wake[i][0]):timeSeries.index(wake[i][1])], minxSeries, maxxSeries,
                         facecolor='#0165fc', alpha=0.3)
ax1.set_title("小鼠瞳孔水平方向的偏移")
ax2.plot(timeSeries, ySeries, c='orange', linestyle=':')
for i in range(len(NREM)):
    ax2.fill_between(timeSeries[timeSeries.index(NREM[i][0]):timeSeries.index(NREM[i][1])], minySeries, maxySeries,
                     facecolor='#fb5ffc', alpha=0.3)
for i in range(len(REM)):
    ax2.fill_between(timeSeries[timeSeries.index(REM[i][0]):timeSeries.index(REM[i][1])], minySeries, maxySeries,
                     facecolor='green', alpha=0.3)
for i in range(len(wake)):
    ax2.fill_between(timeSeries[timeSeries.index(wake[i][0]):timeSeries.index(wake[i][1])], minySeries, maxySeries,
                     facecolor='#0165fc', alpha=0.3)
ax2.set_title("小鼠瞳孔竖直方向的偏移")
ax3.plot(timeSeries, areaSeries, c='r', linestyle=':')
for i in range(len(NREM)):
    ax3.fill_between(timeSeries[timeSeries.index(NREM[i][0]):timeSeries.index(NREM[i][1])], minareaSeries,
                     maxareaSeries, facecolor='#fb5ffc', alpha=0.3)
for i in range(len(REM)):
    ax3.fill_between(timeSeries[timeSeries.index(REM[i][0]):timeSeries.index(REM[i][1])], minareaSeries, maxareaSeries,
                     facecolor='green', alpha=0.3)
for i in range(len(wake)):
    ax3.fill_between(timeSeries[timeSeries.index(wake[i][0]):timeSeries.index(wake[i][1])], minareaSeries,
                     maxareaSeries, facecolor='#0165fc', alpha=0.3)
ax3.set_title("小鼠瞳孔面积的变化")

figure.subplots_adjust(hspace=0.2)
figure.legend(loc='upper left', frameon='True')
plt.show()

with open(name + ".json", "w") as f:
    f.write(json.dumps(pupilSeries, ensure_ascii=False, indent=4, separators=(',', ':')))