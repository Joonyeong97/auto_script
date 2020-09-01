# main.py

import sys
import os
import time

from chromedriver import generate_chrome


PROJECT_DIR = str(os.path.dirname(os.path.abspath(os.getcwd())))
DOWNLOAD_DIR = f'{PROJECT_DIR}/download'
driver_path = f'{PROJECT_DIR}/lib/webDriver/'

platform = sys.platform
if platform == 'darwin':
    print('System platform : Darwin')
    driver_path += 'chromedriver_mac'
elif platform == 'linux':
    print('System platform : Linux')
    driver_path += 'chromedriver_linux'
elif platform == 'win32':
    print('System platform : Window')
    driver_path += 'chromedriver_win.exe'
else:
    print(f'[{sys.platform}] not supported. Check your system platform.')
    raise Exception()

# 크롬 드라이버 인스턴스 생성
chrome = generate_chrome(
    driver_path=driver_path,
    headless=False,
    download_path=DOWNLOAD_DIR)

# 페이지 요청
url = 'https://github.com/login'
chrome.get(url)
time.sleep(3)