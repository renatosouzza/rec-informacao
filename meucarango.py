#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def meucarango_crawler():
    base_url = "https://www.meucarango.com.br/buscar/tipo.carro/tipo-veiculo.novos-usados/anunciante.loja?tipoveiculo=carro&anunciante=loja%7Cconcession%C3%A1ria%7Cpessoa%20f%C3%ADsica&tipoanuncio=novos%7Cusados" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("a", {"class": "nn tipo1 c-after"})

    for carro in carros:
        modelo = carro.find("span", {"class":"make-model"}).text.strip()
        versao = carro.find("span", {"class":"version"}).text.strip()
        preco =  carro.find("div", {"class":"price"}).text.strip()
        ano = carro.find("div", {"class":"features"}).text.strip().split()[0]
        print(modelo, versao, preco, ano)
    



