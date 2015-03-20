# coding: utf-8
from datetime import date


class Usuario(object):

    def __init__(self, nome, senha, cnpj, codigo_admin, num_contrato,
                 cartao_postagem):
        self.nome = nome
        self.senha = senha
        self.codigo_admin = codigo_admin
        self.num_contrato = num_contrato
        self.ano_contrato = date()
        self.cartao_postagem = cartao_postagem
        self.cnpj = cnpj
