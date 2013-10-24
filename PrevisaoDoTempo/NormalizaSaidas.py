# coding=utf-8
import cPickle as pickle
from dateutil.parser import parse
'''
def __lerarquivo__():
    with open('A702.pickle', 'r') as arquivo:
        return pickle.load(arquivo)


def __salvararquivo__(normalizado, variavel):
    with open('A702_' + variavel + '_Proximas6Horas.pickle', 'wb') as arquivo:
        pickle.dump(normalizado, arquivo)


def __parserDataEmHora__(dataStr):
    return parse(dataStr).hour


def __normaliza__(arquivo, variavel):
    output = []
    size = len(arquivo)
    for i, hour in enumerate(arquivo):
        max = i + 6
        if max == size:
            break
        saida = []
        for horas in range(1, 7):
            saida.append(float(arquivo[i + horas][variavel]))
        output.append(saida)
    return output


def main():
    arquivo = __lerarquivo__()
    variaveis = ['t', 'chuva', 'radiacao']
    for variavel in variaveis:
        normalizado = __normaliza__(arquivo, variavel)
        __salvararquivo__(normalizado, variavel)'''

def __lerarquivo__():
    with open('A702.pickle', 'r') as arquivo:
        return pickle.load(arquivo)


def __salvararquivo__(normalizado, i, variavel):
    with open('A702_' + variavel + '+' + str(i) + '.pickle', 'wb') as arquivo:
        pickle.dump(normalizado, arquivo)


def __parserDataEmHora__(dataStr):
    return parse(dataStr).hour


def __normaliza__(arquivo, hora, variavel):
    output = []
    size = len(arquivo)
    for i, hour in enumerate(arquivo):
        prox = i + hora
        if prox == size:
            break
        saida = []
        saida.append(float(arquivo[prox][variavel]))
        output.append(saida)
    #normf = Norm(output)
    #norm_target = normf(output)
    return output


def main():
    arquivo = __lerarquivo__()
    #variaveis = ['t', 'chuva', 'radiacao']
    variaveis = ['radiacao']
    for i in range(1, 7):
        for variavel in variaveis:
            normalizado = __normaliza__(arquivo, i, variavel)
            __salvararquivo__(normalizado, i, variavel)
