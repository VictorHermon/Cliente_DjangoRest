import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    """Verifica se o CPF digitado é valido"""
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    """Verifica se o nome digitado possui números"""
    modelo_nome = '[0-9]'
    nome_correto = re.findall(modelo_nome, nome)
    return nome_correto


def rg_valido(rg):
    """Verifica se o RG digitado tem 9 digitos"""
    return len(rg) == 9


def celular_valido(numero_celular):
    """Verifica se o número de celular está no modelo (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta
