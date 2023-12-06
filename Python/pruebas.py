import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from HtmlTestRunner import HTMLTestRunner
import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from utils import Utils;

class TestUserCRUD(unittest.TestCase):
    def setUp(self):
        url = "http://127.0.0.1:5500/index.htm"
        path_driver = os.chdir(r"C:\chrome")
        chrome_options = Options()
        chrome_options.add_argument("C:\\path\\to\\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()

    def take_screenshot(self, test_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_filename = f'{test_name}_screenshot_{timestamp}.png'
        screenshot_filepath = os.path.join("C:\\Users\\IngCa\\Downloads\\Prueba\\Python\\assets\\img", screenshot_filename)
        self.driver.save_screenshot(screenshot_filepath)

        # Esperar hasta que el elemento newUserBtn esté presente en la página
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "newUserBtn"))
        )
        #//*[@id="newUserBtn"]

    def test_cargar_user(self):

        # Verificación: Usuario creado correctamente
        #//*[@id="userTableBody"]
        user_table_body = self.driver.find_element(By.XPATH, '//*[@id="userTableBody"]')
        self.assertIn("Jean Carlos", user_table_body.text)
        self.take_screenshot("test_cargar_user_exitoso")

    def test_create_user(self):

        Element_Btn_NewUser = self.driver.find_element(By.XPATH, '//*[@id="newUserBtn"]')
        Element_Btn_NewUser.click()

        Element_Nombre = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
        )
        Element_Apellido = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]'))
        )
        Element_edad = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="age"]'))
        )
        #XPATH AGREGAR
        #//*[@id="name"]
        #//*[@id="lastName"]
        #//*[@id="age"]

        Utils.escribir(Element_Nombre, "Alexander")
        Utils.escribir(Element_Apellido, "Campusano")
        Utils.escribir(Element_edad, "21")

        Element_Btn_SaveNewUser = self.driver.find_element(By.XPATH, '//*[@id="saveBtn"]')
        Element_Btn_SaveNewUser.click()

        self.take_screenshot("test_create_user_exitoso")
        # Verificación: Usuario creado correctamente
        #//*[@id="userTableBody"]
        user_table_body = self.driver.find_element(By.XPATH, '//*[@id="userTableBody"]')
        self.assertIn("Alexander", user_table_body.text)
        
    def test_create_user_fail(self):

        Element_Btn_NewUser = self.driver.find_element(By.XPATH, '//*[@id="newUserBtn"]')
        Element_Btn_NewUser.click()

        Element_Nombre = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
        )
        Element_Apellido = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]'))
        )
        Element_edad = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="age"]'))
        )

        # Introducir un nombre muy corto (menos de 3 caracteres)
        Utils.escribir(Element_Nombre, "Al")

        Utils.escribir(Element_Apellido, "Campusano")
        # Introducir una edad no válida (por ejemplo, una cadena en lugar de un número)
        Utils.escribir(Element_edad, "Veintiuno")

        Element_Btn_SaveNewUser = self.driver.find_element(By.XPATH, '//*[@id="saveBtn"]')
        Element_Btn_SaveNewUser.click()

        self.take_screenshot("test_create_user_fail")
        # Verificación: Mensaje de error visible en la interfaz de usuario
        error_message = self.driver.find_element(By.XPATH, '//*[@id="errorMessage"]')
        self.assertTrue(error_message.is_displayed())


    def test_editar_user(self):
        #
        #//*[@id="editBtn"]
        Element_Btn_EditarUser = self.driver.find_element(By.XPATH, '//*[@id="editBtn"]')
        Element_Btn_EditarUser.click()

        Element_Apellido = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]'))
        )
        Element_Nombre = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
        )
        Element_edad = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="age"]'))
        )
        #XPATH AGREGAR
        #//*[@id="name"]
        #//*[@id="lastName"]
        #//*[@id="age"]

        Element_Nombre.clear()
        Utils.escribir(Element_Nombre, "Prof. Kelyn")
        Element_Apellido.clear()
        Utils.escribir(Element_Apellido, "Tejada Belliard")
        Element_edad.clear()
        Utils.escribir(Element_edad, "45")

        Element_Btn_SaveNewUser = self.driver.find_element(By.XPATH, '//*[@id="saveBtn"]')
        Element_Btn_SaveNewUser.click()

        self.take_screenshot("test_editar_user_exitoso")

        # Verificación: Usuario editado correctamente
        #//*[@id="userTableBody"]
        user_table_body = self.driver.find_element(By.XPATH, '//*[@id="userTableBody"]')
        self.assertIn("Prof. Kelyn", user_table_body.text)

    def test_eliminar_user(self):
        Element_Btn_EliminarUser = self.driver.find_element(By.XPATH, '//*[@id="deleteBtn"]')
        Element_Btn_EliminarUser.click()

        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert
        alert.accept()

        user_table_body = self.driver.find_element(By.XPATH, '//*[@id="userTableBody"]')
        self.assertNotIn("Kelyn", user_table_body.text)

        self.take_screenshot("test_eliminar_user_exitoso")

    def test_edad_verific_user(self):
        Element_Btn_NewUser = self.driver.find_element(By.XPATH, '//*[@id="newUserBtn"]')
        Element_Btn_NewUser.click()

        Element_Nombre = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
        )
        Element_Apellido = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]'))
        )
        Element_edad = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="age"]'))
        )

        # XPATH AGREGAR
        # //*[@id="name"]
        # //*[@id="lastName"]
        # //*[@id="age"]

        Utils.escribir(Element_Nombre, "Alexander")
        Utils.escribir(Element_Apellido, "Campusano")
        Utils.escribir(Element_edad, "ABC")

        Element_Btn_SaveNewUser = self.driver.find_element(By.XPATH, '//*[@id="saveBtn"]')
        Element_Btn_SaveNewUser.click()

if __name__ == "__main__":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f'reporte_pruebas_{timestamp}.html'
    report_filepath = os.path.join(os.getcwd(), report_filename)
    unittest.main(testRunner=HTMLTestRunner(output=report_filepath))
