#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def webmotors_crawler():
    base_url = "https://www.webmotors.com.br/carros/estoque?tipoveiculo=carros&estadocidade=estoque" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("a", {"class": "nn tipo1 c-after"})

    for carro in carros:
        modelo = carro.find("span", {"class":"make-model-financiamento"}).text.strip()
        versao = carro.find("span", {"class":"version"}).text.strip()
        preco =  carro.find("div", {"class":"price-novo space-preco"}).text.strip()
        ano = carro.find("div", {"class":"info-veiculo-detalhe"}).text.strip()
        print(modelo, versao, preco, ano)



