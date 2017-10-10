#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def olx_crawler():
    base_url = "http://pe.olx.com.br/veiculos-e-acessorios/carros" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("a", {"class": "OLXad-list-link"})

    for carro in carros:
        modelo = carro.find("h3", {"class":"OLXad-list-title mb5px"}).text.strip()
        preco =  carro.find("p", {"class":"OLXad-list-price"})
        preco = preco.text.strip() if preco else ' '
        print(modelo, preco)



