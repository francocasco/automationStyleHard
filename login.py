from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()

#Abrir Navegador
d = webdriver.Chrome(options=chrome_options)

d.get("https://style-hard.onrender.com/")

d.maximize_window()


#Login
loginButton=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/button")
loginButton.click()

time.sleep(2)

eml=d.find_element(By.XPATH,"//*[@id='username']").send_keys("PYZXPHNL@EXAMPLE.COM")
psw=d.find_element(By.XPATH,"//*[@id='password']").send_keys("123Fr123#")

lgnbtn=d.find_element(By.XPATH,"/html/body/div[1]/main/section/div/div/div/form/div[3]/button")
lgnbtn.click()


time.sleep(10)

#Desloguear
logoutbtn=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/button")
logoutbtn.click()

d.close()

