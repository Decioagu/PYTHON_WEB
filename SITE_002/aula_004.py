# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path # caminho
from time import sleep # esperar tempo

from selenium import webdriver # permite que você interaja com navegadores web
from selenium.webdriver.chrome.service import Service # responsável iniciar chromedriver
from selenium.webdriver.common.by import By # selecionar "nome html" na Tag
from selenium.webdriver.common.keys import Keys # pressionar tecla

# OBS: módulos abaixo trabalham em conjunto:
from selenium.webdriver.support import expected_conditions as EC # esperar eventos específicos na página web.
from selenium.webdriver.support.wait import WebDriverWait # espera resposta (By)

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions() #  inicialização do ChromeDriver.
    # print('options =',options)
    
    # type: ignore
    # if options is not None:
    #     for option in options:
    #         chrome_options.add_argument(option)  

    # instanciar caminho para execução do ChromeDriver
    chrome_service = Service(executable_path = CHROME_DRIVER_PATH) 

    # criar um novo objeto  para controlar o navegador Google Chrome
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    TEMPO_DE_ESPERA = 10

    options = ()
    browser = make_chrome_browser(*options)

    # SITE
    browser.get('https://www.google.com')

    '''
        O módulo selenium.webdriver.common.by fornece uma classe By que 
        contém os seguintes tipos de locators:

        ID: localiza um elemento pelo seu ID.
        NAME: localiza um elemento pelo seu nome.
        TAG_NAME: localiza um elemento pelo seu nome de tag.
        CLASS_NAME: localiza um elemento pela sua classe CSS.
        CSS_SELECTOR: localiza um elemento por um seletor CSS.
        XPATH: localiza um elemento por um XPath.
    '''
    # Espere para encontrar
    try:
        campo_input = WebDriverWait(browser, TEMPO_DE_ESPERA).until(
        EC.presence_of_element_located((By.NAME, 'q')) # 'q' nome no navegador "HTML"
        )
    except:
        print('#################### SEM RESPOSTA ####################')
    else:
        print('#################### EXECUTADO ####################')
        campo_input.send_keys('Hello World!') # enviar ao SITE (campo de pesquisa)
        campo_input.send_keys(Keys.ENTER) # pressionar tecla enter SITE

    finally:
        print('#################### FINALIZADO ####################')

    # seleção de link no navegador
    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # esperar resultado (segundos)
    sleep(TEMPO_DE_ESPERA)
