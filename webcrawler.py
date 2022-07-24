from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import zipfile
import os
from pathlib import Path

chromedriver_path = r"C:\Users\Administrator\Desktop\chromedriver.exe"  # 改成你的chromedriver的完整路径地址

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium

browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
wait = WebDriverWait(browser, 1)  # 超时时长为10s

url = 'https://leetcode.com/problems/combine-two-tables/'

browser.get(url)


filename_class = browser.find_element(by=By.XPATH,
                                      value='/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]').text

print(filename_class)

w_list=filename_class.split('\n')


file_write_obj = open("temp.txt", 'w')
for var in w_list:
    file_write_obj.writelines(var)
    file_write_obj.write('\n')
file_write_obj.close()



from openpyxl import load_workbook

wb = load_workbook(r'C:\Users\Administrator\Desktop\leetcode\Book2.xlsx') # Excel工作簿绝对路径
cell = wb['Sheet1'] # Excel工作表名称
hyperlink = cell['A{}'.format(row)].hyperlink.display # 超链接所在单元格


for row in range(179,210):
    title=cell['A{}'.format(row)].value
    title=title.replace('/','_')
    title = title.replace(':', '_')
    link = cell['A{}'.format(row)].hyperlink.display
    browser.get(link)
    time.sleep(3)
    content1=browser.find_element(by=By.XPATH,
                  value='/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]').text
    content2=browser.find_element(by=By.XPATH,
                  value='/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]').text

    if os.path.exists("{}.txt".format(title)):
        os.remove("{}.txt".format(title))

    file_write_obj = open("{}.txt".format(title), 'w')
    for var in content1.split("\n"):
        file_write_obj.writelines("#  "+var)
        file_write_obj.write('\n')
    file_write_obj.writelines("\n#Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content##Content#\n\n")
    for var in content2.split("\n"):
        file_write_obj.writelines("#  "+var)
        file_write_obj.write('\n')
    file_write_obj.writelines("\n#Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution##Solution#\n\n")
    file_write_obj.close()





