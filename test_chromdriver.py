import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pg

driver = webdriver.Chrome()
a = pg.alert(text='크롬이 열렸다면 성공입니다.', title='ANU Dorm COVID Self Check Assistant', button='OK')