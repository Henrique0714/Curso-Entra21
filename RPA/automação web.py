from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# navegador = webdriver.Firefox()
#
# # https://selenium-python.readthedocs.io/
# # https://www.selenium.dev/
#
# navegador.get('https://www.google.com.br/')
# navegador.find_element('name', 'q').send_keys('Senac'+Keys.ENTER)

navegador = webdriver.Firefox()
navegador.get('https://externo.proway.com.br/login-aluno')
navegador.find_element('id', 'formLoginSubscriber_username').send_keys('henrique.samuel7a@gmail.com'+Keys.TAB)
navegador.find_element('id', 'formLoginSubscriber_password').send_keys('02012005'+Keys.ENTER)
sleep(2)
navegador.find_element('xpath' ,  '/html/body/div[1]/section/section/main/div/div/div/ul/li[1]/ul/li/button/span[2]').click()
