from selenium import webdriver
import time
from PIL import Image
import os
from module import *

file_name = "E:/test.png"
abspath = os.path.abspath(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome(abspath)
driver.get("https://fangkong.hnu.edu.cn/app/#/login?redirect=%2Fhome")
print(driver.title)
driver.maximize_window()
time.sleep(2)

# 1.登录页面截图并保存在E:/test.png
driver.save_screenshot(file_name)
# 2.获取图片验证码坐标和尺寸
code_element = driver.find_element_by_xpath(".//*[@id='verifyCodeImg']")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open(file_name)
# 3.截取图片验证码
img = im.crop((left, top, right, height))
# 4.截取的验证码图片保存为新的文件
img.save(file_name)
driver.close()