import dlib
import cv2
import numpy as np
from os import path
import os
import shutil

# ==========모델 추출======
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('./model/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('./model/dlib_face_recognition_resnet_model_v1.dat')


# ===============얼굴 찾기=======
def find_faces(img):
    dets = detector(img, 1)

    if len(dets) == 0:
        return np.empty(0), np.empty(0), np.empty(0)

    rects, shapes = [], []
    shapes_np = np.zeros((len(dets), 68, 2), dtype=np.int64)
    for k, d in enumerate(dets):
        rect = ((d.left(), d.top()), (d.right(), d.bottom()))
        rects.append(rect)

        shape = sp(img, d)

        # convert dlib shape to numpy array
        for i in range(0, 68):
            shapes_np[k][i] = (shape.part(i).x, shape.part(i).y)

        shapes.append(shape)

    return rects, shapes, shapes_np


# ==============랜드마크 추출==========
def encode_faces(img, shapes):
    face_descriptors = []
    for shape in shapes:
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        face_descriptors.append(np.array(face_descriptor))

    return np.array(face_descriptors)





def facepass():
    # ============유사도 기준 사진 랜드마크 추출==================
    img_paths = {'IYU': './IYU.jpg',}#유사도 기준 사진

    descs = []

    for name, img_path in img_paths.items():
        img = cv2.imread(img_path)
        _, img_shapes, _ = find_faces(img)
        descs.append([name, encode_faces(img, img_shapes)[0]])

    np.save('./descs.npy', descs)
    print(descs)

    # ====================================

    # ============파일 생성========================
    if not path.isdir('./pass'):
        os.mkdir('./pass')

    pathnum = './img'
    file_list = len(os.listdir(pathnum))

    print('파일 개수 {0}개 검출됨'.format(file_list))

    passnum = 0

    for imgnum in range (1,file_list):


        print(imgnum)



        img = cv2.imread('./img/{0}.jpg'.format(imgnum))

        rects, shapes, _ = find_faces(img)  # 얼굴 찾기
        descriptors = encode_faces(img, shapes)  # 인코딩

        for i, desc in enumerate(descriptors):
            x = rects[i][0][0]  # 얼굴 X 좌표
            y = rects[i][0][1]  # 얼굴 Y 좌표
            w = rects[i][1][1] - rects[i][0][1]  # 얼굴 너비
            h = rects[i][1][0] - rects[i][0][0]  # 얼굴 높이

            # 추출된 랜드마크와 데이터베이스의 랜드마크들 중 제일 짧은 거리를 찾는 부분
            descs1 = sorted(descs, key=lambda x: np.linalg.norm([desc] - x[1]))
            dist = np.linalg.norm([desc] - descs1[0][1], axis=1)

            if dist < 0.3:
                shutil.copy('./img/{0}.jpg'.format(imgnum), './pass/{0}.jpg'.format(imgnum))

                print('pass!')
                passnum += 1

            else:
                pass




    print('추출이 끝났습니다. 총 {0}장이 추출되었습니다.'.format(passnum))

