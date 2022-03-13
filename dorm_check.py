from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import NoSuchElementException

import pyautogui as pg
import time
import pickle
import os.path

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
url = 'https://dorm.andong.ac.kr/etrappl/chk_self_cond.php'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
#default settings

def loadInformation():
    with open ('dorm_check_information.bin','rb') as f:
        data = pickle.load(f)
    default(data[0],data[1],data[2])
    CheckInfor()

def default(student_num,birth,password): 
    ClearKeys()
    driver.find_element_by_name('id').click()
    action.send_keys(student_num).perform()
    #학번
    driver.find_element_by_name('passwd').click()
    action.send_keys(birth).perform()
    #생년월일
    driver.find_element_by_name('in_pwd_1').click()
    action.send_keys(password).perform()
    #비밀번호

    driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/input[1]').click()
    #입력 버튼 click
    time.sleep (1)
    try:
        driver.find_element_by_xpath('//*[@id="proceed-button"]').click()
        #insecure warning click
    except (NoSuchElementException):
        pass
    time.sleep(0.5)
    #due to loading

def check ():
    driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[1]/div/label[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[3]/div/label[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[2]/div/label[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[4]/div/label[1]').click()
    driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div[5]/div/label[1]').click()
    driver.find_element_by_xpath('/html/body/div[2]/input[1]').click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    a = pg.alert(text='자가진단이 완료되었습니다', title='ANU Dorm COVID Self Check Assistant', button='OK')
    driver.quit()

def SaveInformation ():
    student_num = pg.prompt(text='학번을 입력하세요', title='ANU Dorm COVID Self Check Assistant', default='20220987')
    birth = pg.prompt(text='생일을 입력하세요', title='ANU Dorm COVID Self Check Assistant', default='030101')
    password = pg.prompt(text='비밀번호를 입력하세요', title='ANU Dorm COVID Self Check Assistant', default='1q2w3e4r')
    data = [student_num, birth, password]
    with open('dorm_check_information.bin','wb') as f:
        pickle.dump(data, f)

def ClearKeys():
    driver.find_element_by_name('id').clear()
    driver.find_element_by_name('passwd').clear()
    driver.find_element_by_name('in_pwd_1').clear()

def InformationError ():
    b = pg.confirm(text='관생정보가 일치하지 않습니다 \n 관생정보를 다시 입력하시겠습니까?',title='ANU Dorm COVID Self Check Assistant',buttons=['Yes','No'])
    if b == 'Yes':
        SaveInformation()
        loadInformation()

def CheckInfor():
    try:
        check_text = driver.find_elements_by_xpath("/html/body/div[1]/form/div[1]")
    except WDE:
        InformationError()
    try:
        if ((check_text[0].text) == "오늘 제출하지 않았습니다."):
            checkbox = pg.confirm(text='오늘 자가진단을 제출하지 않았습니다. 자동으로 제출하시겠습니까?', title='ANU Dorm COVID Self Check Assistant', buttons=['OK','Cancel'])
            if checkbox == 'OK':
                check()
    except NameError:
        InformationError()
if not (os.path.isfile('dorm_check_information.bin')):
    SaveInformation()

loadInformation()
