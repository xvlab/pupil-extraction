import cv2

# 获得视频的格式
videoCapture = cv2.VideoCapture(
    '\\\\192.168.3.146\\public\\临时文件\\xpy\\thy1-gcamp6s-m2-0114-2(airpuff)\\thy1-gcamp6s-m2-0114-2-2.mp4')

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
print(fps, size)

# 编码格式
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
f = cv2.VideoWriter_fourcc('M', 'P', '4', '2')  # ？？

# 指定写视频的格式, I420-avi, MJPG-mp4
videoWriter = cv2.VideoWriter('oto_other.avi', f, fps, size)

# 读帧
success, frame = videoCapture.read()

while success:
    videoWriter.write(frame)  # 写视频帧
    cv2.imshow("video", frame)  # 显示

    cv2.waitKey(int(1000 / int(fps)))  # 延迟

    # if ord("q") == cv2.waitKey(41):
    #     break
    success, frame = videoCapture.read()  # 获取下一帧
# 资源释放
cv2.destroyAllWindows()
videoCapture.release()
videoWriter.release()
