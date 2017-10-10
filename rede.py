#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def rede_crawler():
    base_url = "http://www.redebrasilmotors.com.br/portal/busca?categoria=3&id_marca=0&id_modelo=&de=min&ate=max&regiao=0&cidade=&limit=w3tdm&organizar=&condicoes=t&cores=&combustivel=&km-min=&km-max=" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("div", attrs={"style": "padding: 0; padding-top: 22px"})

    for carro in carros:
        modelo = carro.find("span", attrs={"style": "font-size: 20px"}).text.split("\n")[1].strip()
        versao = carro.find("span", attrs={"style": "font-size: 20px"}).text.split("\n")[4].strip()
        preco =  carro.find("span", attrs={"style": "font-size: 25px;"}).text.strip()
        ano = carro.find("div", attrs={"style": "font-size: 16px; padding: 0"}).text.strip()
        print(modelo,versao,preco, ano)






