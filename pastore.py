#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def pastore_crawler():
    base_url = "http://www.pastorecc.com.br/carros" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find("ul", {"class": "concerta paginate"})
    carros = carros.find_all("li")

    for carro in carros:
        modelo = carro.find("strong", {"class":"title"}).text.strip()
        detalhes_url = carro.find("a", {"class":"see-details"})['href']
        r = requests.get(detalhes_url, headers=headers)
        c = r.content # retorna o html
        html = BeautifulSoup(c,"html.parser")
        detalhes =  html.find("ul", {"class": "concerta"}).text.strip()
        print(modelo)
        print(detalhes)
        print("===========================================================")



