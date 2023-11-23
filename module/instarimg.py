from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from os import path

#=====src추출 함수=====
def collectsrc(driver,p,imgsrc):
    for num in range(100):
        k = driver.find_elements_by_class_name('_aagt')

        for uurl in k:
            imgsrc.add(uurl.get_attribute('src'))
        p.send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
    print('지금까지 수집한 이미지의 src 총 개수 : ', len(imgsrc))




def selfcamcollect():


    #===========크롬드라이버=========
    chrome = 'c:/temp/chromedriver.exe'

    driver = webdriver.Chrome(chrome)


    # ===========로그인정보, 검색할것=========
    ID = '--'
    PW = '--'
    SH = '#셀카'



    # ===========주소입력=========
    url = 'https://www.instagram.com/'
    driver.get(url)
    driver.implicitly_wait(3)



    # ===========로그인과 창 뜨면 제거=========
    e = driver.find_element_by_name('username')
    e.clear()
    e.send_keys(ID)

    e = driver.find_element_by_name('password')
    e.clear()
    e.send_keys(PW)

    e.send_keys(Keys.ENTER)

    time.sleep(5)


    try:
        driver.find_element_by_class_name("cmbtv").click()
    except:
        pass

    try:
        driver.find_element_by_class_name("_a9--._a9_1").click()
    except:
        pass

    print("로그인 성공{0}를 검색합니다.".format(SH))

    time.sleep(3)

    # ===========검색============
    e = driver.find_element_by_class_name('_aawh._aawj._aauy')
    time.sleep(2)
    e.clear()
    time.sleep(2)
    e.send_keys(SH)

    time.sleep(10)

    e = driver.find_element_by_class_name('_abnr._abnu')
    time.sleep(2)
    e.click()

    time.sleep(15)


    # ===========src수집=========
    imgsrc=set()
    p = driver.find_element_by_class_name('_aacl._aacs._aact._aacx._aad6')


    print("파일 추출을 시작합니다.")

    collectsrc(driver, p, imgsrc)

    while True:
        YN = input('더 수집하시겠습니까? Y,N : ')

        if YN=='Y' or YN=='y':
            collectsrc(driver, p, imgsrc)
        elif YN=='N' or YN=='n':
            break
        else:
            print('잘못입력하셨습니다.')
            pass

    # ===========파일 생성=========
    if not path.isdir('./img/'):
        os.mkdir('./img/')
    list_imgsrcs = list(imgsrc)

    filenum = './img'


    # ===========이미지 추출=========
    print('이미지 추출 중.....')
    imgcount=len(os.listdir(filenum))
    count=1

    for list_imgsrc in list_imgsrcs:
        urllib.request.urlretrieve(list_imgsrc, './img/'+"{0}.jpg".format(count+imgcount))
        count+=1

    print('추출 끝')

'''

            https://velog.io/@bi-sz/Python-Web-Crawling-2
            https://0ver-grow.tistory.com/997
            
            https://ukayzm.github.io/python-face-recognition/
            
            https://sulastri.tistory.com/3
            imgsrc.add(k[0].get_attribute('src'))'''








