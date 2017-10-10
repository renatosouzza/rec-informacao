#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def icarros_crawler():
    base_url = "http://www.icarros.com.br/ache/listaanuncios.jsp?bid=0&opcaocidade=1&foa=1&anunciosNovos=1&anunciosUsados=1&marca1=0&anomodeloinicial=0&anomodelofinal=0&precominimo=0&precomaximo=0&cidadeaberto=&escopo=2&locationSop=cid_7043.1_-est_RJ.1_-esc_2.1_-rai_25.1" # url do site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'} # simular cabeçalho de um navegador se não da 403
    r = requests.get(base_url, headers=headers) # faz a requisição
    c = r.content # retorna o html
    html = BeautifulSoup(c,"html.parser") # parseia
    carros = html.find_all("div", {"class": "anuncio_container"})

    for carro in carros:
        modelo = carro.find("h2", {"class":"esquerda titulo_anuncio"}).text.strip()
        versao = carro.find("p", {"class":"texto_padrao texto_padrao_montadora"}).text.strip()
        preco =  carro.find("h3", {"class":"direita preco_anuncio"}).text.strip()
        ano = carro.find("li", {"class":"primeiro"}).text.strip()
        print(modelo, versao, preco, ano)

    



