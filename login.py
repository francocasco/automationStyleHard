from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Configurar para abrir con extension
profile_path = r"C:\Users\QA-User118\AppData\Local\Google\Chrome\User Data\System Profile"
# Ruta a la extensión de Chrome Xpath finder(archivo .crx o carpeta descomprimida)
extension_path = r'C:\Users\QA-User118\Documents\drivers\ihnknokegkbpmofmafnkoadfjkhlogph-1.0.2-Crx4Chrome.com.crx'
# Configurar opciones del navegador para instalar la extensión
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension(extension_path)

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

