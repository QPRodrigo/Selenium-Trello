# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver
#
from datos import datos_personales
#Libreria Tiempo de espera 
import time


#Clases
class EspacioTrabajo(unittest.TestCase):
    
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = r'.\..\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("https://trello.com/")
    
	def test_new_user(self):
		driver = self.driver
		driver.find_element_by_xpath('/html/body/header/nav/div/a[1]').click()
		time.sleep(1)

		#comprueba que estamos en el sitio de crear cuenta por el titulo de la pagina
		self.assertEqual('Log in to Trello', driver.title)
		time.sleep(1)

		#creación de variables con el nombre del selector correspondiente
		user = driver.find_element_by_id('user')
		password = driver.find_element_by_id('password')
		submit_button_login_user = driver.find_element_by_id('login')
		
		#veremos si los elementos están habilitados
		self.assertTrue(user.is_enabled() 
		and password.is_enabled()
		and submit_button_login_user.is_enabled())

		#mandamos los datos al formulario
		user.send_keys(datos_personales.email_address)
		submit_button_login_user.click()
		time.sleep(1)

		password_2 = driver.find_element_by_id('password')
		#mandamos el password al formulario
		password_2.send_keys(datos_personales.password)	
		driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[3]/button').click()
		time.sleep(10)


		#En el archivo datos.py
		#class datos_personales:
		#	email_address = 'correo
		#	password = 'contraseña'


	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
    #testRunner para que genere el reporte
    #output donde se va a guardar las pruebas
    #report_name el nombre de las pruebas.
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'Login'))