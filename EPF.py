# 导入cv模块
import cv2 as cv
import numpy as np


# 高斯双边模糊EPF
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("di_demo", dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 0, 10, 50)
    cv.imshow("shift_demo", dst)
    cv.imwrite("111.jpg",dst)



print("------------Hi,Python!-------------")
# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
src = cv.imread("./kl.jpg")
# 创建窗口并显示图像
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)  # 显示原图
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
# 释放窗口
cv.destroyAllWindows()