#!/usr/bin/env python
# -*- coding: utf-8 -*-
from webmotors import webmotors_crawler
from rede import rede_crawler
from vitaly import vitaly_crawler
from pastore import pastore_crawler
from jbs import jbs_crawler
from mercadolivre import mercadolivre_crawler
from meucarango import meucarango_crawler

while True:
    loja = input("\n w: Webmotors \n j: JBS veiculos \n v: Vitaly motors \n p: Pastore car collection \n r: Rede brasil motors \n 0: Para sair \n")
    if loja == "w":
        webmotors_crawler()
    elif loja == "j":
        jbs_crawler()
    elif loja == "v":
        vitaly_crawler()
    elif loja == "p":
        pastore_crawler()
    elif loja == "r":
        rede_crawler()
	elif loja == "m":
        mercadolivre_crawler()
	elif loja == "c":
        meucarango_crawler()
    elif loja == "0":
        break
    else:
        print("\n Opção Inválida")
        


