'''
    Selenium é uma biblioteca de automação web que permite controlar um navegador
    e interagir com seus elementos. Ele pode ser usado para executar tarefas repetitivas 
    em sites da web, como preencher formulários, fazer compras online ou realizar testes 
    de software.
'''

# Selenium - Automatizando tarefas no navegador (Aula 315)
from pathlib import Path
from time import sleep

from selenium import webdriver # permite que você interaja com navegadores web
from selenium.webdriver.chrome.service import Service # responsável iniciar chromedriver

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
    # Chrome options:
    # https://peter.sh/experiments/chromium-command-line-switches/
    # options = ('--headless') # executa sem abrir navegador = '--disable-gpu'
    # options = ('--disable-gpu') # executa sem abrir navegador = '--headless'
    options = ()
    browser = make_chrome_browser(*options)

    # Abrir SITE
    url = 'https://www.google.com.br/' # SITE
    browser.get(url) # obter da web

    # Dorme por 10 segundos
    sleep(10)
