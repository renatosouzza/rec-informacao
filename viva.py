#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def viva_crawler():
    base_url = "http://www.vivalocal.com/auto-veiculo-usado/br" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("tr", {"class": "classified"})

    for carro in carros:
        modelo = carro.find("a", {"class":"kiwii-clear-none"}).text.strip()
        preco =  carro.find("div", {"class":"price"}).text.strip()
        print(modelo, preco)




