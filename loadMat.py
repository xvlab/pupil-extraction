import scipy.io
import numpy as np

path = "Thy1-GCaMP6s-M5-K-airpuff-0707"

data = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\info.mat')  # 读取mat文件
strengthData = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\strength.mat')
print(strengthData.keys())  # 查看mat文件中的所有变量
print(data.keys())  # 查看mat文件中的所有变量
# print(float(data['sync1'][0][0]))
# print(data['brainState_01'][int(682 / 5)][0])
print(strengthData['puff_list'][0])
# offset = 682  # 在该帧之后开始记录FOV，也即sync1的第一个数据对应682帧

strengthSeries=np.array(strengthData['puff_list'][0])