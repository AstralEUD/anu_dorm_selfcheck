# anu_dorm_selfcheck
Automate ANU dorm selfcheck (due to HTTP problem)
기숙사 자가진단 자동화 도우미

이 프로그램은 다음과 같은 문제로 부터 비롯됨
 * HTTP 보안 문제로 인해 (https > http로 이동시 오류 표출) 모바일 일부 웹 브라우저에서 자가진단이 불가했음.
 * 자가진단 미 제출시 벌점부여가 있었음.
 
 이 프로그램은 다음과 같은 모듈을 이용함
  * pyautogui (GUI)
  * selenium (자동화를 위한 웹 관련 모듈)
  * chromedriver_autoinstaller (자동화에 쓰이는 크롬드라이버 설치 모듈)

## Requirements
 * pyautogui
 * selenium
 * chromedriver_autoinstaller

## What This Program Does
* Due to the HTTP problem, I have to automate the selfcheck process.
* This program will open the dorm selfcheck page, and do self-check by your information.
