#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def vitaly_crawler():
    base_url = "http://www.vitalymotors.com.br/Default.aspx" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("div", {"class": "item-car1"})

    for carro in carros:
        modelo = carro.find("span", {"class":"carName"}).text.strip()
        preco = carro.find("label", {"class":"valueName"}).text.strip()
        print(modelo,preco)


