from time import sleep
import requests

def post_cep(cep):
    url = f'http://45.77.150.143:4800/cep/{cep}'
    response = requests.get(url)
    return response.json()

def criador_cep_aleatorio():
    url ='https://www.4devs.com.br/ferramentas_online.php'
    payload = 'acao=gerar_cep&cep_estado=&cep_cidade=&somente_numeros=S&cep_numeros=8'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text.split('class="output-txt"><span>')[1][:9].replace('-', '')

# Executor
while True:
    cep = criador_cep_aleatorio()
    print(cep)
    sleep(30)
    print(post_cep(cep))
    print(post_cep)