import cv2
import numpy as np
import math
import glob


def cd(visible, fused):
    h, w = visible.shape[0:2]
    s = 0
    for i in range(h):
        for j in range(w):
            n1 = np.linalg.norm(visible[i, j])
            n2 = np.linalg.norm(fused[i, j])
            if not (n1 == 0 or n2 == 0):
                cos = visible[i, j].dot(fused[i, j]) / n1 / n2
                if cos > 1:
                    cos = 1
                if cos < -1:
                    cos = -1
                s += math.acos(cos)
    return s / (h * w)


if __name__ == '__main__':
    f = open('output/color_deviation_values.txt', 'w')
    visible_images = glob.glob("./input/visible/*.jpg")
    for method in ['RGB', 'YIQ', 'HSV', 'CNN', 'MST-SR', 'PIAFusion', 'SeAFusion', 'FCDFusion']:
        print(f'Computing color deviation of method {method}...')
        f.write(f'Computing color deviation of method {method}...\n')
        s = 0
        for visible_path in visible_images:
            visible = cv2.imread(visible_path).astype(np.float32)
            fused_path = visible_path.replace('/input/visible', '/output/' + method)
            fused = cv2.imread(fused_path).astype(np.float32)
            cd_value = cd(visible, fused)
            print(f'{fused_path} : {cd_value}')
            f.write(f'{fused_path} : {cd_value}\n')
            s += cd_value
        print(f'Average: {s / len(visible_images)}\n')
        f.write(f'Average: {s / len(visible_images)}\n\n')
