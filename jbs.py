#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests



def jbs_crawler():
    base_url = "http://www.jbsveiculos.com.br/estoque/" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("div", {"class": "car col-1-4"})

    for carro in carros:
        modelo = carro.find("h2", {"class":"car__name"}).text.strip()
        versao = carro.find("p", {"class":"car__description"}).text.split('ANO')[0]
        preco =  carro.find("p", {"class":"car__price"}).text.strip()
        ano = carro.find("p", {"class":"car__description"}).text.split('ANO')[1][1:]
        print(modelo, versao, preco, ano) 




