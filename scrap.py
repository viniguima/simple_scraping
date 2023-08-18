import requests
from bs4 import BeautifulSoup

# Lista de URLs para fazer scraping
urls = [
    'https://www.luvizotto.com.br/moveis/moveis-de-madeira/linha-gebb-work.html?p=1',
    'https://www.luvizotto.com.br/moveis/moveis-de-madeira/linha-gebb-work.html?p=2',
    'https://www.luvizotto.com.br/moveis/moveis-de-madeira/linha-gebb-work.html?p=3',
    
]

for url in urls:
    # Faça uma solicitação GET para obter o conteúdo HTML da página
    response = requests.get(url)

    # Analise o conteúdo HTML usando a biblioteca BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontre o elemento da página que contém os dados que você deseja extrair
    data = soup.find_all('h2', {'class': 'product-name'})

    # Imprima o texto dos elementos
    for i in data:
        print(i.get_text(), end=' ')
