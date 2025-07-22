from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument(r"CAMINHO DO SEU PERFIL AQUI")

# Argumentos extras para estabilidade
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=options)

driver.get('https://web.whatsapp.com')

print("Aguardando login e carregamento do WhatsApp Web...")

# Espera até que o campo de busca esteja visível (indicando que o login foi concluído)
try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@contenteditable,"true") and @data-tab]'))
    )
    print("WhatsApp Web carregado e logado.")
except Exception as e:
    print("Timeout esperando o WhatsApp Web carregar:", e)
    driver.quit()
    exit()

grupo = "SEU GRUPO AQUI"
mensagem = """SUA MENSAGEM AQUI"""

try:
    print("Tentando encontrar campo de busca (XPath 1)...")
    search_box = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')
    print("Campo de busca encontrado pelo XPath 1.")
except Exception as e1:
    print(f"XPath 1 falhou: {e1}")
    try:
        print("Tentando encontrar campo de busca (XPath 2)...")
        search_box = driver.find_element(By.XPATH, '//div[contains(@contenteditable,"true") and @data-tab]')
        print("Campo de busca encontrado pelo XPath 2.")
    except Exception as e2:
        print(f"XPath 2 falhou: {e2}")
        print("Não conseguiu encontrar campo de busca. Fechando navegador.")
        driver.quit()
        exit()

print("Clique no campo de busca...")
search_box.click()
search_box.clear()
print(f"Digitando nome do grupo: {grupo}")
search_box.send_keys(grupo)
time.sleep(5)
search_box.send_keys(Keys.ENTER)
print("Grupo pesquisado.")

try:
    time.sleep(5)
    print("Tentando encontrar caixa de mensagem...")
    msg_box = driver.find_element(By.XPATH, '//div[contains(@contenteditable,"true") and contains(@data-tab,"10")]')
    print("Caixa de mensagem encontrada.")
    msg_box.click()
    msg_box.send_keys(mensagem)
    msg_box.send_keys(Keys.ENTER)
    print("Mensagem enviada.")
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")

time.sleep(2)
driver.quit()
