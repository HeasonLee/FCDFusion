import cv2
import numpy as np
import glob


def RGB(visible, infrared):
    return visible // 2 + infrared // 2


def YIQ(visible, infrared):
    fused = np.ndarray((h, w, 3), dtype=np.float16)
    m_YIQ = np.mat("0.11, 0.59, 0.30; -0.32, -0.28, 0.60; 0.31, -0.52, 0.21")
    m_BGR = np.mat("1.00, -1.11, 1.73; 1.00, -0.28, -0.64; 1.00, 0.95, 0.62")
    for i in range(h):
        for j in range(w):
            fused[i, j] = np.matmul(m_YIQ, visible[i, j])
            fused[i, j, 0] = (fused[i, j, 0] + infrared[i, j, 0]) / 2
            fused[i, j] = np.matmul(m_BGR, fused[i, j])
            for c in range(3):
                if fused[i, j, c] < 0:
                    fused[i, j, c] = 0
                if fused[i, j, c] > 255:
                    fused[i, j, c] = 255
    return fused.astype(np.uint8)


def HSV(visible, infrared):
    visible_hsv = cv2.cvtColor(visible, cv2.COLOR_BGR2HSV)
    infrared_hsv = cv2.cvtColor(infrared, cv2.COLOR_BGR2HSV)
    for i in range(h):
        for j in range(w):
            visible_hsv[i, j, 2] = visible_hsv[i, j, 2] / 2 + infrared_hsv[i, j, 2] / 2
    return cv2.cvtColor(visible_hsv, cv2.COLOR_HSV2BGR)


def FCDFusion(visible, infrared):
    fused = np.ndarray((h, w, 3), dtype=np.uint16)
    for i in range(h):
        for j in range(w):
            b = visible[i, j, 0]
            g = visible[i, j, 1]
            r = visible[i, j, 2]
            vmax = 1
            if b > vmax:
                vmax = b
            if g > vmax:
                vmax = g
            if r > vmax:
                vmax = r
            a = infrared[i, j, 0] / 255.
            a *= a
            k = (vmax + 255) >> 1
            k = a * k / vmax + 0.5
            fused[i, j, 0] = b * k
            if fused[i, j, 0] > 255:
                fused[i, j, 0] = 255
            fused[i, j, 1] = g * k
            if fused[i, j, 1] > 255:
                fused[i, j, 1] = 255
            fused[i, j, 2] = r * k
            if fused[i, j, 2] > 255:
                fused[i, j, 2] = 255
    return fused.astype(np.uint8)


if __name__ == '__main__':
    visible_images = glob.glob("./input/visible/*.jpg")

    for visible_path in visible_images:
        infrared_path = visible_path.replace("visible", "infrared")
        fused_path = visible_path.replace("input/visible", "output/method")

        visible = cv2.imread(visible_path)
        h, w = visible.shape[0:2]
        infrared = cv2.imread(infrared_path)
        print('Fusing', visible_path, f'({w}×{h}) with corresponding infrared image...')

        cv2.imwrite(fused_path.replace("method", "RGB"), RGB(visible, infrared))
        cv2.imwrite(fused_path.replace("method", "YIQ"), YIQ(visible, infrared))
        cv2.imwrite(fused_path.replace("method", "HSV"), HSV(visible, infrared))
        cv2.imwrite(fused_path.replace("method", "FCDFusion"), FCDFusion(visible, infrared))
    print('Done.')

