#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Criado por : Lucas Souza e Silva - 7561
# Data de criação: 25/03/2024 
# versão ='1.0'
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
""" Classe String contendo alguns métodos de manipuação de
textos"""
# ---------------------------------------------------------------------------

class String:
    __texto = ""
    
    def digitaString(self):
        self.__texto = input('Digite a sua string: ')
    
    def imprimeString(self):
        return self.__texto
    
    def comprimento(self):
        return len(self.__texto)
        
s = String()
s.digitaString()
print("String:", s.imprimeString() )
print(s.imprimeString(), "possui", s.comprimento(), "caracteres")
    