import scipy.io
import matplotlib.pyplot as plt
import cv2
import numpy as np

data = scipy.io.loadmat('\\\\192.168.3.146\\public\\临时文件\\xpy\\matlab.mat')

masks = np.uint8(data['mask'])

for index in range(np.size(masks, 2)):
    mask = masks[:, :, index]
    # plt.imshow(mask)
    # plt.waitforbuttonpress(1)
    binary = np.uint8(mask != 0)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    binary = (binary * 255).astype(np.uint8)
    binary = binary.copy()
    cv2.drawContours(binary, contours, -1, (0, 255, 255), 2)
    cv2.imshow("img", binary)
    cv2.waitKey(0)
    print("------------------------------------------")
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        # cv2.drawContours(mask,contours)
