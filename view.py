import numpy as np
import cv2
import sys
import os

# You should replace these 3 lines with the output in calibration step
DIM=(640, 480)
K=np.array([[262.5425790986778, 0.0, 330.0315995955107], [0.0, 262.58969757778124, 232.9388107102391], [0.0, 0.0, 1.0]])
D=np.array([[-0.031585563437385326], [0.022896931000373787], [-0.0287622290552157], [0.012026614170409339]])

def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    # cv2.imshow("undistorted", undistorted_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite('out_' + os.path.basename(img_path), undistorted_img)

if __name__ == '__main__':
    # for p in sys.argv[1:]:
    #     undistort(p)

    cap = cv2.VideoCapture(8)

    #繰り返しのためのwhile文
    while True:
        #カメラからの画像取得
        ret, frame = cap.read()

        h,w = 480, 640
        map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
        undistorted_img = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
        


        #カメラの画像の出力
        cv2.imshow('union' , undistorted_img)
        cv2.imshow('camera' , frame)


        #繰り返し分から抜けるためのif文
        key =cv2.waitKey(10)
        if key == 27:
            break

    #メモリを解放して終了するためのコマンド
    cap.release()
    cv2.destroyAllWindows()