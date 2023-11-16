from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

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

time.sleep(5)
#Boton productos
productosbtn=d.find_element(By.XPATH,"/html/body/div/div/div[1]/a[2]/span")
productosbtn.click()

#Ir a productos
productosbtn=d.find_element(By.XPATH,"/html/body/div/div/div[1]/a[2]/span")
productosbtn.click()
#Elegir procesador Amd
proceamd=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div[4]/div/a/img")
proceamd.click()
#almacenar precio en una variable
precio=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/p[2]").text
#subir cantidad
cant=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div/button[2]")
cant.click()
#agregar al carrito
addbtn=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/button")
addbtn.click()
#ir al carrito
time.sleep(3)
carritobtn=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/a[1]/button")
carritobtn.click()
#verificar precio total
preciototal=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/h2").text

# Función para extraer el número de una cadena
def extraer_numero(cadena):
    return int(''.join(filter(str.isdigit, cadena)))

# Extraer los números de las cadenas
precio_numero = extraer_numero(precio)
total_numero = extraer_numero(preciototal)

if precio_numero == total_numero:
    print(f"El Precio '{precio_numero}' es igual al precio total '{total_numero}'.")
else:
    print(f"El Precio '{precio_numero}' es diferente al precio total '{total_numero}'.")
#Finalizar compra
finalizarbtn=d.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/button")
finalizarbtn.click()

time.sleep(10)

d.close()

