from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

#Metodo para generar un email random
def generar_email():
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "example.com", "domain.com"]

    # Genera una cadena aleatoria de longitud 8
    nombre_usuario = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    # Selecciona un dominio aleatorio de la lista
    dominio = random.choice(dominios)

    # Concatena el nombre de usuario y el dominio para formar el correo electrónico
    email = f"{nombre_usuario}@{dominio}"

    return email.upper()


chrome_options = webdriver.ChromeOptions()


#Abrir Navegador
d = webdriver.Chrome(options=chrome_options)

d.get("https://style-hard.onrender.com/")

d.maximize_window()

loginButton=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/button")
loginButton.click()

time.sleep(2)

signup=d.find_element(By.XPATH,"/html/body/div[1]/main/section/div/div[2]/div/div[1]/p/a")
signup.click()

bufferEmail=generar_email()
eml=d.find_element(By.XPATH,"//*[@id='email']").send_keys(bufferEmail)
psw=d.find_element(By.XPATH,"//*[@id='password']").send_keys("123Fr123#")

continuergstr=d.find_element(By.XPATH,"/html/body/div[1]/main/section/div/div/div/form/div[3]/button")
continuergstr.click()

time.sleep(3)

#Verificar email
usrbtn=d.find_element(By.XPATH,"//html/body/div[1]/div/div[2]/div[1]/h4")
usrtxt=usrbtn.text

time.sleep(5)

# Verificar si el correo electrónico aleatorio es igual al correo electrónico ingresado
if bufferEmail == usrtxt:
    print(f"El correo electrónico aleatorio '{bufferEmail}' es igual al correo ingresado '{usrtxt}'.")
else:
    print(f"El correo electrónico aleatorio '{bufferEmail}' es diferente al correo ingresado '{usrtxt}'.")

time.sleep(10)

#Desloguear
logoutbtn=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/button")
logoutbtn.click()

d.close()
