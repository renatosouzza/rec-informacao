#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def mercadolivre_crawler():
    base_url = "https://lista.mercadolivre.com.br/carros-usados#D[A:carros-usados,B:1]" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("li", {"class": "results-item"})

    for carro in carros:
        modelo = carro.find("span", {"class":"main-title"}).text.strip()
        preco =  carro.find("span", {"class":"price-fraction"}).text.strip()
        ano = carro.find("div", {"class":"item__attrs"}).text.strip().split()[0]
        print(modelo, preco, ano)



