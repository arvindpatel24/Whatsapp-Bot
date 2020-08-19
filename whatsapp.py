from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import os
from time import sleep
 
driver_loc = 'chromedriver.exe'
os.environ["webdriver.chrome.driver"] = driver_loc
driver = webdriver.Chrome(driver_loc)
driver.get("http://web.whatsapp.com")
driver.maximize_window()
sleep(10)
driver.implicitly_wait(10)

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()

def send_text(num,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(num))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        print('Error',e)
    text_area ='//*[(@id = "main")]//*[contains(concat( " ", @class, " " ), concat( " ", "_3FRCZ", " " ))]'
    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , text_area)
        print("Text Box Found")
        txt_box.send_keys(text)
        txt_box.send_keys('\n')
    except Exception as e:
        print("Not Found: ",e)

def send_img_vid(num,filepath):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(num))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        print('Error',e)  
    try:
        element_presence(By.XPATH,'//div[@title="Attach"]',30)
        attachment = driver.find_element(By.XPATH, '//div[@title="Attach"]')
        attachment.click()
        sleep(1)

        img_vid = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        img_vid.send_keys(filepath)

        send = driver.find_element(By.XPATH,'//span[@data-testid="send"]')
        send.click()
    except Exception as e:
        print("Not Found: ",e)

def send_doc(num,docpath):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(num))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        print('Error',e)  
    try:
        element_presence(By.XPATH,'//div[@title="Attach"]',30)
        attachment = driver.find_element(By.XPATH, '//div[@title="Attach"]')
        attachment.click()
        sleep(1)

        doc = driver.find_element(By.XPATH, '//input[@accept="*"]')
        doc.send_keys(docpath)

        send = driver.find_element(By.XPATH,'//span[@data-testid="send"]')
        send.click()
    except Exception as e:
        print("Not Found: ",e)
num_list = ['919685036275','919799871428']
text_msg = "Automation Testing"
filepath = 'C:\\Users\\Ravi\\Desktop\\Jupyter\\fox.jpg'
docpath = 'C:\\Users\\Ravi\\Desktop\\Jupyter\\FOX Trading Solutions offer letter-Python.docx'

# To send text/imgage & video/ document just change the function name and its parameter
for num in num_list:
    print(num)
    try:
        send_img_vid(num,filepath) # Change here
        sleep(5)
    except Exception as e:
        print(Exception)
        sleep(10)
        is_connected()


        

