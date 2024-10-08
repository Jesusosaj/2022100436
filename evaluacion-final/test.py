from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Configuración de las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Iniciar Chrome maximizado
chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument("--test-type")
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')

# Ruta al ChromeDriver (cambia esto por la ruta donde esté tu chromedriver)
chromedriver_path = chromedriver_path = r'C:\Users\Jesus Sosa\Desktop\python\evaluacion-final\chromedriver.exe'

# Inicializa el servicio de ChromeDriver
service = Service(chromedriver_path)

# Crea una instancia del navegador Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abre la URL de ejemplo
#driver.get('https://www.google.com')
driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')
# Mantiene el navegador abierto durante 10 segundos
#sleep(10)
codigo = driver.find_element(By.ID, 'codigo')
codigo.send_keys("2022100436")
sleep(10)
password = driver.find_element(By.ID, "password")
password.send_keys("Yisus13")
sleep(10)
login = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
login.click()
sleep(10)
# Cierra el navegador después de 10 segundos
driver.quit()
