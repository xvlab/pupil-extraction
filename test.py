# import cv2
# import json
#
# path = "Thy1-GCaMP6s-M5-k-0624"
# name = "Thy1-GCaMP6s-M5-k-0624-2"
# video = cv2.VideoCapture('D:\\mokoghost\\video\\' + path + '\\' + name + '.mp4')
# areaSeries = {}
# success, frame = video.read()
# r = cv2.selectROI('input', frame, False)
# counter = 0
#
# while success and counter < 100:
#     success, frame = video.read()
#     counter = counter + 1
#
# cv2.imshow("img", frame)
# cv2.waitKey(0)
# roi = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
# roi_center_y = int(r[3] / 2)
# roi_center_x = int(r[2] / 2)
# # print(int(r[1]), " ", int(r[1] + r[3]), " ", int(r[0]), " ", int(r[0] + r[2]))
# gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
# # binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 27, 2)
# ret, binary = cv2.threshold(gray, 28, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# # cv2.drawContours(roi, contours, -1, (0, 0, 255), 3)
# # cv2.imshow("img", roi)
# # cv2.waitKey(0)
# # cv2.drawContours(roi, contours, -1, (0, 0, 255), 3)
# # cv2.imshow("img", roi)
# # cv2.waitKey(0)
#
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if 0.4 < area / 1000 < 2.5:
#         print("size: ", area)
#         cv2.drawContours(roi, contour, -1, (0, 0, 255), 3)
#         M = cv2.moments(contour)  # 计算各阶矩,字典形式
#         center_x = int(M["m10"] / M["m00"])
#         center_y = int(M["m01"] / M["m00"])
#         print("x: ", center_x - roi_center_x)
#         print("y: ", center_y - roi_center_y)
#         cv2.circle(roi, (center_x, center_y), 3, 255, -1)
#         cv2.imshow("img", roi)
#         cv2.waitKey(0)
######################################################################################
# import cv2
#
# video = cv2.VideoCapture('D:\\mokoghost\\video\\Thy1-GCaMP6s-M5-k-0624\\Thy1-GCaMP6s-M5-k-0624-2.mp4')
# areaSeries = {}
# success, frame = video.read()
# r = cv2.selectROI('input', frame, False)
# counter = 0
# while success:
#     roi = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
#
#     gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     # binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 27, 2)
#     ret, binary = cv2.threshold(gray, 28, 255, cv2.THRESH_BINARY)
#     contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     number = 0
#     areas = []
#     for contour in contours:
#         area = cv2.contourArea(contour)
#         if 0.4 < area / 1000 < 2.5:
#             number = number + 1
#             areas.append(area)
#     if number > 1:
#         print(counter, " ", number, " ", areas)
#     if number == 0:
#         print(counter, " is 0")
#     counter = counter + 1
#     success, frame = video.read()
######################################################################################
# import cv2
# import matplotlib.pyplot as plt
# import json
#
# path = "Thy1-GCaMP6s-M4-K-airpuff-0706"
# name = "Thy1-GCaMP6s-M4-K-airpuff-0706_all"
# #  cv2.VideoCapture(r'D:\mokoghost\pupil extraction\test.avi')
# video = cv2.VideoCapture('\\\\192.168.3.146\\public\\临时文件\\xpy\\' + path + '\\' + name + '.avi')
# areaSeries = {}
# success, frame = video.read()
# counter = 0
# imglist = []
# show = 0
# while success and counter < 4280:
#     success, frame = video.read()
#     counter = counter + 1
#     if counter > 4255:
#         show = show + 1
#         plt.subplot(5, 5, show)
#         plt.imshow(frame)
#         plt.title("frame " + str(counter))
#         plt.xticks([])
#         plt.yticks([])
#
# plt.savefig('picture.jpg', dpi=600)
#
# plt.show()
######################################################################################
# import numpy as np
# # import matplotlib.pyplot as plt
# #
# # x = np.linspace(0, 2 * np.pi, 100)
# # y1 = np.sin(x)
# # y2 = np.cos(x) + 2
# #
# # plt.figure()
# # plt.plot(x, y1)
# # plt.plot(x, y2)
# # plt.fill_between(x, y1, y2, color='blue', alpha=0.5, label='y2-y1')
# # plt.legend(loc='upper left', frameon='True')
# #
# # plt.show()
# x=np.linspace([500,100])
######################################################################################
# import numpy as np
#
# a = np.random.random((123,))
# print(a.shape)
# counter = 119
# b = a[3:]
# print(b.shape)
######################################################################################
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# # We want to show all ticks...
# ax.set_xticks(np.arange(len(farmers)))
# ax.set_yticks(np.arange(len(vegetables)))
# # ... and label them with the respective list entries
# ax.set_xticklabels(farmers)
# ax.set_yticklabels(vegetables)
#
# # Rotate the tick labels and set their alignment.
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#          rotation_mode="anchor")
#
# # Loop over data dimensions and create text annotations.
# for i in range(len(vegetables)):
#     for j in range(len(farmers)):
#         text = ax.text(j, i, harvest[i, j],
#                        ha="center", va="center", color="w")
#
# ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()
