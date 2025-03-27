from time import sleep
import requests

def contar_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(f"Aguardando... {i} segundos restantes")
        sleep(1)  # Espera 1 segundo
    print("Espera concluída!")

def post_cep(cep):
    url = f'http://45.77.150.143:4800/cep/{cep}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def criador_cep_aleatorio():
    url ='https://www.4devs.com.br/ferramentas_online.php'
    payload = 'acao=gerar_cep&cep_estado=&cep_cidade=&somente_numeros=S&cep_numeros=8'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.text.split('class="output-txt"><span>')[1][:9].replace('-', '')

# Executor
while True:
    try:
        cep = criador_cep_aleatorio()
        print(cep)
        contar_regressiva(30)
        print(post_cep(cep))
        # print(post_cep)
    except Exception as e:
        print(e)
        print('Tentando novamente')
        contar_regressiva(30)
        