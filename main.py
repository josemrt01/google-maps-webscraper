# Este archivo se usa solo para instanciar instancias. Crear información y ejecutar
from business import Business
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time


def wait_page_loading(type, is_singular, attribute):
    try:
        if is_singular:
            WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((type, attribute)))
        else:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((type, attribute)))
    except TimeoutException:
        print("It hasn't found information on the webpage from ", attribute)


def scroll_the_page(i):
    try:
        while i >= len(driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')):
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'wo1ice-loading')))
            section_loading = driver.find_element_by_class_name('wo1ice-loading')
            actions = ActionChains(driver)
            actions.move_to_element(section_loading).perform()
            time.sleep(1)
    except Exception as e:
        scroll_the_page(i)
    return


def get_back():
    try:
        back = driver.find_element_by_css_selector('[aria-label="Atrás"]')
        back.click()
    except Exception as e:
        driver.back()


def get_value(attribute, type):
    try:
        if(type == 'css'):
            node = driver.find_element_by_css_selector(attribute)
        if(type == 'xpath'):
            node = driver.find_element_by_xpath(attribute)
        if node.text != '':
            value = node.text
        else:
            value = ''
    except NoSuchElementException:
        value = ''
    return value


user_input = input("Write here what you're looking and click Enter: ")
amount_results = 20
try:
    amount_results = int(input("Write the amount of results you need and click Enter: "))
except Exception as e:
    print("There was an error while writing the amount of results. Please execute the program and write it again", str(e))
    exit()
delay = 60
driver = webdriver.Chrome(r'C:\bin\chromedriver.exe')
driver.get("https://www.google.com/maps")
# Busca la barra de búsqueda
driver.switch_to.default_content()
wait_page_loading(By.ID, True, 'searchboxinput')
searchbox = driver.find_element_by_id('searchboxinput')
searchbox.send_keys(user_input)
searchbox.send_keys(Keys.ENTER)

# Busca si existen los primeros contenedores con resultados
wait_page_loading(By.XPATH, True, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]')
print("We've found results.")
parent_tab = driver.window_handles[-1]
# Inicia el proceso de navegación por cada resultado
for i in range(0, int((amount_results/20)+1)):
    # Busca si existen contenedores con resultados
    wait_page_loading(By.XPATH, True, '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]')
    for index in range(0, 20):
        scroll_the_page(index)
        place = driver.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
        driver.execute_script("arguments[0].click();", place[index])
        wait_page_loading(By.XPATH, True, "//h1[contains(@class,'header-title')]")
        name = driver.find_element_by_xpath("//h1[contains(@class,'header-title')]").text
        if Business.is_new(name):
            title = get_value('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button', 'xpath')
            address = get_value("[data-item-id='address']", 'css')
            phone = get_value('[data-tooltip="Copiar el número de teléfono"]', 'css')
            webpage = get_value('[data-tooltip="Abrir el sitio web"]', 'css')
            stars = get_value('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span/span', 'xpath')
            amount_reviews = get_value('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span', 'xpath')
            empresa = Business(name, title, phone, address, webpage, stars, amount_reviews)
            print(f"{len(Business.raw_data['Name'])}) {name}, {title}, {address}, {phone}, {stars}, {amount_reviews}")
        else:
            pass
        if len(Business.raw_data['Name']) == amount_results:
            print('The data is already completed!')
            Business.export_data()
            driver.quit()
            exit()
            print('The project has finished succesfully!')
        get_back()
    wait_page_loading(By.ID, True, 'ppdPk-Ej1Yeb-LgbsSe-tJiF1e')
    next_button = driver.find_element_by_id('ppdPk-Ej1Yeb-LgbsSe-tJiF1e')
    driver.execute_script("arguments[0].click();", next_button)