import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import seaborn as sns

import h5py

path = "Thy1-GCaMP6s-M5-K-airpuff-0707"
data = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\info.mat')
#  h5py.File('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\info.mat',
#                  'r')  # 读取mat文件
strengthData = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\strength.mat')
fps = 25
time_offset = float(data['sync1'][0][0]) - 261 / fps  # 4266 261 4178 / fps
proc = np.load('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\Thy1-GCaMP6s-M5-K-airpuff-0707_proc.npy',
               allow_pickle=True).item()
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
airpuffSeries = np.squeeze(data['sync2'])[4:]
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
separateNum = np.zeros((4,))
for strength in strengthSeries:
    if strength == 70:
        separateNum[0] = separateNum[0] + 1
    elif strength == 75:
        separateNum[1] = separateNum[1] + 1
    elif strength == 80:
        separateNum[2] = separateNum[2] + 1
    elif strength == 85:
        separateNum[3] = separateNum[3] + 1
pupilX85Accumulate = np.zeros((750, int(separateNum[3])))
pupilX80Accumulate = np.zeros((750, int(separateNum[2])))
pupilX75Accumulate = np.zeros((750, int(separateNum[1])))
pupilX70Accumulate = np.zeros((750, int(separateNum[0])))
pupilY85Accumulate = np.zeros((750, int(separateNum[3])))
pupilY80Accumulate = np.zeros((750, int(separateNum[2])))
pupilY75Accumulate = np.zeros((750, int(separateNum[1])))
pupilY70Accumulate = np.zeros((750, int(separateNum[0])))
pupilArea85Accumulate = np.zeros((750, int(separateNum[3])))
pupilArea80Accumulate = np.zeros((750, int(separateNum[2])))
pupilArea75Accumulate = np.zeros((750, int(separateNum[1])))
pupilArea70Accumulate = np.zeros((750, int(separateNum[0])))
motSVDAccumulate = np.zeros((750, motSVD.shape[1], 4))
counterS = np.zeros((4,)).astype(int)
k = 0
for index in indexSeries:
    if strengthSeries[k] == 70:
        for num in range(-375, 375):
            pupilX70Accumulate[num + 375, counterS[0]] = pupilX70Accumulate[num + 375, counterS[0]] + \
                                                         pupilXSeries[index + num]
            pupilY70Accumulate[num + 375, counterS[0]] = pupilY70Accumulate[num + 375, counterS[0]] + \
                                                         pupilYSeries[index + num]
            pupilArea70Accumulate[num + 375, counterS[0]] = pupilArea70Accumulate[num + 375, counterS[0]] + \
                                                            pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 0] = motSVDAccumulate[num, :, 0] + motSVD[index + num, :]
        counterS[0] = counterS[0] + 1
    elif strengthSeries[k] == 75:
        for num in range(-375, 375):
            pupilX75Accumulate[num + 375, counterS[1]] = pupilX75Accumulate[num + 375, counterS[1]] + \
                                                         pupilXSeries[index + num]
            pupilY75Accumulate[num + 375, counterS[1]] = pupilY75Accumulate[num + 375, counterS[1]] + \
                                                         pupilYSeries[index + num]
            pupilArea75Accumulate[num + 375, counterS[1]] = pupilArea75Accumulate[num + 375, counterS[1]] + \
                                                            pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 1] = motSVDAccumulate[num, :, 1] + motSVD[index + num, :]
        counterS[1] = counterS[1] + 1
    elif strengthSeries[k] == 80:
        for num in range(-375, 375):
            pupilX80Accumulate[num + 375, counterS[2]] = pupilX80Accumulate[num + 375, counterS[2]] + \
                                                         pupilXSeries[index + num]
            pupilY80Accumulate[num + 375, counterS[2]] = pupilY80Accumulate[num + 375, counterS[2]] + \
                                                         pupilYSeries[index + num]
            pupilArea80Accumulate[num + 375, counterS[2]] = pupilArea80Accumulate[num + 375, counterS[2]] + \
                                                            pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 2] = motSVDAccumulate[num, :, 2] + motSVD[index + num, :]
        counterS[2] = counterS[2] + 1
    elif strengthSeries[k] == 85:
        for num in range(-375, 375):
            pupilX85Accumulate[num + 375, counterS[3]] = pupilX85Accumulate[num + 375, counterS[3]] + \
                                                         pupilXSeries[index + num]
            pupilY85Accumulate[num + 375, counterS[3]] = pupilY85Accumulate[num + 375, counterS[3]] + \
                                                         pupilYSeries[index + num]
            pupilArea85Accumulate[num + 375, counterS[3]] = pupilArea85Accumulate[num + 375, counterS[3]] + \
                                                            pupilAreaSeries[index + num]
            motSVDAccumulate[num, :, 3] = motSVDAccumulate[num, :, 3] + motSVD[index + num, :]
        counterS[3] = counterS[3] + 1
    k = k + 1

timespan = np.linspace(1, 30, 750)
# timespan
cmap = sns.cubehelix_palette(start=1.5, rot=3, gamma=0.8, as_cmap=True)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
figX70, axX70 = plt.subplots(1, 1, figsize=(8, 8), dpi=300)
im = axX70.imshow(pupilX70Accumulate.reshape(pupilY70Accumulate.shape[1], pupilY70Accumulate.shape[0]))
# plt.savefig('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\' + path + '.jpg', dpi=600)
plt.show()
