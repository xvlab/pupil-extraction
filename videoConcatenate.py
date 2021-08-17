import cv2

# 获得视频的格式
path = "Thy1-GCaMP6s-M4-K-airpuff-0706"
videoCapture1 = cv2.VideoCapture(
    "\\\\192.168.3.146\\public\\临时文件\\xpy\\" + path + '\\Thy1-GCaMP6s-M4-K-airpuff-0706.avi')
videoCapture2 = cv2.VideoCapture(
    "\\\\192.168.3.146\\public\\临时文件\\xpy\\" + path + '\\Thy1-GCaMP6s-M4-K-airpuff-0706-3.mp4')

# 获得码率及尺寸
fps = videoCapture1.get(cv2.CAP_PROP_FPS)
width = int(videoCapture1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCapture1.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
print(fps, size)

# 编码格式
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
f = cv2.VideoWriter_fourcc('M', 'P', '4', '2')  # ？？

# 指定写视频的格式, I420-avi, MJPG-mp4
videoWriter = cv2.VideoWriter("\\\\192.168.3.146\\public\\临时文件\\xpy\\" + path + '\\' + path + '_all.avi', f, fps, size)

# 读帧
success, frame = videoCapture1.read()
while success:
    videoWriter.write(frame)  # 写视频帧
    success, frame = videoCapture1.read()  # 获取下一帧
# 资源释放
videoCapture1.release()

success2, frame2 = videoCapture2.read()
while success2:
    videoWriter.write(frame2)  # 写视频帧
    success2, frame2 = videoCapture2.read()  # 获取下一帧
# 资源释放
videoCapture2.release()
videoWriter.release()
