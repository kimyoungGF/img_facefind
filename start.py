from module.instarimg import selfcamcollect
from module.face_s import facepass
import sys

while True:
    while True:
        print('얼굴 추출을 시작하시겠습니까?')
        x = input('Y or N : ')
        if x=='Y'or x=='y':
            selfcamcollect()
            break
        elif x=='N' or x=='n':
            break
        else:
            print('다시 입력해 주십시오')
            pass

    while True:
        print('얼굴 유사도 추출을 시작하시겠습니까?')
        y = input('Y or N : ')
        if y=='Y' or y== 'y':
            facepass()
            break
        elif y=='N'or y=='n':
            break
        else:
            print('다시 입력해 주십시오')
            pass

    while True:
        print('프로그램을 종료하시겠습니까?')
        a = input('Y or N : ')
        if a=='Y' or a== 'y':
            sys.exit()
        elif a=='N' or a=='n':
            break
        else:
            print('다시 입력해 주십시오')
            pass

