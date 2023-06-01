import cv2
from os import path
import os
import shutil

if not path.isdir('./class'):
    os.mkdir('./class/')

if not path.isdir('./face_only'):
    os.mkdir('./face_only/')

pathnum = './img'
file_list = len(os.listdir(pathnum))

print('파일 개수 {0}개 검출됨'.format(file_list))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

facenum=0

for imgnum in range(1,file_list):
    img = cv2.imread('./img/{0}.jpg'.format(imgnum))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    try:
        if (len(faces)>0):
            facenum+=1

            for (x, y, w, h) in faces:
                #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                cropped = img[y - int(h/3):y + h + int(h/3), x - int(w/3):x + w + int(w/3)]
                cv2.imwrite("./face_only/{0}.jpg".format(facenum), cropped)
                '''
                # 눈 찾기
                roi_color = img[y:y + h, x:x + w]
                roi_gray = gray[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)'''



            shutil.copy('./img/{0}.jpg'.format(imgnum), './class/{0}.jpg'.format(imgnum))
            file_oldname = os.path.join('./class/{0}.jpg'.format(imgnum))
            file_newname_newfile = os.path.join('./class/face{0}.jpg'.format(facenum))

            os.rename(file_oldname, file_newname_newfile)

            print('{0}'.format(imgnum))



        else:
            pass
    except:
        print('{0}번 추출실패'.format(imgnum))
        pass


print('얼굴 인식 된 사진 개수 = {0}개'.format(facenum))




#cv2.imshow('image', img)

#key = cv2.waitKey(0)
#cv2.destroyAllWindows()


#https://minimin2.tistory.com/139